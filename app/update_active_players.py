import csv

positions_list = [
    'GOL',
    'ZAG', 'ZGD', 'ZGE',
    'LD', 'LE', 'ADD', 'ADE',
    'VOL', 'VLD', 'VLE',
    'MC', 'MCE', 'MCD',
    'MD', 'ME', 'PD', 'PE',
    'MEI', 'MEE', 'MED',
    'SA', 'MAD', 'MAE',
    'ATA', 'ATD', 'ATE'
]

teams = [
    'Boca Juniors', 'Estudiantes',
    'Independiente', 'Racing',
    'River Plate', 'Rosario Central',
    'San Lorenzo', 'Velez Sarsfield',
    'Argentinos Jrs', 'Arsenal de Sarandi',
    'Defensa Y Justicia', 'Huracan',
    'Lanus', 'Newells Old Boys',
    'Talleres', 'Tigre'
]

competitions = ['A', 'B', 'C', 'SC']

def update_active_players():
    with open('active_players.csv', 'r') as file:
        players_list = list()
        for line in file:
            if line.strip():
                players_list.append(line.strip())
    return players_list

active_players_list = update_active_players()
print('updated')
