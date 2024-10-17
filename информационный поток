import fitz  # это pymupdf
import re
from multi_column import column_boxes

def extract_paragraphs_from_pdf(pdf_path):
    """
    Извлекает текст из PDF файла и возвращает список абзацев.

    :param pdf_path: Путь к PDF файлу.
    :return: Список абзацев, где каждый абзац представлен как строка.
    """
    # Открытие PDF документа
    doc = fitz.open(pdf_path)

    # Переменная для хранения всего извлеченного текста
    all_extracted_text = ""

    # Обработка каждой страницы
    for page in doc:
        # Получение границ текстовых блоков
        bboxes = column_boxes(page, footer_margin=50, no_image_text=True)

        # Извлечение текста из каждого блока и добавление в строку
        for rect in bboxes:
            # Извлекаем текст для текущего прямоугольника
            extracted_text = page.get_text(clip=rect, sort=True)
            # Добавляем текст в общую строку
            all_extracted_text += extracted_text

    # Используем регулярное выражение для объединения строк, которые не начинаются с красной строки
    processed_text = re.sub(r'(?<!\n)(\n)([^\s])', r' \2', all_extracted_text)

    # Удаляем переходы на новую строку, если строка не заканчивается точкой
    #processed_text = re.sub(r'([^\.\n])\n', r'\1 ', processed_text)

    # Удаляем пустые строки
    #processed_text = "\n".join([line for line in processed_text.splitlines() if line.strip()])

    # Разделяем текст на абзацы
    paragraphs = [paragraph.strip() for paragraph in processed_text.split("\n\n") if paragraph.strip()]

    return paragraphs

# Пример использования функции
pdf_path = "Coal_Trader_16_Sep_2024.pdf"
paragraphs = extract_paragraphs_from_pdf(pdf_path)
