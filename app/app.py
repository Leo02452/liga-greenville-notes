from flask import Flask, render_template, request, redirect
from extract_notes_to_text import extract_notes

app = Flask(
    __name__,
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if (
        request.method == 'POST' and
        'home_image_1' and
        'home_image_2'in request.files and
        'season' and
        'day' and
        'number_of_games' in request.form
    ):
        image1 = request.files['home_image_1']
        image2 = request.files['home_image_2']
        season = request.form['season']
        day = request.form['day']
        number_of_games = request.form['number_of_games']
        
        image1.save(f'backups/{season}/{day}/images/originals/' + image1.filename)
        image2.save(f'backups/{season}/{day}/images/originals/' + image2.filename)
        extract_notes(season, day, int(number_of_games))
        return redirect(f'/notes-registration/{season}/{day}/{number_of_games}')

    return render_template(
        'index.html',
      )

