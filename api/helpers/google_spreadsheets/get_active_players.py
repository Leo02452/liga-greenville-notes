# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

from .spreadsheet_agent import workbook
data = workbook.worksheet('Jog_ativos').get_all_values()

active_players_list = [
    value.strip() for sublist in data
    for value in sublist if value.strip()
]

active_players_list.sort()
