import csv
from refine_data import replace_players, convert_numbers
from update_active_players import active_players_list

def text_to_csv(
        input_file,
        output_file,
        game_info,
    ):
    with open(input_file, 'r') as infile, open(output_file, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        lines = infile.readlines()
        number_of_players = int(len(lines) / 3)
        print(number_of_players)

        pos_line = 0
        nome_line = number_of_players
        np_line = number_of_players * 2
        loop_limit = number_of_players * 3
          
        while np_line < loop_limit:
            writer.writerow([
                lines[pos_line].strip(),
                replace_players(active_players_list, lines[nome_line].strip()),
                convert_numbers(lines[np_line].strip()),
                game_info['time'],
                game_info['adversario'],
                game_info['competicao']
            ])
            pos_line += 1
            nome_line += 1
            np_line += 1
    infile.close()
    outfile.close()

def table_to_csv(
        input_file,
        output_file,
        game_info,
    ):
    with open(input_file, 'r') as infile, open(output_file, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        reader = csv.reader(infile)
        for pos, name, np in reader:
            writer.writerow([
                pos,
                name,
                np,
                game_info['time'],
                game_info['adversario'],
                game_info['competicao']
            ])
    infile.close()
    outfile.close()