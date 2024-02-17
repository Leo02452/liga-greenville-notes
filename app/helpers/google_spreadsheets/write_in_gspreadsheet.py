from .spreadsheet_agent import workbook

def write_players_notes_in_google_sheets(players_list, game_info):
    worksheet = workbook.worksheet("Data")
    column_a = worksheet.col_values(1)
    first_avaiable_row = len(column_a) + 1
    data_to_add = []
    for player in players_list:
        data_to_add.append([ 
            player["position"],
            player["name"],
            player["note"].replace('.', ','),
            game_info['team'],
            game_info['opponent'],
            game_info['competition']
        ])
    cell_range = f'A{first_avaiable_row}:F{first_avaiable_row + len(data_to_add) - 1}'
    worksheet.update(cell_range, data_to_add)
