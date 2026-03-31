import pdfplumber
import sys

# Set stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\skyle\.collab-workspace\Company Workspace\ws_default\src\Skyler's HW\Canvas\downloads\ORF309\Midterm 1 Practice\output\q1c_detailed.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, 1):
        print(f'--- Page {i} ---')
        print(page.extract_text())
        print()
