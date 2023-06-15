import os
import re

def string_replacement(file_path):
    replacements = {
        'MEL': 'MEI',
        'McD': 'MCD',
        'VoL': 'VOL',
        'Lp': 'LD',
        'ii': 'u',
        '0.': 'O.',
        'fi': 'n',
        'ié': 'ić',
        'T. Alexander-Ar...': 'T. Alexander-Arnold',
        'A. Zambo Anguis...': 'A. Zambo Anguissa',
        'D. Nujiez': 'D. Nuñez',
        'R. Ledo': 'R. Leão',
        '6. Kobel': 'G. Kobel',
        'Kessić': 'Kessié',
        'Taglianco': 'Tagliafico'
    }

    grouped_replacements = {
        '': ['', '@', '*', '=', '>', '+', '~', '®', '©', '-', '_', '—'],
        'ZGD': ['z6D', 'Z6D', '76D', 'zG6D', 'ZG6D'],
        'I.': ['l.', '|.']
    }

    temp_file_path = 'temp_file.txt'

    with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
        for line in file:
            for replacement_key, replacement_values in grouped_replacements.items():
                for key in replacement_values:
                    line = line.replace(key, replacement_key)
            for key, value in replacements.items():
                line = line.replace(key, value)
            line = line.strip()
            line = re.sub(r'([a-zA-Z])\.([a-zA-Z])', r'\1. \2', line)
            temp_file.write(line + '\n')

    os.remove(file_path)
    os.rename(temp_file_path, file_path)
