import pdfplumber

pdf_path = r"C:\Users\skyle\OneDrive\Desktop\Canvas\downloads\ORF309\Course Materials\ORF309.pdf"
output_path = r"C:\Users\skyle\OneDrive\Desktop\Canvas\textbook_lln_pages.txt"

# Read specific pages about LLN
lln_pages = [5, 6, 17, 32, 38, 43, 53, 55, 56, 57, 59, 60, 61, 62]

with pdfplumber.open(pdf_path) as pdf:
    with open(output_path, 'w', encoding='utf-8') as f:
        for page_num in lln_pages:
            if page_num <= len(pdf.pages):
                page = pdf.pages[page_num - 1]
                text = page.extract_text()
                separator = '=' * 80
                f.write(f"\n{separator}\n")
                f.write(f"PAGE {page_num}\n")
                f.write(f"{separator}\n")
                f.write(text)
                f.write("\n")

print(f"Extracted LLN pages to {output_path}")
