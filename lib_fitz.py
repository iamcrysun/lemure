import fitz  # PyMuPDF

# Функция для извлечения текста с учетом координат блоков
def extract_text_with_structure_fitz(pdf_path):
    doc = fitz.open(pdf_path)
    structured_text = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")  # Извлекаем текст в блоках

        page_text = ""
        for block in blocks:
            block_text = block[4]  # Текст блока находится на 4-м месте
            page_text += block_text.strip() + " "  # Объединяем блоки в один текст страницы

        structured_text.append(page_text.strip())

    return '\n'.join(structured_text)

# Пример использования
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
extracted_text_fitz = extract_text_with_structure_fitz(pdf_path)

# Сохранение результата в файл
with open('fitz_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text_fitz)

print(extracted_text_fitz)
