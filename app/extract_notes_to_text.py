from app.helpers.image import combine_images, invert_colors
from app.helpers.image_to_text import extract_image_to_text
import app.helpers.normalize_data as normalize_data
import os

def extract_notes(season, day_of_league, number_of_games):
    for index in range(1, (number_of_games + 1)):
        os.makedirs(f"app/static/{season}/{day_of_league}/images/originals", exist_ok=True)
        home_image_1 = f"app/static/{season}/{day_of_league}/images/originals/j{index}h1.png"
        home_image_2 = f"app/static/{season}/{day_of_league}/images/originals/j{index}h2.png"
        away_image_1 = f"app/static/{season}/{day_of_league}/images/originals/j{index}a1.png"
        away_image_2 = f"app/static/{season}/{day_of_league}/images/originals/j{index}a2.png"
        home_saved_image = f"app/static/{season}/{day_of_league}/images/j{index}h.png"
        away_saved_image = f"app/static/{season}/{day_of_league}/images/j{index}a.png"
        combine_images(home_image_1, home_image_2, home_saved_image)
        combine_images(away_image_1, away_image_2, away_saved_image)

        os.makedirs(f"app/static/{season}/{day_of_league}/images/inverted", exist_ok=True)
        home_saved_inverted_image = f"app/static/{season}/{day_of_league}/images/inverted/j{index}h.png"
        away_saved_inverted_image = f"app/static/{season}/{day_of_league}/images/inverted/j{index}a.png"

        invert_colors(home_saved_image, home_saved_inverted_image)
        invert_colors(away_saved_image, away_saved_inverted_image)

        os.makedirs(f"app/static/{season}/{day_of_league}/texts", exist_ok=True)
        home_txt_file = f"app/static/{season}/{day_of_league}/texts/j{index}h.txt"
        away_txt_file = f"app/static/{season}/{day_of_league}/texts/j{index}a.txt"
        extract_image_to_text(home_saved_inverted_image, home_txt_file)
        extract_image_to_text(away_saved_inverted_image, away_txt_file)

        normalize_data.normalize(home_txt_file)
        normalize_data.normalize(away_txt_file)
