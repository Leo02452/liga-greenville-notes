import unicodedata, shutil, re
from .google_spreadsheets.get_active_players import active_players_list

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
    with open('api/helpers/unidentified_players.txt', mode='a') as file:
        file.write(txt_player + '\n')

def remove_empty_lines(file_path):
    with open(file_path, 'r') as input_file, open('temp_file.txt', 'w') as temp_file:
        lines = input_file.readlines()
        for line in lines:
            if line.strip():
                temp_file.write(line)

    shutil.move('temp_file.txt', file_path)

def normalize_position(position):
    grouped_replacements = {
        'ZGD': [
            'Z@D',
            'ZED',
            # 'ZG6D', 'Z6D', '76D'
        ],
        'ZGE': [
            '2GE'
            # 'Z6E'
        ],
        'LD': [
            # 'LO',
            'LP','UP', 'I)', 'LB',
        ],
        # 'MEI': ['MEL'],
        'GOL': ['@L', 'GL', 'QL'],
        '': [
            "'",
            # 'M.'
        ],
    }

    uppercase_position = position.upper()
    for replacement_key, replacement_values in grouped_replacements.items():
        for key in replacement_values:
            uppercase_position = uppercase_position.replace(key, replacement_key)
        
    return uppercase_position
    
def normalize_player_name(player_name):
    replacements = {
        'ii': 'u',
        'fi': 'n',
        'ié': 'ić',
        'Mério': 'Mario',
        '$': '',
        # '0.': 'O.',
        # 'T. AlexanderAr...': 'T. Alexander-Arnold',
        # 'A. Zambo Anguis...': 'A. Zambo Anguissa',
        # 'D. Nujiez': 'D. Nuñez',
        # 'R. Ledo': 'R. Leão',
        # '6. Kobel': 'G. Kobel',
        # 'Kessić': 'Kessié',
        # 'Taglianco': 'Tagliafico',
    }

    grouped_replacements = {
        '': ['+', '*', '>', '@', '—', '_', '', '='],
        'I.': ['l.', '|.', 'i.']
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

def normalize_notes(note):
    note = note.replace(')', '')
    
    if re.match(r'^(?!^\d{3}$)(\d{1,2})[.,]?\d{1}$', note):
        pattern = r'^(\d{1,2})[.,]?(\d{1})$'
        replacement = r'\1.\2'
        normalized_note = re.sub(pattern, replacement, note)
        normalized_note = normalized_note.replace('1.', '7.')
        return normalized_note  # Print the matched portion
    elif re.match(r'^(?!^\d{3}$)[a-zA-Z0-9.,]+$', note) or re.match(r'^(?!^\d{3}$)[a-zA-Z.,]+$', note):
        return "7."
    else:
        return ""

def process_line(line):
    line = line.strip()
    pattern = r'\s+'
    components = re.split(pattern, line)

    if len(components) >= 3:
        position = components[0]
        player_name = ' '.join(components[1:-1])
        note = components[-1]
        player_name_parts = re.split(r'\s|,', player_name)
        player_name_parts = [part for part in player_name_parts if part]
        player_name = ' '.join(player_name_parts)
        return position, player_name, note
    else:
        return None, None, None

def normalize(file_content):
    temp_file_content = []
    
    lines = file_content.split('\n')
    lines = [line for line in lines if line.strip()]

    for line in lines:
        position, player_name, note = process_line(line)
        position = normalize_position(position)
        player_name = normalize_player_name(player_name)
        note = normalize_notes(note)
        temp_file_content.append(f'{position},{player_name},{note}')

    return '\n'.join(temp_file_content)