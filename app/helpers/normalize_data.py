import unicodedata

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

