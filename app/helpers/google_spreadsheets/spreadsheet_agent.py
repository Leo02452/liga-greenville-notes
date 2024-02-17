import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('app/helpers/google_spreadsheets/creds.json', scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open('24_France')
