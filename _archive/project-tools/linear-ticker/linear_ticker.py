#!/usr/bin/env python3
"""
Linear Ticker - Display Linear issues in a maximized window in the current workspace
"""

import os
import sys
import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
import subprocess
from typing import List, Dict, Any

# Linear API Configuration
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")  # Set via environment variable or .env file
LINEAR_API_URL = "https://api.linear.app/graphql"

TEAM_IDS = {
    "Engineering": "5d82889a-d2da-4418-a03f-ab40fbd7fa0f",
    "Withai": "1d90e365-7f76-48d0-8229-0ef04cccf7d2"
}


class LinearTicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Ticker")

        # Configure window to open in current workspace and maximize
        self.setup_window()

        # Configure colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.accent_color = "#5e6ad2"

        self.root.configure(bg=self.bg_color)

        # Create UI
        self.create_header()
        self.create_issue_list()
        self.create_footer()

        # Load issues
        self.refresh_issues()

        # Auto-refresh every 5 minutes
        self.auto_refresh()

    def setup_window(self):
        """Configure window to open maximized in current workspace"""
        # Set window to open in current workspace (not spawn on different desktop)
        self.root.attributes('-topmost', False)

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window to full screen size
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Maximize the window using macOS native command
        self.root.update_idletasks()

        # Use AppleScript to ensure window opens in current workspace and maximizes
        try:
            script = '''
            tell application "System Events"
                tell process "Python"
                    set frontmost to true
                    tell window 1
                        set value of attribute "AXFullScreen" to true
                    end tell
                end tell
            end tell
            '''
            subprocess.run(['osascript', '-e', script], capture_output=True)
        except Exception as e:
            # Fallback: just maximize to screen size
            self.root.state('zoomed')

    def create_header(self):
        """Create header with title and refresh button"""
        header_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Linear Ticker",
            font=("SF Pro Display", 32, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(side=tk.LEFT)

        # Last updated label
        self.last_updated_label = tk.Label(
            header_frame,
            text="",
            font=("SF Pro Display", 12),
            bg=self.bg_color,
            fg="#888888"
        )
        self.last_updated_label.pack(side=tk.LEFT, padx=20)

        # Refresh button
        refresh_btn = tk.Button(
            header_frame,
            text="↻ Refresh",
            font=("SF Pro Display", 14),
            bg=self.accent_color,
            fg=self.fg_color,
            relief=tk.FLAT,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.refresh_issues
        )
        refresh_btn.pack(side=tk.RIGHT)

    def create_issue_list(self):
        """Create scrollable list of issues"""
        # Container for list
        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas for scrolling
        self.canvas = tk.Canvas(
            list_frame,
            bg=self.bg_color,
            highlightthickness=0,
            yscrollcommand=scrollbar.set
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)

        # Frame inside canvas
        self.issues_frame = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.issues_frame, anchor=tk.NW)

        # Bind scroll events
        self.issues_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def create_footer(self):
        """Create footer with stats"""
        self.footer_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        self.footer_frame.pack(fill=tk.X)

        self.stats_label = tk.Label(
            self.footer_frame,
            text="",
            font=("SF Pro Display", 12),
            bg=self.bg_color,
            fg="#888888"
        )
        self.stats_label.pack()

    def on_frame_configure(self, event):
        """Update scroll region when frame size changes"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        """Handle mousewheel scrolling"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def fetch_issues(self) -> List[Dict[str, Any]]:
        """Fetch issues from Linear API"""
        query = """
        query {
          issues(
            filter: {
              team: { id: { in: ["%s", "%s"] } }
              state: { type: { neq: "completed" } }
            }
            orderBy: updatedAt
            first: 100
          ) {
            nodes {
              id
              identifier
              title
              priority
              state {
                name
                type
              }
              assignee {
                name
              }
              labels {
                nodes {
                  name
                }
              }
              project {
                name
              }
              cycle {
                name
              }
              createdAt
              updatedAt
            }
          }
        }
        """ % (TEAM_IDS["Engineering"], TEAM_IDS["Withai"])

        headers = {
            "Authorization": LINEAR_API_KEY,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(
                LINEAR_API_URL,
                json={"query": query},
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            return data.get("data", {}).get("issues", {}).get("nodes", [])
        except Exception as e:
            print(f"Error fetching issues: {e}")
            return []

    def get_priority_emoji(self, priority: int) -> str:
        """Get emoji for priority level"""
        priority_map = {
            1: "🔴",
            2: "🟠",
            3: "🟡",
            4: "🔵"
        }
        return priority_map.get(priority, "⚪")

    def create_issue_card(self, issue: Dict[str, Any], parent: tk.Frame):
        """Create a card widget for an issue"""
        # Card frame
        card = tk.Frame(
            parent,
            bg="#2a2a2a",
            relief=tk.FLAT,
            padx=20,
            pady=15
        )
        card.pack(fill=tk.X, pady=5)

        # Top row: ID, Priority, Title
        top_row = tk.Frame(card, bg="#2a2a2a")
        top_row.pack(fill=tk.X)

        # Issue ID
        id_label = tk.Label(
            top_row,
            text=issue["identifier"],
            font=("SF Mono", 12, "bold"),
            bg="#2a2a2a",
            fg="#888888"
        )
        id_label.pack(side=tk.LEFT, padx=(0, 10))

        # Priority
        priority_label = tk.Label(
            top_row,
            text=self.get_priority_emoji(issue.get("priority", 0)),
            font=("Arial", 14),
            bg="#2a2a2a"
        )
        priority_label.pack(side=tk.LEFT, padx=(0, 10))

        # Title
        title_label = tk.Label(
            top_row,
            text=issue["title"],
            font=("SF Pro Display", 14),
            bg="#2a2a2a",
            fg=self.fg_color,
            anchor=tk.W
        )
        title_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Middle row: Labels, State
        middle_row = tk.Frame(card, bg="#2a2a2a")
        middle_row.pack(fill=tk.X, pady=(10, 0))

        # State
        state_name = issue.get("state", {}).get("name", "No State")
        state_label = tk.Label(
            middle_row,
            text=f"[{state_name}]",
            font=("SF Pro Display", 11),
            bg="#2a2a2a",
            fg="#888888"
        )
        state_label.pack(side=tk.LEFT, padx=(0, 10))

        # Labels
        labels = issue.get("labels", {}).get("nodes", [])
        if labels:
            for label in labels[:3]:  # Show max 3 labels
                label_widget = tk.Label(
                    middle_row,
                    text=label["name"],
                    font=("SF Pro Display", 10),
                    bg="#3a3a3a",
                    fg="#aaaaaa",
                    padx=8,
                    pady=2
                )
                label_widget.pack(side=tk.LEFT, padx=(0, 5))

        # Bottom row: Assignee, Project, Cycle
        bottom_row = tk.Frame(card, bg="#2a2a2a")
        bottom_row.pack(fill=tk.X, pady=(8, 0))

        info_parts = []

        if issue.get("assignee"):
            info_parts.append(f"👤 {issue['assignee']['name']}")

        if issue.get("project"):
            info_parts.append(f"📁 {issue['project']['name']}")

        if issue.get("cycle"):
            info_parts.append(f"🔄 {issue['cycle']['name']}")

        if info_parts:
            info_label = tk.Label(
                bottom_row,
                text=" • ".join(info_parts),
                font=("SF Pro Display", 10),
                bg="#2a2a2a",
                fg="#666666"
            )
            info_label.pack(side=tk.LEFT)

        # Make card clickable to open in Linear
        def open_in_linear(event):
            # Extract issue number from identifier (e.g., "ENG-123" -> "123")
            issue_id = issue["identifier"]
            # Open in browser
            subprocess.run(["open", f"https://linear.app/issue/{issue_id}"])

        card.bind("<Button-1>", open_in_linear)
        for widget in card.winfo_children():
            widget.bind("<Button-1>", open_in_linear)
            for child in widget.winfo_children():
                child.bind("<Button-1>", open_in_linear)

        # Change cursor on hover
        card.bind("<Enter>", lambda e: card.configure(bg="#3a3a3a"))
        card.bind("<Leave>", lambda e: card.configure(bg="#2a2a2a"))

    def refresh_issues(self):
        """Refresh the issue list"""
        # Clear existing issues
        for widget in self.issues_frame.winfo_children():
            widget.destroy()

        # Fetch new issues
        issues = self.fetch_issues()

        # Group issues by state
        states = {}
        for issue in issues:
            state = issue.get("state", {}).get("name", "No State")
            if state not in states:
                states[state] = []
            states[state].append(issue)

        # Display issues grouped by state
        for state, state_issues in states.items():
            # State header
            state_header = tk.Label(
                self.issues_frame,
                text=f"{state} ({len(state_issues)})",
                font=("SF Pro Display", 18, "bold"),
                bg=self.bg_color,
                fg=self.accent_color,
                anchor=tk.W
            )
            state_header.pack(fill=tk.X, pady=(20, 10))

            # Issues in this state
            for issue in state_issues:
                self.create_issue_card(issue, self.issues_frame)

        # Update last updated time
        now = datetime.now().strftime("%H:%M:%S")
        self.last_updated_label.config(text=f"Last updated: {now}")

        # Update stats
        total_issues = len(issues)
        self.stats_label.config(text=f"Total Issues: {total_issues}")

    def auto_refresh(self):
        """Auto-refresh issues every 5 minutes"""
        self.refresh_issues()
        self.root.after(300000, self.auto_refresh)  # 300000ms = 5 minutes


def main():
    root = tk.Tk()
    app = LinearTicker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
