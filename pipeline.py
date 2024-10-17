from pdf2docx import Converter
import docx

# Функция для конвертации PDF в DOCX
def convert_pdf_to_docx(pdf_path, docx_path):
    # Создаем объект конвертера
    cv = Converter(pdf_path)
    # Конвертируем PDF в DOCX
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print(f"Конвертация завершена: {docx_path}")

# Функция для извлечения текста и таблиц из DOCX
def extract_text_and_tables_from_docx(docx_path):
    # Открываем документ
    doc = docx.Document(docx_path)

    full_text = []

    # Проходим по каждому элементу в теле документа
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Если элемент - параграф
            para = docx.text.paragraph.Paragraph(element, doc)
            full_text.append(para.text)
        elif element.tag.endswith('tbl'):  # Если элемент - таблица
            table = docx.table.Table(element, doc)
            for row in table.rows:
                row_data = [cell.text for cell in row.cells]
                # Добавляем строку таблицы в виде строки, разделенной символами |
                full_text.append(' | '.join(row_data))

    # Объединяем все элементы с новой строкой между ними
    return '\n'.join(full_text)

def clean_text(text):
    # Разделяем текст на строки
    lines = text.splitlines()

    # Убираем пустые строки и строки, содержащие только пробелы
    clean_lines = [line.strip() for line in lines if line.strip()]

    # Объединяем строки, добавляя один пробел между строками
    clean_text = '\n'.join(clean_lines)

    return clean_text

# Функция для сохранения текста в файл
def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Текст успешно сохранен в {output_file}")

# Основная функция
def pdf_to_txt_via_docx(pdf_path, docx_path, txt_path):
    # Шаг 1: Конвертация PDF в DOCX
    convert_pdf_to_docx(pdf_path, docx_path)

    # Шаг 2: Извлечение текста и таблиц из DOCX
    document_text = extract_text_and_tables_from_docx(docx_path)

    # Шаг 3: Очистка текста (убираем лишние пробелы и разрывы)
    cleaned_text = clean_text(document_text)

    # Шаг 4: Сохранение очищенного текста в TXT файл
    save_text_to_file(cleaned_text, txt_path)


# Пример использования
pdf_path = 'Coal_Trader_16_Sep_2024.pdf'  # Укажите путь к вашему PDF файлу
docx_path = 'output_document.docx'        # Укажите путь для временного DOCX файла
txt_path = 'output_text.txt'              # Укажите путь для финального TXT файла

# Конвертация PDF в TXT через DOCX
pdf_to_txt_via_docx(pdf_path, docx_path, txt_path)
