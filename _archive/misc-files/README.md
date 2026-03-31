# Canvas - Course Organization Hub

**Spring 2026 Courses**

---

## Active Courses

| Course | Description | Key Folders |
|--------|-------------|-------------|
| [ECO310](ECO310/) | Intermediate Microeconomics | [materials](ECO310/materials/), [study](ECO310/study/) |
| [ASA201](ASA201/) | Asian American Studies | [materials](ASA201/materials/), [study](ASA201/study/) |
| [MUS262](MUS262/) | Jazz History | [materials](MUS262/materials/), [study](MUS262/study/) |
| [ORF309](ORF309/) | Probability & Stochastic Processes | [materials](ORF309/materials/), [study](ORF309/study/) |

Each course has exactly two folders: `materials/` (Canvas-synced teacher content) and `study/` (your work).

---

## Directory Structure

```
Canvas/
  {COURSE}/
    materials/       All Canvas content (synced by download_course.py)
    study/           Your work (solutions, notes, trackers, papers)

  scripts/           Shared Canvas API tools (download_course.py, etc.)
  _archive/          Past courses, old docs, personal notes
```

---

## Tools

### Syncing from Canvas

```bash
# Sync all current courses
python scripts/download_course.py --all

# Sync a single course
python scripts/download_course.py ECO310

# Sync only discussions
python scripts/download_course.py --all --discussions-only

# Download announcements + assignments
python scripts/download_course.py --all --content-only
```

New downloads land directly in each course's `materials/` folder.

---

## Archive

The [_archive](_archive/) folder contains:
- **past-courses/** -- ECO362, MAT201, ORF245, ORF307, PSY254, SPI387, URB201
- **meta/** -- Old repo management docs
- **personal/** -- Personal productivity notes, academic calendar
