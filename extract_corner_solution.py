import pdfplumber
import sys

# Set stdout to UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\study-guides\output\q3b_corner_solution.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        page_text = page.extract_text()
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print(f"{'='*60}")
        print(page_text)
