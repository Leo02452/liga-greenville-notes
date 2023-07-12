import gspread

gc = gspread.oauth()

sh = gc.open("23 - Argentina_Greenville")

data = sh.get_worksheet(5).get_all_values()

active_players_list = [
    value.strip() for sublist in data
    for value in sublist if value.strip()
]

active_players_list.sort()
