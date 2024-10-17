from pdf2docx import Converter

# Функция для конвертации PDF в DOCX
def convert_pdf_to_docx(pdf_path, docx_path):
    # Создаем объект конвертера
    cv = Converter(pdf_path)
    # Конвертируем PDF в DOCX
    cv.convert(docx_path, start=0, end=None)  # start и end можно указать для конвертации определенных страниц
    cv.close()

# Пример использования
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
docx_path = 'output_document.docx'

# Конвертация
convert_pdf_to_docx(pdf_path, docx_path)
print(f"Конвертация завершена: {docx_path}")