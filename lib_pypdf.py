import pypdf

def extract_text_pypdf(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
print(extract_text_pypdf(pdf_path))