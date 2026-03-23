import pdfplumber
import sys

# Set stdout to UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\Midterm Review Materials\midtemr review 26.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        page_text = page.extract_text()
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print(f"{'='*60}")
        print(page_text)
