# Linear Ticker

A macOS application that displays your Linear issues in a maximized window in your current workspace.

## Features

- Opens maximized in the current workspace (no spawning on different desktops)
- Real-time display of all active Linear issues
- Auto-refreshes every 5 minutes
- Click any issue to open it in Linear
- Groups issues by state
- Shows priority, labels, assignee, project, and cycle information
- Clean, dark-themed interface

## Setup

1. Make the launch script executable:
```bash
chmod +x launch.sh
```

2. Run the ticker:
```bash
./launch.sh
```

The first run will create a virtual environment and install dependencies automatically.

## Usage

- **Refresh**: Click the "↻ Refresh" button to manually refresh issues
- **Open Issue**: Click on any issue card to open it in Linear
- **Scroll**: Use mouse wheel or trackpad to scroll through issues
- **Auto-refresh**: Issues automatically refresh every 5 minutes

## Requirements

- macOS
- Python 3.7+
- Internet connection (for Linear API access)

## Configuration

The ticker uses the Linear API key configured in your `~/.claude/CLAUDE.md` file and displays issues from both Engineering and Withai teams.

To modify teams or settings, edit the `linear_ticker.py` file:
- `TEAM_IDS`: Dictionary of team names and IDs to display
- `auto_refresh()`: Change refresh interval (default: 5 minutes)
