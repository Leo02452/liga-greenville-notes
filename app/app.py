from flask import Flask, render_template, request, redirect
from extract_notes_to_text import extract_notes
from update_active_players import teams, competitions
from werkzeug.utils import secure_filename
import os

app = Flask(
    __name__,
    )

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
def extract_notes(
    season, day, number_of_games
    ):

    image_paths = []
    for index in range(1, (int(number_of_games) + 1)):
        home_image = f'{season}/{day}/images/j{index}h.png'
        away_image = f'{season}/{day}/images/j{index}a.png'
        image_paths.append(home_image)
        image_paths.append(away_image)
    return render_template(
        'notes.html',
        image_paths=image_paths,
        teams=teams,
        competitions=competitions,
        )

if __name__ == '__main__':
    app.run()
