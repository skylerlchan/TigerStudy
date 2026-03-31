# Exam Cheat Sheet Generator Prompt

Copy the prompt below and fill in the bracketed fields for your course. Paste it into a new Claude Code session with access to your Canvas downloads folder.

---

## Prompt

```
I have an exam coming up for [COURSE NAME] ([COURSE CODE]) on [DATE]. The exam covers [MATERIAL SCOPE — e.g., "Slides 01-09", "Lectures 1-12", "Chapters 1-5"].

The exam allows [CHEAT SHEET RULES — e.g., "one hand-written double-sided letter-size cheat sheet", "two pages of notes", "one page front only"].

Here are the relevant files:

- Lecture slides/notes: [PATH TO LECTURE FOLDER — e.g., C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\Preferences and Choice\]
- Practice exams: [PATH TO PRACTICE EXAM FOLDER — e.g., C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\Midterm Review Materials\]

Please:

1. **Read all lecture slides** that are in scope for this exam. Extract every definition, formula, theorem, and key result.

2. **Read all practice exams AND their solutions.** For each problem, note which formulas/concepts it tests. Track frequency — how many exams test each concept.

3. **Cross-reference** the lecture content against the practice exam frequency analysis. Identify:
   - Formulas/concepts that appear on EVERY exam (must-know)
   - Formulas that appear on most exams (high priority)
   - Formulas that appear occasionally (medium priority)

4. **Create a LaTeX cheat sheet** at [OUTPUT PATH — e.g., C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\study-guides\midterm1_cheatsheet.tex] that:
   - Fits on [NUMBER] page(s), landscape, 4-column layout with ultra-compact spacing
   - Is organized by topic matching the lecture structure
   - Contains ALL testable formulas, definitions, and theorems
   - **Highlights the most frequently tested formulas** in yellow using \colorbox{yellow!25}
   - Includes a "Problem-Solving Techniques" section with patterns you identified from the practice exams
   - Includes a "Common Exam Traps" section based on mistakes visible in the solutions

5. **Compile to PDF** in an output/ subfolder.

6. **Create a preparation strategy PDF** at [OUTPUT PATH — e.g., ...\study-guides\midterm1_prep_strategy.tex] that includes:
   - A frequency table showing how often each topic appeared across all practice exams, color-coded by priority
   - A study plan for how to use the cheat sheet and practice exams
   - The specific problem patterns to drill (based on your frequency analysis)
   - Common exam traps and mistakes to avoid

The cheat sheet should be my anchor — if I know where every formula is on it and understand when to apply each one, I should be able to handle any problem they throw at me.
```

---

## Notes

- Run `python download_course.py --all` first to make sure all course materials are synced.
- The more practice exams available, the better the frequency analysis. 4+ exams gives strong signal.
- For courses without practice exams, the prompt still works — it just won't have frequency-based highlighting. You can remove steps 2-3 and the highlighting part.
- If the course is more conceptual than formula-heavy (e.g., ASA201), swap "formulas" for "key terms, arguments, and frameworks" throughout.
