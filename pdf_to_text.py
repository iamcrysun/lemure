import pdfplumber

# Функция для извлечения текста из колонок
def extract_text_from_columns(pdf_path):
    text = ''

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            width = page.width
            height = page.height

            # Задаем две области для колонок (левая и правая)
            left_bbox = (0, 0, width / 2, height)  # Левая колонка
            right_bbox = (width / 2, 0, width, height)  # Правая колонка

            # Извлекаем текст из каждой колонки по очереди
            left_text = page.within_bbox(left_bbox).extract_text()
            right_text = page.within_bbox(right_bbox).extract_text()

            # Добавляем текст с каждой страницы
            if left_text:
                text += left_text + '\n'
            if right_text:
                text += right_text + '\n'

    return text

# Пример использования функции
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
extracted_text = extract_text_from_columns(pdf_path)

# Сохраняем текст в файл
with open('output_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(extracted_text)
