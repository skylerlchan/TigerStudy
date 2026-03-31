# Canvas Directory - Housekeeping & Organization Guide

**Last Updated:** 2026-02-28

---

## Overview

This document provides recommendations for organizing loose files in the Canvas root directory and maintaining a clean workspace.

**Current Status:**
- 4 active classes: ECO310, ASA201, MUS262, ORF309
- Each class now has a HOME.md file documenting all materials
- Root directory contains 11+ loose files that need organization

---

## Root Directory - Loose Files

### Current Loose Files (11 files):

#### Python Scripts (5 files):
1. `extract_hw_pdf.py` (445 B)
2. `extract_lln_pages.py` (837 B)
3. `extract_pdf.py` (587 B)
4. `extract_textbook.py` (1.4K)
5. `search_slides.py` (1.0K)

#### LaTeX Documents (5 files):
1. `chain_rule_explanation.tex` (3.0K)
2. `marshallian_demand_solution.tex` (5.9K)
3. `problem3_solution.tex` (4.5K)
4. `problem4_solution.tex` (3.6K)
5. `product_rule_explanation.tex` (4.3K)

#### Text/Data Files (4 files):
1. `homework04_text.txt` (2.9K)
2. `puar_text.txt` (108K)
3. `textbook_lln_pages.txt` (31K)
4. `textbook_relevant.txt` (115K)

#### Markdown:
1. `math_test.md` (415 B)

---

## Organization Recommendations

### 1. Python Scripts → `scripts/` directory

**Action:** Move all 5 Python files to existing `scripts/` directory

```bash
mv extract_hw_pdf.py scripts/
mv extract_lln_pages.py scripts/
mv extract_pdf.py scripts/
mv extract_textbook.py scripts/
mv search_slides.py scripts/
```

**Rationale:** These are utility scripts for PDF extraction and search. They belong in the scripts/ directory with other utilities.

### 2. LaTeX Documents → Appropriate Class Folders

