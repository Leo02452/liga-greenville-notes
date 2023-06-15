from refine_data import remove_empty_lines, string_replacement, normalize_notes
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def extract_image_to_text(image_path, file_path):
    with open(file_path, mode='w') as file:
        text = pytesseract.image_to_string(image_path)
        file.write(text)

    string_replacement(file_path)
    normalize_notes(file_path)
    remove_empty_lines(file_path)