# download_course.py
# Unified Canvas downloader: PDFs + Discussions
# Usage: python download_course.py <COURSE_NAME> <COURSE_ID>
# Example: python download_course.py ECO310 20994
#
# Or run without arguments to download all configured courses:
# python download_course.py --all
#
# Flags:
#   --no-discussions   Skip discussion downloads
#   --discussions-only Only download discussions (skip PDFs)

import os
import re
import sys
import time
import json
import pathlib
import argparse
import requests
from html.parser import HTMLParser
from urllib.parse import urlparse
from typing import Dict, Iterable, List, Optional

# Load .env file if it exists (simple implementation without python-dotenv)
def load_env():
    env_file = pathlib.Path(__file__).parent.parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

load_env()

# ====== CONFIG ======
BASE_URL     = "https://princeton.instructure.com"
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN", "")  # Set via environment variable
REPO_ROOT    = pathlib.Path(__file__).parent.parent
COURSES_FILE = pathlib.Path(__file__).parent / "courses.json"
PER_PAGE     = 100
# ====================

def course_materials_dir(course_name: str) -> pathlib.Path:
    """Get the materials directory for a course.

    Current courses:  {REPO_ROOT}/{course_name}/materials/
    Past courses:     {REPO_ROOT}/_archive/past-courses/{course_name}/materials/
    """
    data = load_courses()
    if course_name in data.get("past", {}):
        return REPO_ROOT / "_archive" / "past-courses" / course_name / "materials"
    return REPO_ROOT / course_name / "materials"

def load_courses() -> Dict:
    """Load courses from JSON file, or return defaults if file doesn't exist."""
    default_courses = {
        "current": {
            "ASA201": 21131,
            "MUS262": 20893,
            "ORF309": 20650,
            "ECO310": 20994,
        },
        "past": {
            "ECO362": 19196,
            "MAT201": 15323,
            "ORF245": 17181,
            "ORF307": 18899,
            "PSY254": 18965,
            "SPI387": 19569,
        }
    }
    if COURSES_FILE.exists():
        try:
            with open(COURSES_FILE, "r") as f:
                data = json.load(f)
                # Handle old format (flat dict) -> convert to new format
                if "current" not in data and "past" not in data:
                    return {"current": data, "past": {}}
                return data
        except (json.JSONDecodeError, IOError):
            return default_courses
    else:
        save_courses(default_courses)
        return default_courses

def save_courses(courses: Dict) -> None:
    """Save courses to JSON file."""
    with open(COURSES_FILE, "w") as f:
        json.dump(courses, f, indent=2)

def get_all_courses(data: Dict) -> Dict[str, int]:
    """Get all courses (current + past) as flat dict."""
    all_courses = {}
    all_courses.update(data.get("current", {}))
    all_courses.update(data.get("past", {}))
    return all_courses

def find_course(data: Dict, name: str) -> Optional[int]:
    """Find a course ID by name in either bucket."""
    if name in data.get("current", {}):
        return data["current"][name]
    if name in data.get("past", {}):
        return data["past"][name]
    return None

def add_course(name: str, course_id: int, bucket: str = "current") -> None:
    """Add a course to the config and save."""
    data = load_courses()
    if bucket not in data:
        data[bucket] = {}
    data[bucket][name] = course_id
    save_courses(data)
    print(f"Added {name} (ID: {course_id}) to {bucket} courses")

def move_course(name: str, to_bucket: str) -> bool:
    """Move a course between current and past."""
    data = load_courses()
    from_bucket = "past" if to_bucket == "current" else "current"

    if name in data.get(from_bucket, {}):
        course_id = data[from_bucket].pop(name)
        if to_bucket not in data:
            data[to_bucket] = {}
        data[to_bucket][name] = course_id
        save_courses(data)
        return True
    return False

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {ACCESS_TOKEN}"})

