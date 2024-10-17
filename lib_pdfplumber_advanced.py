import pdfplumber
from collections import defaultdict


def extract_text_with_columns_and_tables(pdf_path):
    full_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = []

            # Извлекаем таблицы (если они есть)
            if page.extract_tables():
                for table in page.extract_tables():
                    # Преобразуем таблицу в текст (разделяя ячейки табуляцией)
                    for row in table:
                        row_text = '\t'.join([cell if cell else '' for cell in row])
                        page_text.append(row_text)

            # Извлекаем символы (для анализа шрифтов и заголовков)
            chars = page.chars

            # Кластеризация текста по X-координатам (определение колонок)
            column_threshold = 50  # Порог для определения новой колонки (можно корректировать)
            columns = defaultdict(list)

            for char in chars:
                x0 = char['x0']
                size = char['size']  # Размер шрифта
                char_text = char['text']

                # Определяем, к какой колонке относится символ
                added_to_column = False
                for column_x in columns:
                    if abs(x0 - column_x) < column_threshold:
                        columns[column_x].append(char)
                        added_to_column = True
                        break
                if not added_to_column:
                    columns[x0].append(char)

            # Сортируем символы в каждой колонке по Y-координатам (чтобы сохранить порядок строк)
            sorted_columns = {}
            for column_x, chars in columns.items():
                sorted_columns[column_x] = sorted(chars, key=lambda c: c['top'])

            # Определение заголовков (например, по размеру шрифта)
            headers = []
            for column_x in sorted(sorted_columns):
                for char in sorted_columns[column_x]:
                    if char['size'] > 14:
                        headers.append(char['text'].strip())

            # Объединяем текст из колонок
            for column_x in sorted(sorted_columns):  # Обходим колонки по возрастанию X
                column_text = ''.join([char['text'] for char in sorted_columns[column_x]])
                page_text.append(column_text)

            # Добавляем текст со всех колонок страницы
            full_text.append('\n'.join(page_text))

    return '\n'.join(full_text)


# Пример использования
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'
extracted_text = extract_text_with_columns_and_tables(pdf_path)

# Сохранение результата в файл
with open('output_text_with_tables_and_headers.txt', 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(extracted_text)
