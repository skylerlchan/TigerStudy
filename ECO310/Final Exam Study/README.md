# ECO310 Final Exam Study Materials

**Created:** March 31, 2026
**Content Coverage:** Post-Midterm Material (Lectures 7-14)
- Choice Under Uncertainty (Lectures 7-9)
- Producer Theory & Markets (Lectures 10-14)

## 📚 What's Included

### 1. **ECO310_ULTIMATE_Final_Guide.tex** (Ultimate Study Guide)
A comprehensive 40+ page study guide featuring:
- ✅ Beginner-friendly explanations with real-world examples
- ✅ 20+ fully worked examples
- ✅ All formulas you need (color-coded by importance)
- ✅ Pattern recognition guide (when to use what technique)
- ✅ Common mistakes and how to avoid them
- ✅ Step-by-step problem-solving strategies

**Sections:**
1. Choice Under Uncertainty (Expected Utility, Risk Aversion, Insurance, Portfolio Choice)
2. Producer Theory (Production Functions, Cost Functions)
3. Perfect Competition vs. Monopoly
4. General Equilibrium and Welfare
5. Pattern Recognition Guide
6. Complete Formula Sheet
7. Common Mistakes to Avoid

### 2. **ECO310_Final_CheatSheet.tex** (2-Page Cheat Sheet)
A condensed 2-page reference guide with:
- All key formulas for uncertainty, costs, competition, and monopoly
- Quick lookup table for problem types
- Common mistakes checklist
- Perfect for last-minute review or bringing to study sessions

## 🔨 How to Compile

### Option 1: Using the Compilation Script (Easiest)
```bash
cd "ECO310/Final Exam Study"
./compile.sh
```

### Option 2: Manual Compilation
```bash
# Compile Ultimate Guide (run twice for table of contents)
pdflatex ECO310_ULTIMATE_Final_Guide.tex
pdflatex ECO310_ULTIMATE_Final_Guide.tex

# Compile Cheat Sheet
pdflatex ECO310_Final_CheatSheet.tex
```

### Prerequisites
You need LaTeX installed on your system:
- **Mac:** Install [MacTeX](https://www.tug.org/mactex/) (3.5GB)
- **Windows:** Install [MiKTeX](https://miktex.org/)
- **Linux:** `sudo apt-get install texlive-full`

### Quick Install (Mac)
```bash
# Install using Homebrew (if you have it)
brew install --cask mactex

# Or download from: https://www.tug.org/mactex/
```

## 📖 How to Use This Guide

### Study Plan (3-4 Days)

**Day 1:** Read Section 1 (Uncertainty)
- Work through all examples
- Try 3 practice problems from old exams

**Day 2:** Read Sections 2-3 (Firms & Markets)
- Work through all examples
- Try 3 more practice problems

**Day 3:** Read Section 4 (General Equilibrium)
- Review all sections
- Do a full practice exam

**Day 4:** Formula review + Practice
- Review Section 6 (formulas)
- Do another practice exam
- Create your own cheat sheet

### Quick Reference Options

**First Time Learning?** → Read Ultimate Guide in order (Sections 1-4)

**Need Quick Review?** → Go straight to Formula Sheet (Section 6)

**Doing Practice Problems?** → Use Pattern Recognition Guide (Section 5)

**Last-Minute Cramming?** → Focus on Sections 1, 3, and 6 + Cheat Sheet

## 🎯 Key Topics to Master

### Must-Know Concepts (80% of Exam)

**Choice Under Uncertainty:**
1. Expected Utility vs. Expected Value
2. Certainty Equivalent calculation
3. Risk Premium
4. Risk aversion and concavity
5. Insurance problems
6. Portfolio optimization

**Producer Theory:**
1. Inverting production functions to get cost functions
2. Marginal cost calculation
3. Average cost relationships

**Market Structures:**
1. Perfect Competition: P = MC
2. Monopoly: MR = MC (and MR formula for linear demand)
3. Long-run equilibrium conditions

## ⚠️ Common Mistakes to Avoid

1. ❌ Confusing EV and EU (they're different!)
2. ❌ Forgetting to invert production function before finding cost
3. ❌ Using P = MC for monopoly (should be MR = MC)
4. ❌ Wrong MR formula (for P = a - bQ, MR = a - 2bQ, not a - bQ!)
5. ❌ Mixing up demand Q^D(P) and inverse demand P^D(Q)
6. ❌ Not checking for corner solutions in portfolio problems

## 📊 The Big 5 Master List

Master these 5 things and you'll ace the exam:

1. **Expected Utility vs. Expected Value** - Know when to use each
2. **Certainty Equivalent** - Solve u(CE) = EU(L)
3. **MR for Linear Demand** - Same intercept, twice the slope
4. **P = MC (competition) vs. MR = MC (monopoly)** - Don't mix these up!
5. **Inverting Production Functions** - Must do this before finding costs

## 📁 File Structure

```
ECO310/Final Exam Study/
├── ECO310_ULTIMATE_Final_Guide.tex    (Ultimate guide source)
├── ECO310_ULTIMATE_Final_Guide.pdf    (Compiled guide - you create this)
├── ECO310_Final_CheatSheet.tex         (Cheat sheet source)
├── ECO310_Final_CheatSheet.pdf         (Compiled cheat sheet - you create this)
├── compile.sh                          (Compilation script)
└── README.md                           (This file)
```

## 💡 Tips for Success

1. **Work through every example** - Don't just read, actually solve them
2. **Make your own cheat sheet** - The process of making it helps you learn
3. **Focus on patterns** - Many problems follow the same structure
4. **Do practice exams under time pressure** - Simulate real exam conditions
5. **Understand WHY, not just HOW** - Conceptual understanding beats memorization

## 🆘 Troubleshooting

**"I don't have LaTeX installed"**
- See Prerequisites section above for installation instructions
- Or use [Overleaf](https://www.overleaf.com/) (free online LaTeX editor)

**"Compilation fails"**
- Make sure all required LaTeX packages are installed
- Check the .log files for specific errors
- Try compiling on Overleaf if local compilation fails

**"I can't open the PDF"**
- Make sure you've compiled the .tex files first
- PDFs are not included - you must generate them from the .tex source

## 📧 Questions?

If you find errors or have suggestions for improvements, feel free to update the source .tex files!

---

**Good luck on your final exam! 🎓**

Remember: Master the formulas, practice the problems, and trust your preparation.