def paginate(url: str, params: Optional[Dict]=None) -> Iterable[Dict]:
    """Yield JSON items across Canvas pagination via Link headers."""
    params = dict(params or {})
    params.setdefault("per_page", PER_PAGE)
    while url:
        r = session.get(url, params=params)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list):
            for item in data:
                yield item
        else:
            yield data
        next_url = None
        if "Link" in r.headers:
            links = parse_link_header(r.headers["Link"])
            next_url = links.get("next")
        url, params = next_url, None

def parse_link_header(value: str) -> Dict[str, str]:
    """Parse RFC5988 Link header into {'rel': url}."""
    links = {}
    for part in value.split(","):
        section = part.split(";")
        if len(section) < 2:
            continue
        url = section[0].strip().lstrip("<").rstrip(">")
        rel = None
        for attr in section[1:]:
            attr = attr.strip()
            if attr.startswith("rel="):
                rel = attr.split("=", 1)[1].strip('"')
        if url and rel:
            links[rel] = url
    return links

def sanitize(name: str) -> str:
    name = name.strip().replace(":", " -")
    return re.sub(r'[\\/*?:"<>|]+', "_", name)

def ensure_dir(p: pathlib.Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def backoff_sleep(i: int):
    time.sleep(min(8, 1.5 * i))

def is_pdf_by_name_or_type(name: Optional[str], content_type: Optional[str]) -> bool:
    if content_type and content_type.lower() == "application/pdf":
        return True
    if name and name.lower().endswith(".pdf"):
        return True
    return False

def get_file_details(file_id: int) -> Optional[Dict]:
    url = f"{BASE_URL}/api/v1/files/{file_id}"
    for attempt in range(5):
        r = session.get(url)
        if r.status_code == 429:
            backoff_sleep(attempt + 1)
            continue
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()
    return None

def download_file(url: str, dest_path: pathlib.Path) -> None:
    tmp_path = dest_path.with_suffix(dest_path.suffix + ".part")
    with session.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(tmp_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if chunk:
                    f.write(chunk)
    tmp_path.replace(dest_path)

# ====== HTML TO MARKDOWN (for discussions) ======

class HTMLToMarkdown(HTMLParser):
    """Simple HTML to markdown converter for discussion posts."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.current_tag = None
        self.in_list = False
        self.list_type = None
        self._pending_href = ""

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'p':
            self.result.append('\n')
        elif tag == 'br':
            self.result.append('\n')
        elif tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag == 'ul':
            self.in_list = True
            self.list_type = 'ul'
        elif tag == 'ol':
            self.in_list = True
            self.list_type = 'ol'
        elif tag == 'li':
            self.result.append('\n- ' if self.list_type == 'ul' else '\n1. ')
        elif tag == 'a':
            self._pending_href = dict(attrs).get('href', '')
            self.result.append('[')
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            level = int(tag[1])
            self.result.append('\n' + '#' * level + ' ')

    def handle_endtag(self, tag):
        if tag in ('strong', 'b'):
            self.result.append('**')
        elif tag in ('em', 'i'):
            self.result.append('*')
        elif tag == 'a':
            self.result.append(f']({self._pending_href})')
        elif tag == 'p':
            self.result.append('\n')
        elif tag in ('ul', 'ol'):
            self.in_list = False
            self.result.append('\n')
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.result.append('\n')

    def handle_data(self, data):
        self.result.append(data)

    def get_text(self):
        return ''.join(self.result).strip()


def html_to_markdown(html_content: str) -> str:
    if not html_content:
        return ""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    text = parser.get_text()
    return re.sub(r'\n{3,}', '\n\n', text)


def format_discussion_entry(entry: Dict, participants: Dict, indent: int = 0) -> str:
    """Format a single discussion entry as markdown."""
    lines = []
    prefix = "  " * indent

    user_name = entry.get("user_name") or participants.get(entry.get("user_id"), "Unknown")
    created = (entry.get("created_at") or "")[:10]
    message = html_to_markdown(entry.get("message", ""))

    if indent == 0:
        lines.append(f"\n---\n")
        lines.append(f"**{user_name}** ({created}):\n")
    else:
        lines.append(f"\n{prefix}> **{user_name}** ({created}):\n")

    if message:
        if indent > 0:
            for msg_line in message.split('\n'):
                lines.append(f"{prefix}> {msg_line}")
        else:
            lines.append(message)
    lines.append("")

    for reply in (entry.get("replies") or []):
        if "user_name" not in reply:
            reply["user_name"] = participants.get(reply.get("user_id"), "Unknown")
        lines.append(format_discussion_entry(reply, participants, indent + 1))

    return "\n".join(lines)


def download_discussions(course_name: str, course_id: int) -> Dict[str, int]:
    """Download all discussion topics and replies for a course."""
    disc_dir = course_materials_dir(course_name) / "Discussions"
    ensure_dir(disc_dir)

    print(f"\n{'='*50}")
    print(f"Downloading discussions: {course_name} (ID: {course_id})")
    print(f"{'='*50}")

    topics_url = f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics"
    topics = list(paginate(topics_url, params={"order_by": "position"}))
    print(f"Found {len(topics)} discussion topics")

    stats = {"topics": len(topics), "saved": 0, "total_replies": 0}

    for i, topic in enumerate(topics, 1):
        title = topic.get("title", f"Discussion {topic.get('id', 'unknown')}")
        topic_id = topic.get("id")
        posted_at = (topic.get("posted_at") or topic.get("created_at") or "")[:10]

        safe_title = sanitize(title)[:80]
        filepath = disc_dir / f"{safe_title}.md"

        print(f"\n  [{i}/{len(topics)}] {title}")

        # Get full topic view with nested replies
        try:
            r = session.get(f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics/{topic_id}/view")
            r.raise_for_status()
            full_view = r.json()
        except requests.HTTPError:
            full_view = {}

        # Build markdown
        md_lines = [f"# {title}\n"]
        if posted_at:
            md_lines.append(f"**Posted:** {posted_at}\n")
        author = topic.get("author", {}).get("display_name", "")
        if author:
            md_lines.append(f"**Author:** {author}\n")

        body = html_to_markdown(topic.get("message", ""))
        if body:
            md_lines.append(f"\n## Discussion Prompt\n")
            md_lines.append(body)
            md_lines.append("")

        participants = {p["id"]: p.get("display_name", "Unknown")
                       for p in full_view.get("participants", [])}
        view_entries = full_view.get("view", []) or []

        if view_entries:
            md_lines.append(f"\n## Replies ({len(view_entries)} top-level)\n")
            reply_count = 0
            for entry in view_entries:
                if "user_name" not in entry:
                    entry["user_name"] = participants.get(entry.get("user_id"), "Unknown")
                md_lines.append(format_discussion_entry(entry, participants))
                reply_count += 1 + len(entry.get("replies") or [])
            stats["total_replies"] += reply_count
            print(f"    {reply_count} replies")
        else:
            md_lines.append("\n*No replies yet.*\n")
            print(f"    No replies")

        filepath.write_text("\n".join(md_lines), encoding="utf-8")
        stats["saved"] += 1
        print(f"    -> {filepath.name}")
        time.sleep(0.3)

    return stats


def print_discussion_summary(course_name: str, stats: Dict[str, int]):
    print(f"\n--- {course_name} Discussions ---")
    print(f"  Topics found:   {stats['topics']}")
    print(f"  Files saved:    {stats['saved']}")
    print(f"  Total replies:  {stats['total_replies']}")


# ====== ANNOUNCEMENTS DOWNLOAD ======

def download_announcements(course_name: str, course_id: int) -> Dict[str, int]:
    """Download all announcements for a course."""
    ann_dir = course_materials_dir(course_name) / "Announcements"
    ensure_dir(ann_dir)

    print(f"\n{'='*50}")
    print(f"Downloading announcements: {course_name} (ID: {course_id})")
    print(f"{'='*50}")

    ann_url = f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics"
    announcements = list(paginate(ann_url, params={"only_announcements": True, "order_by": "recent_activity"}))
    print(f"Found {len(announcements)} announcements")

    stats = {"found": len(announcements), "saved": 0}

    for i, ann in enumerate(announcements, 1):
        title = ann.get("title", f"Announcement {ann.get('id', 'unknown')}")
        posted_at = (ann.get("posted_at") or ann.get("created_at") or "")[:10]

        safe_title = sanitize(title)[:80]
        filepath = ann_dir / f"{posted_at}_{safe_title}.md"

        print(f"\n  [{i}/{len(announcements)}] {title}")

        # Build markdown
        md_lines = [f"# {title}\n"]
        if posted_at:
            md_lines.append(f"**Posted:** {posted_at}\n")
        author = ann.get("author", {}).get("display_name", "")
        if author:
            md_lines.append(f"**Author:** {author}\n")

        message = html_to_markdown(ann.get("message", ""))
        if message:
            md_lines.append(f"\n{message}\n")

        filepath.write_text("\n".join(md_lines), encoding="utf-8")
        stats["saved"] += 1
        print(f"    -> {filepath.name}")
        time.sleep(0.2)

    return stats


def print_announcement_summary(course_name: str, stats: Dict[str, int]):
    print(f"\n--- {course_name} Announcements ---")
    print(f"  Found:  {stats['found']}")
    print(f"  Saved:  {stats['saved']}")


# ====== ASSIGNMENTS DOWNLOAD ======

def download_assignments(course_name: str, course_id: int) -> Dict[str, int]:
    """Download all assignments for a course."""
    assign_dir = course_materials_dir(course_name) / "Assignments"
    ensure_dir(assign_dir)

    print(f"\n{'='*50}")
    print(f"Downloading assignments: {course_name} (ID: {course_id})")
    print(f"{'='*50}")

    assign_url = f"{BASE_URL}/api/v1/courses/{course_id}/assignments"
    assignments = list(paginate(assign_url))
    print(f"Found {len(assignments)} assignments")

    stats = {"found": len(assignments), "saved": 0}

    for i, assign in enumerate(assignments, 1):
        name = assign.get("name", f"Assignment {assign.get('id', 'unknown')}")
        due_at = (assign.get("due_at") or "")[:10]
        points = assign.get("points_possible", 0)

        safe_name = sanitize(name)[:80]
        filepath = assign_dir / f"{due_at}_{safe_name}.md" if due_at else assign_dir / f"{safe_name}.md"

        print(f"\n  [{i}/{len(assignments)}] {name}")

        # Build markdown
        md_lines = [f"# {name}\n"]
        if due_at:
            md_lines.append(f"**Due Date:** {due_at}\n")
        if points:
            md_lines.append(f"**Points:** {points}\n")

        description = html_to_markdown(assign.get("description", ""))
        if description:
            md_lines.append(f"\n## Description\n")
            md_lines.append(description)
            md_lines.append("")

        # Add submission info if available
        submission_types = assign.get("submission_types", [])
        if submission_types:
            md_lines.append(f"\n## Submission Types\n")
            for sub_type in submission_types:
                md_lines.append(f"- {sub_type}")
            md_lines.append("")

        # Add HTML URL
        html_url = assign.get("html_url", "")
        if html_url:
            md_lines.append(f"\n**Canvas Link:** {html_url}\n")

        filepath.write_text("\n".join(md_lines), encoding="utf-8")
        stats["saved"] += 1
        print(f"    -> {filepath.name}")
        time.sleep(0.2)

    return stats


def print_assignment_summary(course_name: str, stats: Dict[str, int]):
    print(f"\n--- {course_name} Assignments ---")
    print(f"  Found:  {stats['found']}")
    print(f"  Saved:  {stats['saved']}")


# ====== PDF DOWNLOAD ======

def download_course(course_name: str, course_id: int) -> Dict[str, int]:
    """Download all PDFs for a single course. Returns stats dict."""
    out_dir = course_materials_dir(course_name)
    ensure_dir(out_dir)

    print(f"\n{'='*50}")
    print(f"Downloading: {course_name} (ID: {course_id})")
    print(f"{'='*50}")

    modules_url = f"{BASE_URL}/api/v1/courses/{course_id}/modules"
    modules = list(paginate(modules_url, params={"include[]": "items"}))

    print(f"Found {len(modules)} modules")

    stats = {"seen": 0, "pdf": 0, "saved": 0, "skipped": 0}

    for m in modules:
        m_name = sanitize(m.get("name", f"module_{m.get('id','unknown')}"))
        mod_dir = out_dir / m_name
        ensure_dir(mod_dir)

        items = m.get("items") or []
        print(f"\nModule: {m_name} - {len(items)} items")

        for it in items:
            stats["seen"] += 1
            if it.get("type") != "File":
                continue

            file_id = it.get("content_id")
            item_title = it.get("title") or it.get("html_url") or f"file_{file_id}"
            file_meta = get_file_details(file_id) if file_id else None

            if not file_meta:
                print(f"  -Skipped (no file details): {item_title}")
                continue

            locked = file_meta.get("locked_for_user") or file_meta.get("lock_at") or file_meta.get("hidden_for_user")
            if locked:
                print(f"  -Skipped (locked/hidden): {file_meta.get('display_name', item_title)}")
                continue

            display_name = file_meta.get("display_name") or item_title
            content_type = (file_meta.get("content-type") or file_meta.get("content_type"))
            url = file_meta.get("url")

            if not is_pdf_by_name_or_type(display_name, content_type):
                if url and urlparse(url).path.lower().endswith(".pdf"):
                    pass
                else:
                    continue

            stats["pdf"] += 1
            fname = sanitize(display_name if display_name.lower().endswith(".pdf") else display_name + ".pdf")
            dest = mod_dir / fname

            if dest.exists():
                print(f"  [OK] Already exists: {display_name}")
                stats["skipped"] += 1
                continue

            try:
                if not url:
                    print(f"  -Skipped (no download URL): {display_name}")
                    continue

                print(f"  >> Downloading: {display_name}")
                download_file(url, dest)
                stats["saved"] += 1

            except requests.HTTPError as e:
                print(f"  ! HTTP error {e.response.status_code} on {display_name}")
            except Exception as e:
                print(f"  ! Error on {display_name}: {e}")

    return stats

def print_summary(course_name: str, stats: Dict[str, int]):
    print(f"\n--- {course_name} Summary ---")
    print(f"Module items scanned: {stats['seen']}")
    print(f"PDF candidates found: {stats['pdf']}")
    print(f"Already existed:      {stats['skipped']}")
    print(f"Newly downloaded:     {stats['saved']}")

def print_courses_list(data: Dict):
    """Pretty print the courses list."""
    print("\nCURRENT COURSES:")
    if data.get("current"):
        for name, cid in data["current"].items():
            print(f"  -{name}: {cid}")
    else:
        print("  (none)")

    print("\nPAST COURSES:")
    if data.get("past"):
        for name, cid in data["past"].items():
            print(f"  -{name}: {cid}")
    else:
        print("  (none)")

def sync_course(course_name: str, course_id: int, do_pdfs: bool, do_discussions: bool,
                do_announcements: bool = False, do_assignments: bool = False):
    """Run PDF download and/or discussion sync for a single course."""
    pdf_stats = None
    disc_stats = None
    ann_stats = None
    assign_stats = None

    if do_pdfs:
        pdf_stats = download_course(course_name, course_id)
        print_summary(course_name, pdf_stats)
    if do_discussions:
        disc_stats = download_discussions(course_name, course_id)
        print_discussion_summary(course_name, disc_stats)
    if do_announcements:
        ann_stats = download_announcements(course_name, course_id)
        print_announcement_summary(course_name, ann_stats)
    if do_assignments:
        assign_stats = download_assignments(course_name, course_id)
        print_assignment_summary(course_name, assign_stats)

    return pdf_stats, disc_stats, ann_stats, assign_stats


def main():
    parser = argparse.ArgumentParser(description="Download Canvas course PDFs and discussions")
    parser.add_argument("course_name", nargs="?", help="Course name (e.g., ECO310)")
    parser.add_argument("course_id", nargs="?", type=int, help="Course ID (e.g., 20994)")
    parser.add_argument("--all", action="store_true", help="Download all current courses")
    parser.add_argument("--all-courses", action="store_true", help="Download ALL courses (current + past)")
    parser.add_argument("--list", action="store_true", help="List all configured courses")
    parser.add_argument("--remove", metavar="COURSE", help="Remove a course from config")
    parser.add_argument("--archive", metavar="COURSE", help="Move a course to past")
    parser.add_argument("--unarchive", metavar="COURSE", help="Move a course to current")
    parser.add_argument("--past", action="store_true", help="Add new course to past instead of current")
    parser.add_argument("--no-discussions", action="store_true", help="Skip discussion downloads")
    parser.add_argument("--discussions-only", action="store_true", help="Only download discussions (skip PDFs)")
    parser.add_argument("--announcements", action="store_true", help="Download announcements")
    parser.add_argument("--assignments", action="store_true", help="Download assignments")
    parser.add_argument("--content-only", action="store_true", help="Download announcements + assignments (skip PDFs/discussions)")
    args = parser.parse_args()

    do_pdfs = not args.discussions_only and not args.content_only
    do_discussions = not args.no_discussions and not args.content_only
    do_announcements = args.announcements or args.content_only
    do_assignments = args.assignments or args.content_only

    data = load_courses()

    if args.list:
        print_courses_list(data)
        return

    if args.remove:
        removed = False
        if args.remove in data.get("current", {}):
            del data["current"][args.remove]
            removed = True
        elif args.remove in data.get("past", {}):
            del data["past"][args.remove]
            removed = True
        if removed:
            save_courses(data)
            print(f"Removed {args.remove}")
        else:
            print(f"Course {args.remove} not found")
        return

    if args.archive:
        if move_course(args.archive, "past"):
            print(f"Moved {args.archive} to past courses")
        else:
            print(f"Course {args.archive} not found in current courses")
        return

    if args.unarchive:
        if move_course(args.unarchive, "current"):
            print(f"Moved {args.unarchive} to current courses")
        else:
            print(f"Course {args.unarchive} not found in past courses")
        return

    if args.all:
        current = data.get("current", {})
        if not current:
            print("No current courses configured.")
            return
        print(f"Syncing {len(current)} current courses...")
        all_pdf_stats = {}
        all_disc_stats = {}
        all_ann_stats = {}
        all_assign_stats = {}
        for name, cid in current.items():
            pdf_s, disc_s, ann_s, assign_s = sync_course(name, cid, do_pdfs, do_discussions, do_announcements, do_assignments)
            if pdf_s:
                all_pdf_stats[name] = pdf_s
            if disc_s:
                all_disc_stats[name] = disc_s
            if ann_s:
                all_ann_stats[name] = ann_s
            if assign_s:
                all_assign_stats[name] = assign_s

        print(f"\n{'='*50}")
        print("OVERALL SUMMARY")
        print(f"{'='*50}")
        if all_pdf_stats:
            total_saved = sum(s["saved"] for s in all_pdf_stats.values())
            total_skipped = sum(s["skipped"] for s in all_pdf_stats.values())
            print(f"PDFs newly downloaded:  {total_saved}")
            print(f"PDFs already existed:   {total_skipped}")
        if all_disc_stats:
            total_topics = sum(s["topics"] for s in all_disc_stats.values())
            total_replies = sum(s["total_replies"] for s in all_disc_stats.values())
            print(f"Discussion topics:      {total_topics}")
            print(f"Total replies:          {total_replies}")
        if all_ann_stats:
            total_ann = sum(s["saved"] for s in all_ann_stats.values())
            print(f"Announcements saved:    {total_ann}")
        if all_assign_stats:
            total_assign = sum(s["saved"] for s in all_assign_stats.values())
            print(f"Assignments saved:      {total_assign}")
        print(f"Saved to: {REPO_ROOT.resolve()}")
        return

    if args.all_courses:
        all_courses = get_all_courses(data)
        if not all_courses:
            print("No courses configured.")
            return
        print(f"Syncing ALL {len(all_courses)} courses (current + past)...")
        all_pdf_stats = {}
        all_disc_stats = {}
        all_ann_stats = {}
        all_assign_stats = {}
        for name, cid in all_courses.items():
            pdf_s, disc_s, ann_s, assign_s = sync_course(name, cid, do_pdfs, do_discussions, do_announcements, do_assignments)
            if pdf_s:
                all_pdf_stats[name] = pdf_s
            if disc_s:
                all_disc_stats[name] = disc_s
            if ann_s:
                all_ann_stats[name] = ann_s
            if assign_s:
                all_assign_stats[name] = assign_s

        print(f"\n{'='*50}")
        print("OVERALL SUMMARY")
        print(f"{'='*50}")
        if all_pdf_stats:
            total_saved = sum(s["saved"] for s in all_pdf_stats.values())
            total_skipped = sum(s["skipped"] for s in all_pdf_stats.values())
            print(f"PDFs newly downloaded:  {total_saved}")
            print(f"PDFs already existed:   {total_skipped}")
        if all_disc_stats:
            total_topics = sum(s["topics"] for s in all_disc_stats.values())
            total_replies = sum(s["total_replies"] for s in all_disc_stats.values())
            print(f"Discussion topics:      {total_topics}")
            print(f"Total replies:          {total_replies}")
        if all_ann_stats:
            total_ann = sum(s["saved"] for s in all_ann_stats.values())
            print(f"Announcements saved:    {total_ann}")
        if all_assign_stats:
            total_assign = sum(s["saved"] for s in all_assign_stats.values())
            print(f"Assignments saved:      {total_assign}")
        print(f"Saved to: {REPO_ROOT.resolve()}")
        return

    if args.course_name and args.course_id:
        existing = find_course(data, args.course_name)
        if not existing:
            bucket = "past" if args.past else "current"
            add_course(args.course_name, args.course_id, bucket)
        sync_course(args.course_name, args.course_id, do_pdfs, do_discussions, do_announcements, do_assignments)
        print(f"Saved to: {course_materials_dir(args.course_name).resolve()}")
    elif args.course_name:
        course_id = find_course(data, args.course_name)
        if course_id:
            sync_course(args.course_name, course_id, do_pdfs, do_discussions, do_announcements, do_assignments)
            print(f"Saved to: {course_materials_dir(args.course_name).resolve()}")
        else:
            print(f"Course {args.course_name} not found. Add it with:")
            print(f"  python download_course.py {args.course_name} <COURSE_ID>")
    else:
        print("Usage:")
        print("  python download_course.py --all                     (sync current courses)")
        print("  python download_course.py --all-courses             (sync ALL courses)")
        print("  python download_course.py <COURSE_NAME> <COURSE_ID> (add & download)")
        print("  python download_course.py <COURSE_NAME>             (download existing)")
        print("  python download_course.py --list                    (show all courses)")
        print("  python download_course.py --archive <COURSE>        (move to past)")
        print("  python download_course.py --unarchive <COURSE>      (move to current)")
        print("  python download_course.py --remove <COURSE>         (delete from config)")
        print("  python download_course.py --no-discussions          (skip discussions)")
        print("  python download_course.py --discussions-only        (only discussions)")
        print("  python download_course.py --announcements           (download announcements)")
        print("  python download_course.py --assignments             (download assignments)")
        print("  python download_course.py --content-only            (announcements + assignments only)")
        print_courses_list(data)

if __name__ == "__main__":
    main()
