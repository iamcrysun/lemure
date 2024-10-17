from pdfminer.high_level import extract_text_to_fp
from io import StringIO


# Функция для извлечения текста с pdfminer
def extract_text_pdfminer(pdf_path):
    output_string = StringIO()
    with open(pdf_path, 'rb') as pdf_file:
        extract_text_to_fp(pdf_file, output_string)

    return output_string.getvalue()


# Пример использования
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
extracted_text_pdfminer = extract_text_pdfminer(pdf_path)

# Сохранение результата в файл
with open('pdfminer_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text_pdfminer)

print(extracted_text_pdfminer)
