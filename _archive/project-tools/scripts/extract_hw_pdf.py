import pdfplumber

pdf_path = r"C:\Users\skyle\OneDrive\Desktop\Current Project\Canvas\downloads\ECO310\Homework\intermediate_mathps2_26.pdf"

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf.pages)}\n")
    for i, page in enumerate(pdf.pages):
        print(f"\n{'='*80}")
        print(f"PAGE {i+1}")
        print(f"{'='*80}\n")
        text = page.extract_text()
        if text:
            print(text)
