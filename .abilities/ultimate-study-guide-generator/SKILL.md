# Ultimate Study Guide Generator

## Metadata
- **Name:** ultimate-study-guide-generator
- **Version:** 1.0.0
- **Author:** Claude
- **Created:** 2026-03-31
- **Specification:** agentskills.io v1.0

## Description
Creates comprehensive, beautifully formatted study guides for exams that are intuitive, well-organized, and highly effective. Analyzes past exams, identifies patterns, creates beginner-friendly explanations with worked examples, and generates both a full guide and a 2-page cheat sheet.

## When to Use
Use this skill when the user:
- Asks for a study guide for an upcoming exam
- Wants to prepare for a midterm or final
- Says "create a study guide like the ORF309 one"
- Needs comprehensive exam prep materials
- Has past exams available to analyze

## Key Features of the Output

### 1. Ultimate Study Guide (60+ pages PDF)
- **Beginner-friendly explanations** with real-world examples
- **Color-coded priority system**: RED (critical), GREEN (examples), ORANGE (formulas), YELLOW (warnings)
- **15+ fully worked examples** from actual past exams
- **Pattern recognition guide** (when you see X → use technique Y)
- **Complete formula sheets** organized by topic
- **Common mistakes highlighted** with how to avoid them
- **Study plans** (4-day intensive, 2-day crash)
- **Exam day strategy** with time management tips

### 2. Two-Page Cheat Sheet (landscape PDF)
- **Ultra-compact** format (8pt font, 3 columns)
- **All critical formulas** in one place
- **Quick reference tables**
- **Worked examples** on page 2
- **Pattern recognition** table
- **Common mistakes** checklist
- Ready to print and bring to exam

## Instructions

When this skill is invoked, follow these steps:

### Step 1: Gather Information

Ask the user (if not provided):
1. **Course name and exam**: "ECO310 Midterm 2" or "MATH 301 Final"
2. **Location of materials**: Where are past exams, lecture slides, etc.?
3. **Scope**: "Content after Midterm 1" or "All semester" or specific topics?
4. **Special requests**: Any particular topics to emphasize?

### Step 2: Analyze Past Exams

1. **Find all past exams** in the materials folder
2. **Extract text** from PDFs using `pdftotext`
3. **Identify topics** that appear in each exam
4. **Calculate frequency**:
   - Appears in 100% of exams → CRITICAL
   - Appears in 70-90% → HIGH PRIORITY
   - Appears in 40-70% → MEDIUM PRIORITY
   - Appears in <40% → OPTIONAL

5. **For each topic**, note:
   - Which exam, which question
   - Type of problem (calculation, proof, conceptual)
   - Difficulty level
   - Common variations

### Step 3: Identify Lecture Coverage

1. **Find lecture slides** for relevant material
2. **Extract key concepts** from each lecture
3. **Map exam questions to lecture topics**
4. **Identify which lectures** are most tested

### Step 4: Create Ultimate Study Guide

Create LaTeX document with this structure:

```latex
\documentclass[10pt,letterpaper]{article}
% Color-coded tcolorbox environments:
% - criticalbox (RED) - Master these first
% - examplebox (GREEN) - Worked examples
% - formulabox (BLUE) - Key formulas
% - warningbox (ORANGE) - Common mistakes
% - strategybox (LIGHTBLUE) - Problem-solving

Sections:
1. Quick Navigation (where to start)
2. Topic 1 (highest frequency)
   - Big idea in plain English
   - Key formulas
   - 3-5 worked examples
   - Common mistakes
   - Quick reference
3. Topic 2 (second highest)
   - Same structure
4. Topic 3...
5. Pattern Recognition Guide
6. Complete Formula Sheet
7. Common Mistakes
8. Exam Strategy
9. Study Plans
```

**Key principles:**
- **Plain English first**, then math
- **Real-world examples** before abstract concepts
- **Step-by-step** worked examples
- **"Why"** before "how"
- **Visual boxes** for critical info
- **Frequency indicators** (appears in X/Y exams)

### Step 5: Create Two-Page Cheat Sheet

Create separate LaTeX document:

```latex
\documentclass[8pt,landscape]{extarticle}
% 3 columns, ultra-compact
% Page 1: All formulas organized by topic
% Page 2: Worked examples + quick reference
```

**Key principles:**
- **Formulas only**, minimal explanation
- **Pattern recognition table**
- **Quick reference** format
- **Scannable** during exam

### Step 6: Compile to PDF

Use the `latex-to-pdf` skill or tectonic:
```bash
cd <directory>
tectonic <filename>.tex
```

Verify PDFs created successfully.

### Step 7: Create Markdown Versions

For accessibility, also create:
- `BEGINNERS_GUIDE_<exam>.md` - Step-by-step explanations
- `COMPREHENSIVE_STUDY_GUIDE_<exam>.md` - Full analysis with tables

## Template Structure

### Ultimate Guide Template Sections:

**Title Page:**
- Course + Exam name
- "Everything You Need to Ace This Exam"
- One guide, all topics, step-by-step
- What's inside (checklist)

