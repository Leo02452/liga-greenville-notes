from flask import Flask, redirect, render_template, request, session

from .helpers.converters import extract_text_to_list
from .helpers.extract_notes_to_text import extract_notes
from .helpers.google_spreadsheets.get_active_players import active_players_list
from .helpers.google_spreadsheets.write_in_gspreadsheet import \
    write_players_notes_in_google_sheets
from .helpers.season_static_data import competitions, positions_list, teams
from .helpers.onedrive.handle_onedrive_files import get_texts_list, get_file_content, get_images_list

app = Flask(
    __name__,
    static_folder='./static',
    template_folder='./templates',
    )

app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if all(field in request.form for field in ['season', 'day', 'number_of_games']):
            season = request.form['season']
            day = request.form['day']

            extract_notes(season, day)
            return redirect(f'/notes-registration/{season}/{day}')

    return render_template('index.html')

@app.route('/notes-registration/<season>/<day>', methods=['GET', 'POST'])
def show_notes(
    season, day
    ):

    extracted_data = []
    texts_list = get_texts_list(season, day)
    images_list = get_images_list(season, day, 'Completas')
    for text in texts_list:
        text_id = text['id']
        file_content = get_file_content(text_id)
        team_data = extract_text_to_list(file_content)
        extracted_data.append(team_data)

    image_paths = []
    for image in images_list:
        image_url = image['webUrl']
        image_paths.append(image_url)
    
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

    write_players_notes_in_google_sheets(
         home_team_players,
         {
            "team": home_team,
            "opponent": away_team,
            "competition": competition,
        },
    )

    write_players_notes_in_google_sheets(
        away_team_players,
        {
            "team": away_team,
            "opponent": home_team,
            "competition": competition,
        },
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
