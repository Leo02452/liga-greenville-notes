import os
import shutil
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

def remove_empty_lines(file_path):
    with open(file_path, 'r') as input_file, open('temp_file.txt', 'w') as temp_file:
        lines = input_file.readlines()

        for line in lines:
            if line.strip():
                temp_file.write(line)

    shutil.move('temp_file.txt', file_path)

def normalize_notes(file_path):
    with open(file_path, 'r') as input_file, open('temp_file.txt', 'w') as temp_file:
        lines = input_file.readlines()

        for line in lines:
            line_list = line.strip().split(',')
            line_is_digit = line_list[0].isdigit()
            one_item = len(line_list) == 1
            if (one_item and line_is_digit):
                if (line_list[0] == '1' or line_list[0][0] == '1'):
                    new_line = line.replace('1', '7,')
                    temp_file.write(new_line)
                else:
                    temp_file.write(','.join([number for number in line_list[0]]) + '\n')
            else:
                temp_file.write(line)
    shutil.move('temp_file.txt', file_path)