**Quick Start (Page 2):**
- Navigation guide
- The Big 3 topics (highest frequency)
- How to use this guide
- 4-day study plan overview

**For Each Topic:**
```
TOPIC NAME (appears in X/Y exams - Z% of exam)

[CRITICALBOX] Why this matters

What is [Topic]?
- Big idea in plain English
- Real-world example

Key Formulas
[FORMULABOX]
- Main formula with explanation
- When to use it

[EXAMPLEBOX] Worked Example 1
- Problem from actual exam
- Step-by-step solution
- Key insight

[EXAMPLEBOX] Worked Example 2...

[WARNINGBOX] Common Mistakes
1. Mistake description + how to avoid

Quick Reference
- All formulas for this topic
- Problem-solving steps
```

**Pattern Recognition:**
```
Table: When you see... → Use this technique
Flowchart: Decision tree for problem types
```

**Formula Sheet:**
- All formulas by topic
- Compact reference

**Common Mistakes:**
- Top 10 mistakes across all topics
- How to avoid each

**Exam Strategy:**
- Time management
- Partial credit tips
- Day-of checklist

**Study Plans:**
- 4-day intensive
- 2-day crash
- Last-minute cram

### Cheat Sheet Template:

**Page 1 (3 columns):**
```
Column 1:
- Topic 1 formulas
- Topic 2 formulas

Column 2:
- Topic 3 formulas
- Topic 4 formulas
- Pattern recognition table

Column 3:
- Topic 5 formulas
- Common mistakes
- Other formulas (backup)
```

**Page 2 (3 columns):**
```
15-20 worked examples
Useful facts
Exam strategy tips
```

## LaTeX Color Scheme

```latex
\definecolor{criticalcolor}{RGB}{220,20,60}  % Crimson red
\definecolor{examplecolor}{RGB}{0,100,0}     % Forest green
\definecolor{warningcolor}{RGB}{255,140,0}   % Orange
\definecolor{headercolor}{RGB}{25,25,112}    % Midnight blue
\definecolor{formulacolor}{RGB}{0,51,102}    % Navy
```

## Quality Checklist

Before delivering, verify:

- [ ] All past exams analyzed
- [ ] Frequency analysis included
- [ ] Each high-frequency topic has 3+ examples
- [ ] Formulas have explanations (not just symbols)
- [ ] Pattern recognition guide complete
- [ ] Both PDFs compile successfully
- [ ] Cheat sheet fits on 2 pages
- [ ] Common mistakes identified
- [ ] Study plans included
- [ ] Beginner-friendly language used

## Example Workflow

**User:** "Create a study guide like the ORF309 one for ECO310"

**Response:**
1. "Great! I'll create an Ultimate Study Guide for ECO310. Let me gather your materials..."
2. Search for past exams in ECO310 folder
3. Extract and analyze all past exams
4. Identify lecture slides
5. Build frequency analysis
6. Create comprehensive LaTeX guide
7. Create 2-page cheat sheet
8. Compile both to PDF
9. Create markdown versions
10. Present all files with clear navigation

## What Makes This Effective

**The ORF309 guide worked because:**

1. **Frequency-based prioritization** - Focus on what actually appears
2. **Beginner explanations** - No assumed knowledge
3. **Real examples** - From actual exams, fully worked
4. **Pattern recognition** - Instant problem identification
5. **Visual organization** - Color-coded boxes
6. **Multiple formats** - Full guide + cheat sheet + markdown
7. **Practical strategies** - How to study, take exam
8. **Realistic plans** - 4-day, 2-day, last-minute options

**Key insight:** Students need to understand WHY techniques work, not just memorize formulas.

## Tips for Different Subjects

**Math/Statistics (like ORF309):**
- Focus on technique recognition
- Step-by-step formula derivations
- Lots of worked examples
- Common calculation errors

**Economics (like ECO310):**
- Intuition before math
- Graphical interpretations
- Real-world examples
- Common conceptual mistakes

**Physics:**
- Concept → Formula → Application
- Unit analysis
- Common physics intuition errors

**Computer Science:**
- Algorithm patterns
- Complexity analysis
- Code examples
- Common bugs

## Files to Create

For each study guide, create:

1. `<COURSE>_<EXAM>_ULTIMATE_Guide.tex` (main guide source)
2. `<COURSE>_<EXAM>_ULTIMATE_Guide.pdf` (compiled guide)
3. `<COURSE>_<EXAM>_CHEATSHEET.tex` (cheat sheet source)
4. `<COURSE>_<EXAM>_CHEATSHEET.pdf` (compiled cheat sheet)
5. `BEGINNERS_GUIDE_<EXAM>.md` (markdown explanations)
6. `COMPREHENSIVE_STUDY_GUIDE_<EXAM>.md` (markdown analysis)

## Success Criteria

The guide is successful if:
- User can start from zero knowledge
- Pattern recognition is instant
- Formulas have context
- Examples are fully worked
- Common mistakes are highlighted
- Cheat sheet is exam-ready
- Study plans are actionable

## Version History
- 1.0.0 (2026-03-31): Initial creation based on ORF309 Midterm 2 success