#### Math/Economics Files → ECO310:
- `marshallian_demand_solution.tex` → **Already in root, compiled PDF in output/**
  - **Keep in root** OR move to `downloads/ECO310/Homework/`

- `chain_rule_explanation.tex` → Likely ECO310 (microeconomics uses calculus)
  - Move to `downloads/ECO310/study-guides/`

- `product_rule_explanation.tex` → Likely ECO310 or ORF309
  - Move to `downloads/ECO310/study-guides/` or `downloads/ORF309/notes/`

#### Problem Solutions → Likely ORF309:
- `problem3_solution.tex` → Check if this is ORF309 HW
  - Move to `downloads/ORF309/homework-work/`

- `problem4_solution.tex` → Check if this is ORF309 HW
  - Move to `downloads/ORF309/homework-work/`

### 3. Text Files → Appropriate Class Folders

#### ORF309 Files:
- `homework04_text.txt` → ORF309 HW4 extraction
  - Move to `downloads/ORF309/homework-work/`

- `textbook_lln_pages.txt` → ORF309 textbook (Law of Large Numbers)
  - Move to `downloads/ORF309/notes/`

- `textbook_relevant.txt` → ORF309 textbook extractions
  - Move to `downloads/ORF309/notes/`

#### ASA201 File:
- `puar_text.txt` (108K) → ASA201 reading (Puar - Terrorist Assemblages)
  - Move to `downloads/ASA201/Week 5 - Tuesday - Asian_America and Empire/`
  - OR create `downloads/ASA201/extracted_texts/` folder

### 4. Test File:
- `math_test.md` → Test/scratch file
  - **DELETE** (appears to be a test file)

---

## Proposed Organized Structure

### After Reorganization:

```
Canvas/
├── downloads/
│   ├── ECO310/
│   │   ├── HOME.md ✅
│   │   ├── study-guides/
│   │   │   ├── chain_rule_explanation.tex (moved)
│   │   │   └── product_rule_explanation.tex (moved)
│   │   └── Homework/
│   │       └── marshallian_demand_solution.tex (consider moving)
│   ├── ASA201/
│   │   ├── HOME.md ✅
│   │   └── extracted_texts/
│   │       └── puar_text.txt (moved)
│   ├── MUS262/
│   │   └── HOME.md ✅
│   └── ORF309/
│       ├── HOME.md ✅
│       ├── homework-work/
│       │   ├── problem3_solution.tex (moved)
│       │   ├── problem4_solution.tex (moved)
│       │   └── homework04_text.txt (moved)
│       └── notes/
│           ├── textbook_lln_pages.txt (moved)
│           └── textbook_relevant.txt (moved)
├── scripts/
│   ├── extract_hw_pdf.py (moved)
│   ├── extract_lln_pages.py (moved)
│   ├── extract_pdf.py (moved)
│   ├── extract_textbook.py (moved)
│   └── search_slides.py (moved)
├── output/
│   └── [compiled PDFs]
├── reference/
├── research/
├── study_plans/
├── _archive/
└── [other organized directories]
```

---

## Detailed File Assignment

### By Class:

#### ECO310 (Microeconomics):
- ✅ `marshallian_demand_solution.tex` - Demand function solution (keep in root or move to ECO310)
- 📦 `chain_rule_explanation.tex` - Calculus reference (→ ECO310/study-guides/)
- 📦 `product_rule_explanation.tex` - Calculus reference (→ ECO310/study-guides/)

#### ASA201 (Asian American Studies):
- 📦 `puar_text.txt` - Extracted reading text (→ ASA201/extracted_texts/)

#### ORF309 (Probability):
- 📦 `problem3_solution.tex` - Homework solution (→ ORF309/homework-work/)
- 📦 `problem4_solution.tex` - Homework solution (→ ORF309/homework-work/)
- 📦 `homework04_text.txt` - HW4 extraction (→ ORF309/homework-work/)
- 📦 `textbook_lln_pages.txt` - Textbook extract (→ ORF309/notes/)
- 📦 `textbook_relevant.txt` - Textbook extract (→ ORF309/notes/)

#### Utilities:
- 📦 `extract_hw_pdf.py` (→ scripts/)
- 📦 `extract_lln_pages.py` (→ scripts/)
- 📦 `extract_pdf.py` (→ scripts/)
- 📦 `extract_textbook.py` (→ scripts/)
- 📦 `search_slides.py` (→ scripts/)

#### Delete:
- ❌ `math_test.md` - Test file

---

## Step-by-Step Cleanup Commands

### Option 1: Move Files (Preserves everything)

```bash
# Python scripts to scripts/
mv extract_*.py scripts/
mv search_slides.py scripts/

# ECO310 files
mv chain_rule_explanation.tex downloads/ECO310/study-guides/
mv product_rule_explanation.tex downloads/ECO310/study-guides/

# ORF309 files
mv problem3_solution.tex downloads/ORF309/homework-work/
mv problem4_solution.tex downloads/ORF309/homework-work/
mv homework04_text.txt downloads/ORF309/homework-work/
mv textbook_lln_pages.txt downloads/ORF309/notes/
mv textbook_relevant.txt downloads/ORF309/notes/

# ASA201 files
mkdir -p downloads/ASA201/extracted_texts/
mv puar_text.txt downloads/ASA201/extracted_texts/

# Delete test file
rm math_test.md
```

### Option 2: Interactive Review

Before moving files, you may want to:
1. Open each .tex file to verify which class it belongs to
2. Check if text files are still needed or can be deleted
3. Verify that problem solutions match ORF309 homework

---

## Summary of Changes

### Files to Move: 14 files
- 5 Python scripts → `scripts/`
- 3 LaTeX files → Class folders
- 5 Text files → Class folders
- 1 Markdown file → DELETE

### Files to Keep in Root:
- `marshallian_demand_solution.tex` - Recently created, may want in root for easy access
- Existing directories (output/, downloads/, etc.)

### Space Impact:
- No significant space savings (just organization)
- Reduces root directory clutter from 11+ files to ~1-2 files

---

## Class-Specific Cleanup Summary

See individual class HOME.md files for detailed cleanup recommendations:

| Class | Files | Cleanup Tasks | Priority |
|-------|-------|---------------|----------|
| **ECO310** | 83 | Delete 2 duplicate precepts + 5 temp files | Medium |
| **ASA201** | 37 | Fix 1 filename, check small PDF, delete 5 empty folders | High |
| **MUS262** | 20 | Delete 4 LaTeX artifacts, 1 empty folder | Low |
| **ORF309** | 104 | Delete 1 duplicate syllabus + 1 temp file | Low |

**Total Across All Classes:** ~18 files can be deleted (mostly build artifacts and duplicates)

---

## Maintenance Tips

### Going Forward:

1. **New Files:** Place in appropriate class folder immediately
2. **Scripts:** Keep all Python/utility scripts in `scripts/`
3. **Build Artifacts:** Delete .aux, .log, .out, .toc files after LaTeX compilation
4. **Extractions:** Keep text extractions in class folders, not root
5. **Test Files:** Delete test/scratch files when no longer needed

### Regular Cleanup Schedule:

- **Weekly:** Delete LaTeX build artifacts
- **After Each Assignment:** Organize new files into class folders
- **End of Semester:** Archive old materials to `_archive/`

---

## Quick Reference

### HOME Pages Created:
- ✅ [downloads/ECO310/HOME.md](downloads/ECO310/HOME.md)
- ✅ [downloads/ASA201/HOME.md](downloads/ASA201/HOME.md)
- ✅ [downloads/MUS262/HOME.md](downloads/MUS262/HOME.md)
- ✅ [downloads/ORF309/HOME.md](downloads/ORF309/HOME.md)

Each HOME page includes:
- Complete file inventory
- Organization structure
- Duplicate identification
- Cleanup recommendations
- Quick stats

---

## Total Cleanup Summary

### Across Entire Canvas Directory:

| Action | Files | Space Saved |
|--------|-------|-------------|
| Delete duplicates | ~7 files | ~2 MB |
| Delete build artifacts | ~6 files | ~0.1 MB |
| Delete temp files | ~4 files | ~0.5 MB |
| Delete empty folders | ~6 folders | 0 MB |
| Move to organize | ~14 files | 0 MB (just organization) |
| **Total Changes** | **~37 items** | **~2.6 MB** |

**Total Current Size:** 43.9 MB (downloads) + 11.5 MB (root) + 26 MB (archive) = **81.4 MB**

**After Cleanup:** ~78.8 MB (3% reduction, but much better organization)

---

## Status

✅ All four classes now have HOME.md documentation
✅ All files inventoried and categorized
✅ Cleanup recommendations provided
✅ Organization plan created

**Next Steps:**
1. Review this housekeeping guide
2. Execute cleanup commands for files you want to delete
3. Move loose root files to appropriate locations
4. Maintain organization going forward
