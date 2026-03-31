import pdfplumber
import sys

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\skyle\OneDrive\Desktop\Canvas\downloads\ECO310\Choice Under Uncertainty\intermediate_lec7 and 8 math26.pdf'

with pdfplumber.open(pdf_path) as pdf:
    print(f'Total pages: {len(pdf.pages)}\n')

    for i, page in enumerate(pdf.pages):
        print(f'\n{"="*60}')
        print(f'PAGE {i+1}')
        print("="*60)
        text = page.extract_text()
        if text:
            print(text)
        else:
            print("[No text extracted from this page]")
