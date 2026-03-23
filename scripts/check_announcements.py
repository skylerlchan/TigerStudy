#!/usr/bin/env python3
"""Check Canvas announcements for exam policies."""

import requests
import sys
from datetime import datetime

# Set UTF-8 encoding for output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# From download_course.py
BASE_URL = "https://princeton.instructure.com"
ACCESS_TOKEN = "12465~7Jk9uv8w9XvVhDWeuQZCQNXwnPnMwKKYMuLTmGe7fPe7fQBhThz2TLeFF8WUPNuB"
ECO310_COURSE_ID = 20994

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {ACCESS_TOKEN}"})

def get_announcements(course_id, limit=10):
    """Get recent course announcements."""
    url = f"{BASE_URL}/api/v1/courses/{course_id}/discussion_topics"
    params = {
        "only_announcements": True,
        "per_page": limit,
        "order_by": "recent_activity"
    }

    try:
        r = session.get(url, params=params)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Error fetching announcements: {e}")
        return []

def search_for_keywords(text, keywords):
    """Search text for keywords (case-insensitive)."""
    if not text:
        return []
    text_lower = text.lower()
    found = []
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return found

def main():
    print("Fetching ECO 310 announcements...\n")
    announcements = get_announcements(ECO310_COURSE_ID)

    if not announcements:
        print("No announcements found (or error accessing Canvas)")
        return

    print(f"Found {len(announcements)} recent announcements\n")
    print("="*70)

    # Keywords to search for
    exam_keywords = [
        "cheat sheet", "cheatsheet", "note sheet", "formula sheet",
        "open note", "open-note", "closed note", "open book",
        "calculator", "allowed", "permitted", "bring",
        "midterm", "exam policy"
    ]

    for i, ann in enumerate(announcements, 1):
        title = ann.get("title", "(No title)")
        message = ann.get("message", "")
        posted_at = ann.get("posted_at", "")

        # Parse date
        if posted_at:
            try:
                dt = datetime.fromisoformat(posted_at.replace('Z', '+00:00'))
                posted_str = dt.strftime("%B %d, %Y")
            except:
                posted_str = posted_at[:10]
        else:
            posted_str = "Unknown date"

        # Check for exam-related keywords
        found_keywords = search_for_keywords(title, exam_keywords)
        found_keywords += search_for_keywords(message, exam_keywords)

        print(f"\n[{i}] {title}")
        print(f"    Posted: {posted_str}")

        if found_keywords:
            print(f"    *** RELEVANT: Contains {', '.join(set(found_keywords))}")
            print(f"\n    Message preview:")
            # Strip HTML tags for preview
            import re
            clean_msg = re.sub(r'<[^>]+>', '', message)
            clean_msg = re.sub(r'\s+', ' ', clean_msg).strip()
            print(f"    {clean_msg[:300]}...")
        else:
            print(f"    (No exam policy keywords found)")

        print("-"*70)

    print("\n" + "="*70)
    print("\nKeywords searched:")
    print(", ".join(exam_keywords))
    print("\nIf a relevant announcement is found above, read the full message")
    print("on Canvas for complete details.")

if __name__ == "__main__":
    main()
