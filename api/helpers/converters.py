import csv
import os

import pytesseract

from io import BytesIO
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def extract_image_to_text(image_path):
    custom_config = r'--psm 6 --oem 1'
    text = pytesseract.image_to_string(
        Image.open(BytesIO(image_path)),
        config=custom_config,
    )
    return text

def extract_text_to_list(file_content):
    extracted_data = []
    lines = file_content.decode('utf-8').split('\n')
    for line in lines:
        position, player_name, note = line.split(',')
        extracted_data.append({
            "position": position,
            "player_name": player_name,
            "note": note,
        })
    return extracted_data

def extract_list_to_csv(players_list, game_info, season, day):
    os.makedirs(f'api/static/{season}/{day}/datas', exist_ok=True)
    output_file = f'api/static/{season}/{day}/datas/data.csv'
    with open(output_file, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        for player in players_list:
            writer.writerow([
                player["position"],
                player["name"],
                player["note"],
                game_info['team'],
                game_info['opponent'],
                game_info['competition']
            ])