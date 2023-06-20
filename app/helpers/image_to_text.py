from helpers.refine_data import remove_empty_lines, string_replacement, normalize_notes
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
import re

def process_line(line):
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line using regular expressions
    pattern = r'\s+'  # Matches two or more consecutive spaces
    components = re.split(pattern, line)

    # Extract the individual data points
    if len(components) >= 3:
        position = components[0]
        player_name = ' '.join(components[1:-1])  # Join all components except first and last
        note = components[-1]
        # Split the player name and note further if they have a space or comma in between
        player_name_parts = re.split(r'\s|,', player_name)
        player_name_parts = [part for part in player_name_parts if part]  # Remove empty parts
        player_name = ' '.join(player_name_parts)
        return position, player_name, note
    else:
        return None, None, None  # Line does not contain all three data points



def extract_image_to_text(image_path, file_path):
    with open(file_path, mode='w') as file:
        custom_config = r'--psm 6 --oem 1'
        text = pytesseract.image_to_string(
            image_path,
            config=custom_config,
        )
        file.write(text)

    string_replacement(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            position, player_name, note = process_line(line)
            print("Position:", position)
            print("Player Name:", player_name)
            print("Note:", note)
    # normalize_notes(file_path)
    # remove_empty_lines(file_path)