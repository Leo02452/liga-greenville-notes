import csv, os

def save_in_csv(players_list, game_info, season, day):
    os.makedirs(f'app/static/{season}/{day}/datas', exist_ok=True)
    output_file = f'app/static/{season}/{day}/datas/data.csv'
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
