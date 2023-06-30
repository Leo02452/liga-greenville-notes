import unicodedata

def remove_accents_and_letter_through(player):
    normalized_player = unicodedata.normalize('NFD', player)
    stripped_player = ''.join(c for c in normalized_player if unicodedata.category(c) != 'Mn')
    first_through_correction = stripped_player.replace('ø', 'o')
    second_through_correction = first_through_correction.replace('Ø', 'O')
    return second_through_correction

