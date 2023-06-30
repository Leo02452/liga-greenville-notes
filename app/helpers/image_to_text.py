import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def extract_image_to_text(image_path, file_path):
    with open(file_path, mode='w') as file:
        custom_config = r'--psm 6 --oem 1'
        text = pytesseract.image_to_string(
            image_path,
            config=custom_config,
        )
        file.write(text)
