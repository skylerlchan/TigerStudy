#!/usr/bin/env python3
"""Explore what's available via Canvas API for ECO310."""

import requests
import json
import sys
import io
import os

# Fix encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = "https://princeton.instructure.com"
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN", "")  # Set via environment variable
ECO310_COURSE_ID = 20994

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {ACCESS_TOKEN}"})

def test_endpoint(name, url, params=None):
    """Test an API endpoint and show what's available."""
    try:
        r = session.get(url, params=params or {})
        r.raise_for_status()
        data = r.json()

        if isinstance(data, list):
            count = len(data)
            sample = data[0] if data else None
        else:
            count = 1
            sample = data

        print(f"\n{'='*70}")
        print(f"[OK] {name}")
        print(f"  Endpoint: {url.replace(BASE_URL, '')}")
        print(f"  Count: {count} items")

        if sample:
            print(f"  Sample keys: {', '.join(list(sample.keys())[:10])}")

        return True
    except Exception as e:
        print(f"\n[FAIL] {name}: {e}")
        return False

print("EXPLORING CANVAS API FOR ECO 310")
print("="*70)

# Test various endpoints
endpoints = [
    ("Announcements", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/discussion_topics",
     {"only_announcements": True, "per_page": 5}),

    ("Assignments", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/assignments",
     {"per_page": 10}),

    ("Quizzes", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/quizzes",
     {"per_page": 10}),

    ("Pages", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/pages",
     {"per_page": 10}),

    ("Calendar Events", f"{BASE_URL}/api/v1/calendar_events",
     {"context_codes[]": f"course_{ECO310_COURSE_ID}", "per_page": 10}),

    ("Modules", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/modules",
     {"per_page": 10}),

    ("Discussion Topics (all)", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/discussion_topics",
     {"per_page": 10}),

    ("Course Info", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}", None),

    ("Tabs", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/tabs", None),

    ("Recent Activity", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/activity_stream",
     {"per_page": 10}),

    ("Submissions", f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/students/submissions",
     {"student_ids[]": "self", "per_page": 10}),
]

results = {}
for name, url, params in endpoints:
    results[name] = test_endpoint(name, url, params)

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print("\nAvailable endpoints:")
for name, available in results.items():
    status = "[OK]" if available else "[FAIL]"
    print(f"  {status} {name}")

print("\n" + "="*70)
print("RECOMMENDATION: Add these to download_course.py:")
print("  - Announcements (important updates)")
print("  - Assignments (due dates, descriptions)")
print("  - Pages (course content)")
print("  - Calendar Events (exam dates, office hours)")
print("="*70)
