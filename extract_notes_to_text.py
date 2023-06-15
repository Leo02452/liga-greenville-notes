from helpers.image import combine_images, invert_colors
from helpers.image_to_text import extract_image_to_text

season = 'season07'
day_of_league = 'day03'
number_of_games = 16

for index in range(1, (number_of_games + 1)):
    home_image_1 = f"backups/{season}/{day_of_league}/images/originals/j{index}h1.png"
    home_image_2 = f"backups/{season}/{day_of_league}/images/originals/j{index}h2.png"
    away_image_1 = f"backups/{season}/{day_of_league}/images/originals/j{index}a1.png"
    away_image_1 = f"backups/{season}/{day_of_league}/images/originals/j{index}a2.png"
    home_saved_image = f"backups/{season}/{day_of_league}/images/j{index}h.png"
    away_saved_image = f"backups/{season}/{day_of_league}/images/j{index}a.png"
    combine_images(home_image_1, home_image_2, home_saved_image)
    combine_images(away_image_1, away_image_1, away_saved_image)

    home_saved_inverted_image = f"backups/{season}/{day_of_league}/images/inverted/j{index}h.png"
    away_saved_inverted_image = f"backups/{season}/{day_of_league}/images/inverted/j{index}a.png"
    invert_colors(home_saved_image, home_saved_inverted_image)
    invert_colors(away_saved_image, away_saved_inverted_image)

    home_txt_file = f"backups/{season}/{day_of_league}/texts/j{index}h.txt"
    away_txt_file = f"backups/{season}/{day_of_league}/texts/j{index}a.txt"
    extract_image_to_text(home_saved_inverted_image, home_txt_file)
    extract_image_to_text(away_saved_inverted_image, away_txt_file)
