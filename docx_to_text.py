import docx


def extract_text_and_tables_from_docx(docx_path):
    # Открываем документ
    doc = docx.Document(docx_path)

    full_text = []

    for element in doc.element.body:
        if element.tag.endswith('p'):  # Проверяем, если это параграф (p)
            para = docx.text.paragraph.Paragraph(element, doc)
            full_text.append(para.text)
        elif element.tag.endswith('tbl'):  # Проверяем, если это таблица (tbl)
            table = docx.table.Table(element, doc)
            for row in table.rows:
                row_data = [cell.text for cell in row.cells]
                # Добавляем строку таблицы в виде строки, разделенной символами |
                full_text.append(' | '.join(row_data))

    # Объединяем все элементы с новой строкой между ними
    return '\n'.join(full_text)


def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)


# Использование скрипта
input_docx = 'output_document.docx'  # путь к вашему файлу
output_txt = 'output_text.txt'  # файл для сохранения текста

# Извлечение текста и таблиц
document_text = extract_text_and_tables_from_docx(input_docx)

# Сохранение в файл
save_text_to_file(document_text, output_txt)

print(f"Текст и таблицы успешно извлечены и сохранены в {output_txt}")
