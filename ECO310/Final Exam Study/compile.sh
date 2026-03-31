#!/bin/bash

# ECO310 Final Exam Study Materials Compilation Script
# Run this script to compile both the Ultimate Study Guide and Cheat Sheet

echo "Compiling ECO310 Final Exam Study Materials..."
echo ""

# Navigate to directory
cd "$(dirname "$0")"

# Compile Ultimate Study Guide (run twice for TOC)
echo "📚 Compiling Ultimate Study Guide..."
pdflatex -interaction=nonstopmode ECO310_ULTIMATE_Final_Guide.tex > compile_guide.log 2>&1
pdflatex -interaction=nonstopmode ECO310_ULTIMATE_Final_Guide.tex >> compile_guide.log 2>&1

if [ -f "ECO310_ULTIMATE_Final_Guide.pdf" ]; then
    echo "✅ Ultimate Study Guide compiled successfully!"
else
    echo "❌ Error compiling Ultimate Study Guide. Check compile_guide.log"
fi

# Compile Cheat Sheet
echo "📝 Compiling Cheat Sheet..."
pdflatex -interaction=nonstopmode ECO310_Final_CheatSheet.tex > compile_cheatsheet.log 2>&1

if [ -f "ECO310_Final_CheatSheet.pdf" ]; then
    echo "✅ Cheat Sheet compiled successfully!"
else
    echo "❌ Error compiling Cheat Sheet. Check compile_cheatsheet.log"
fi

# Clean up auxiliary files
echo ""
echo "🧹 Cleaning up auxiliary files..."
rm -f *.aux *.log *.toc *.out

echo ""
echo "✨ Done! Your study materials are ready:"
echo "   - ECO310_ULTIMATE_Final_Guide.pdf (comprehensive guide)"
echo "   - ECO310_Final_CheatSheet.pdf (2-page reference)"
