#!/usr/bin/env python3
"""Get full announcement details."""

import requests
import re
import os

BASE_URL = "https://princeton.instructure.com"
ACCESS_TOKEN = os.getenv("CANVAS_ACCESS_TOKEN", "")  # Set via environment variable
ECO310_COURSE_ID = 20994

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {ACCESS_TOKEN}"})

# Get announcements
url = f"{BASE_URL}/api/v1/courses/{ECO310_COURSE_ID}/discussion_topics"
params = {"only_announcements": True, "per_page": 10}
r = session.get(url, params=params)
announcements = r.json()

# Find the midterm info announcement
for ann in announcements:
    if "Midterm Info" in ann.get("title", ""):
        print("="*70)
        print(f"TITLE: {ann.get('title')}")
        print(f"POSTED: {ann.get('posted_at', '')[:10]}")
        print("="*70)
        print()

        message = ann.get("message", "")

        # Strip HTML tags
        clean = re.sub(r'<[^>]+>', '', message)
        clean = re.sub(r'&amp;', '&', clean)
        clean = re.sub(r'&lt;', '<', clean)
        clean = re.sub(r'&gt;', '>', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()

        print(clean)
        print()
        print("="*70)
        break
