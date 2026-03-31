# Ultimate Study Guide Generator - Reusable Prompt

## How to Use This

Copy and paste this prompt to Claude whenever you need a study guide for any class:

---

## THE PROMPT:

```
Create an Ultimate Study Guide for my [COURSE NAME] [EXAM TYPE] using the same format and approach as the ORF309 Midterm 2 guide you created.

**Course:** [e.g., MATH 340, CHEM 201, etc.]
**Exam:** [e.g., Midterm 2, Final Exam, etc.]
**Materials location:** [path to your course folder]
**Scope:** [e.g., "Content after Midterm 1", "Entire semester", "Chapters 5-10"]

**What to include:**
1. Analyze all past exams in the materials folder
2. Calculate topic frequency (what appears most often)
3. Identify lecture slides that correspond to exam content
4. Create comprehensive guide with:
   - Beginner-friendly explanations (real-world examples first)
   - Color-coded priority boxes (RED=critical, GREEN=examples, ORANGE=warnings)
   - 15+ fully worked examples from actual past exams
   - Pattern recognition guide (when you see X → use technique Y)
   - Complete formula sheets organized by topic
   - Common mistakes highlighted
   - Study plans (4-day intensive + 2-day crash)
   - Exam day strategy

5. Create 2-page cheat sheet:
   - Landscape format, 3 columns, ultra-compact
   - All formulas on page 1
   - Worked examples on page 2
   - Ready to print and bring to exam

6. Compile everything to PDF

**Format:** Follow the exact LaTeX structure from ORF309:
- Use tcolorbox for colored boxes
- criticalbox (red) for must-know content
- examplebox (green) for worked examples
- formulabox (blue) for key formulas
- warningbox (orange) for common mistakes
- Title page with overview
- Table of contents
- Quick navigation section
- Priority-ordered topics (highest frequency first)

**Special requests:** [any specific topics to emphasize or questions you have]
```

---

## Customization Tips

**For Math/Statistics Courses:**
- Emphasize technique recognition
- Include formula derivations
- Lots of calculation examples
- Common arithmetic errors

**For Economics Courses:**
- Start with intuition, then math
- Include graphs and visual explanations
- Real-world examples
- Conceptual vs computational problems

**For Science Courses:**
- Concept → Formula → Application flow
- Include unit analysis
- Lab-related problems
- Common physics/chemistry intuition errors

**For Computer Science:**
- Algorithm pattern recognition
- Complexity analysis
- Code examples with explanations
- Common bugs and edge cases

---

## Example Usage

### Example 1: Math Course
```
Create an Ultimate Study Guide for my MATH 340 Linear Algebra Final Exam using the same format as the ORF309 guide.

**Course:** MATH 340
**Exam:** Final Exam
**Materials location:** ~/Desktop/MATH340/materials/
**Scope:** Entire semester (Chapters 1-7)

Focus on: eigenvalues, diagonalization, vector spaces, linear transformations
```

### Example 2: Economics Course
```
Create an Ultimate Study Guide for my ECO 362 Financial Markets Midterm 2 using the ORF309 format.

**Course:** ECO 362
**Exam:** Midterm 2
**Materials location:** ~/Desktop/ECO362/
**Scope:** Content after Midterm 1 (portfolio theory, CAPM, options)
```

### Example 3: Computer Science
```
Create an Ultimate Study Guide for my COS 226 Algorithms Final using the ORF309 format.

**Course:** COS 226
**Exam:** Final Exam
**Materials location:** ~/Courses/COS226/
**Scope:** Entire semester

Focus on: sorting algorithms, graph algorithms, dynamic programming, complexity analysis
```

---

## What You'll Receive

After Claude processes your request, you'll get:

### 1. Ultimate Study Guide PDF (60+ pages)
- **Section 1:** Quick navigation
- **Section 2-N:** Topics ordered by exam frequency
  - Plain English explanation
  - Real-world examples
  - Key formulas in blue boxes
  - 3-5 worked examples in green boxes
  - Common mistakes in orange boxes
  - Quick reference
- **Pattern Recognition:** Table showing problem type → technique
- **Complete Formula Sheet:** All formulas by topic
- **Common Mistakes:** Top 10 across all topics
- **Exam Strategy:** Time management, partial credit tips
- **Study Plans:** 4-day and 2-day schedules

### 2. Two-Page Cheat Sheet PDF
- **Page 1:** All formulas organized by topic (3 columns)
  - Pattern recognition table
  - Common mistakes checklist
  - Other distributions/concepts (backup)
- **Page 2:** 15-20 worked examples
  - Useful facts
  - Exam strategy tips

### 3. Markdown Versions
- `BEGINNERS_GUIDE_<exam>.md` - Step-by-step explanations
- `COMPREHENSIVE_STUDY_GUIDE_<exam>.md` - Full frequency analysis

---

## Success Factors

What made the ORF309 guide so effective:

1. **Frequency-based prioritization** - Focus on what actually appears
2. **Beginner explanations** - Build understanding from scratch
3. **Real examples** - Every example from actual past exams
4. **Pattern recognition** - Instantly know which technique to use
5. **Visual organization** - Color-coded for easy scanning
6. **Multiple formats** - Full guide + cheat sheet + markdown
7. **Practical strategies** - How to study efficiently + take exam
8. **Realistic schedules** - Multiple study plans for different time constraints

---

## Tips for Best Results

1. **Organize your materials first:**
   ```
   Course/
   ├── Past_Exams/
   ├── Lecture_Slides/
   ├── Problem_Sets/
   └── Notes/
   ```

2. **Have at least 3 past exams** for good frequency analysis

3. **Include solutions** if available - helps with worked examples

4. **Be specific about scope** - "After Midterm 1" vs "Entire semester"

5. **Mention any weak areas** - Claude can emphasize those topics

---

## Advanced: Creating a Custom Skill

If you use this frequently, you can create a shortcut:

**In your CLAUDE.md file, add:**
```markdown
# study-guide command
When I say "/study-guide [COURSE] [EXAM]", use the ultimate-study-guide-generator skill to create a comprehensive study guide for that course and exam. Follow the ORF309 format exactly.
```

Then you can just type:
```
/study-guide ECO310 Final
```

---

## Troubleshooting

**Q: What if I don't have past exams?**
A: Claude can still create a guide from lecture slides and problem sets, but mention this upfront so it focuses on lecture content.

**Q: Can I request specific formatting changes?**
A: Yes! Add to "Special requests" section. E.g., "Make cheat sheet 1 page instead of 2" or "Include more graphs"

**Q: What if my course uses a different structure?**
A: Describe your course structure in the prompt. E.g., "This course is project-based, focus on design patterns and best practices"

**Q: Can I get just the cheat sheet?**
A: Yes, specify: "Create only a 2-page cheat sheet (skip the full guide)"

---

## File Locations

After creation, your files will be in:
```
<Course_Folder>/materials/
├── <COURSE>_<EXAM>_ULTIMATE_Guide.pdf
├── <COURSE>_<EXAM>_CHEATSHEET.pdf
├── BEGINNERS_GUIDE_<EXAM>.md
└── COMPREHENSIVE_STUDY_GUIDE_<EXAM>.md
```

---

## Remember

The key to these guides is:
- **Understanding over memorization**
- **Patterns over individual problems**
- **Practice with real examples**
- **Strategic preparation (not cramming everything)**

Good luck with your exams! 🚀
