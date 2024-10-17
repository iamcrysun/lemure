import pypdfium2 as pdfium

def extract_text_pypdfium2(pdf_path):
    pdf = pdfium.PdfDocument(pdf_path)
    text = ''
    for i in range(len(pdf)):
        page = pdf[i]
        text += page.get_textpage().get_text_range()
    pdf.close()
    return text

pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
print(extract_text_pypdfium2(pdf_path))