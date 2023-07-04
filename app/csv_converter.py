import csv

def save_in_csv(players_list, game_info):
    output_file = 'app/static/season07/day03/datas/data.csv'
    with open(output_file, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        for player in players_list:
            writer.writerow([
                player["position"],
                player["name"],
                player["note"],
                game_info['team'],
                game_info['opponent'],
                game_info['competition']
            ])
