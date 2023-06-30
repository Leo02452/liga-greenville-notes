import unicodedata, shutil, re
from app.update_active_players import active_players_list

def remove_accents_and_letter_through(player):
    normalized_player = unicodedata.normalize('NFD', player)
    stripped_player = ''.join(c for c in normalized_player if unicodedata.category(c) != 'Mn')
    first_through_correction = stripped_player.replace('ø', 'o')
    second_through_correction = first_through_correction.replace('Ø', 'O')
    return second_through_correction

def abbreviate_first_name(player):
    fullname = player.split(" ")
    if (3 > len(fullname) > 1):
        first_name, last_name = fullname
        first_letter = first_name[0]
        return f"{first_letter}. {last_name}"
    else:
        return " ".join(fullname)

def replace_players(players_list, txt_player):
    for player in players_list:
        base_player = remove_accents_and_letter_through(player)
        abbreviated_base_player = abbreviate_first_name(base_player)
        txt_player_without_accent = remove_accents_and_letter_through(txt_player)
        if (
            (txt_player_without_accent == abbreviated_base_player or
            abbreviated_base_player in txt_player_without_accent) and
            txt_player_without_accent != player
        ):
            return player
        elif txt_player_without_accent == player:
            return player

def remove_empty_lines(file_path):
    with open(file_path, 'r') as input_file, open('temp_file.txt', 'w') as temp_file:
        lines = input_file.readlines()
        for line in lines:
            if line.strip():
                temp_file.write(line)

    shutil.move('temp_file.txt', file_path)

def normalize_position(position):
    uppercase_position = position.upper()
    return uppercase_position
    
def normalize_player_name(player_name):
    replacements = {
        'ii': 'u',
        '0.': 'O.',
        'fi': 'n',
        'ié': 'ić',
        'T. AlexanderAr...': 'T. Alexander-Arnold',
        'A. Zambo Anguis...': 'A. Zambo Anguissa',
        'D. Nujiez': 'D. Nuñez',
        'R. Ledo': 'R. Leão',
        '6. Kobel': 'G. Kobel',
        'Kessić': 'Kessié',
        'Taglianco': 'Tagliafico'
    }

    grouped_replacements = {
        '': ['@', '*', '=', '>', '»', '+', '~', '®', '©', '-', '_', '—', '&', '%'],
        'I.': ['l.', '|.']
    }

    for replacement_key, replacement_values in grouped_replacements.items():
        for key in replacement_values:
            player_name = player_name.replace(key, replacement_key)
    for key, value in replacements.items():
        player_name = player_name.replace(key, value)
    player_name = player_name.strip()
    player_name = re.sub(r'([a-zA-Z])\.([a-zA-Z])', r'\1. \2', player_name)
    player_name = replace_players(active_players_list, player_name)
    return player_name
