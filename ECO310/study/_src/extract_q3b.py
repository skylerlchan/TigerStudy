import pdfplumber
import sys

pdf_path = r"C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\Midterm Review Materials\310 midterm spring solutions 25.pdf"

with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for i, page in enumerate(pdf.pages):
        page_text = page.extract_text()
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print(f"{'='*60}")
        print(page_text)
        full_text += f"\n--- PAGE {i+1} ---\n" + page_text
