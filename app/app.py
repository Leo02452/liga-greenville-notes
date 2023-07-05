from flask import Flask, render_template, request, redirect, session
from app.extract_notes_to_text import extract_notes
from app.update_active_players import teams, competitions, active_players_list, positions_list
from werkzeug.utils import secure_filename
from app.helpers.extraction import extract_text_to_list
from app.csv_converter import save_in_csv
import os

app = Flask(
    __name__,
    )

app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if all(field in request.form for field in ['season', 'day', 'number_of_games']):
            season = request.form['season']
            day = request.form['day']
            number_of_games = request.form['number_of_games']

            image_dir = os.path.join(app.root_path, 'static', season, day, 'images', 'originals')
            os.makedirs(image_dir, exist_ok=True)

            for key, file in request.files.items():
                if key.startswith('home_image_') or key.startswith('away_image_'):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(image_dir, filename)
                    file.save(file_path)

            extract_notes(season, day, int(number_of_games))
            return redirect(f'/notes-registration/{season}/{day}/{number_of_games}')

    return render_template('index.html')

@app.route('/notes-registration/<season>/<day>/<number_of_games>', methods=['GET', 'POST'])
def show_notes(
    season, day, number_of_games
    ):

    image_paths = []
    extracted_data = []
    for index in range(1, (int(number_of_games) + 1)):
        home_image = f'{season}/{day}/images/j{index}h.png'
        away_image = f'{season}/{day}/images/j{index}a.png'
        image_paths.append(home_image)
        image_paths.append(away_image)
    
        home_file_path = f'app/static/{season}/{day}/texts/j{index}h.txt'
        away_file_path = f'app/static/{season}/{day}/texts/j{index}a.txt'
        home_file_data = extract_text_to_list(home_file_path)
        away_file_data = extract_text_to_list(away_file_path)
        extracted_data.append(home_file_data)
        extracted_data.append(away_file_data)
    
    session['image_paths'] = image_paths
    session['extracted_data'] = extracted_data
    session['season'] = season
    session['day'] = day

    return render_template(
        'notes.html',
        image_paths=image_paths,
        teams=teams,
        competitions=competitions,
        active_players_list=active_players_list,
        extracted_data=extracted_data,
        positions_list=positions_list,
        )

@app.route('/game-submition', methods=['POST'])
def submit_game():
    home_team = request.form["home_team"]
    away_team = request.form["away_team"]
    competition = request.form["competition"]
    home_team_players = []
    away_team_players = []
    index = 1
    while True:
        if (
            f"ht_position_{index}" in request.form and
            f"ht_name_{index}" in request.form and
            f"ht_note_{index}" in request.form
            ):
                home_team_player_position = request.form[f"ht_position_{index}"]
                home_team_player_name = request.form[f"ht_name_{index}"]
                home_team_player_note = request.form[f"ht_note_{index}"]

                home_team_players.append({
                    'position': home_team_player_position,
                    'name': home_team_player_name,
                    'note': home_team_player_note
                })

        if (
            f"at_position_{index}" in request.form and
            f"at_name_{index}" in request.form and
            f"at_note_{index}" in request.form
            ):
                away_team_player_position = request.form[f"at_position_{index}"]
                away_team_player_name = request.form[f"at_name_{index}"]
                away_team_player_note = request.form[f"at_note_{index}"]

                away_team_players.append({
                    'position': away_team_player_position,
                    'name': away_team_player_name,
                    'note': away_team_player_note
                })

                index += 1
        else:
             index += 1
             break
        
    season = session.get('season')
    day = session.get('day')

    save_in_csv(
        home_team_players,
        {
            "team": home_team,
            "opponent": away_team,
            "competition": competition,
        },
        season,
        day,
    )

    save_in_csv(
        away_team_players,
        {
            "team": away_team,
            "opponent": home_team,
            "competition": competition,
        },
        season,
        day
    )

    image_paths = session.get('image_paths')
    extracted_data = session.get('extracted_data')

    submitted_form_indexes = session.get('submitted_form_indexes', [])
    submitted_form_indexes.append(int(request.form.get("form_index")))
    session['submitted_form_indexes'] = submitted_form_indexes

    return render_template(
        'notes.html',
        image_paths=image_paths,
        teams=teams,
        competitions=competitions,
        active_players_list=active_players_list,
        extracted_data=extracted_data,
        positions_list=positions_list,
        submitted_form_indexes=submitted_form_indexes,
        )

if __name__ == '__main__':
    app.run()
