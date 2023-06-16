from helpers.csv_converter import text_to_csv, table_to_csv

boca_juniors = 'Boca Juniors'
estudiantes = 'Estudiantes'
independiente = 'Independiente'
racing = 'Racing'
river_plate = 'River Plate'
rosario_central = 'Rosario Central'
san_lorenzo = 'San Lorenzo'
velez_sarsfield = 'Velez Sarsfield'
argentinos_jrs = 'Argentinos Jrs'
arsenal_sarandi = 'Arsenal de Sarandi'
defensa_justica = 'Defensa Y Justicia'
huracan = 'Huracan'
lanus = 'Lanus'
newells_old_boyd = 'Newells Old Boys'
talleres = 'Talleres'
tigre = 'Tigre'

season = 'season07'
day_of_league = 'day02'

game = 'j16'
home_team = huracan
away_team = defensa_justica
competition = 'B'

home_team_txt = f'backups/{season}/{day_of_league}/texts/{game}h.txt'
away_team_txt = f'backups/{season}/{day_of_league}/texts/{game}a.txt'
csv_to_append = f'backups/{season}/{day_of_league}/datas/notes.csv'

text_to_csv(
    home_team_txt,
    csv_to_append,
    {
        'time': home_team,
        'adversario': away_team,
        'competicao': competition
    },
)

text_to_csv(
    away_team_txt,
    csv_to_append,
    {
        'time': away_team,
        'adversario': home_team,
        'competicao': competition
    },
)
# table_to_csv(text_from_image, csv_to_append, game_info)
