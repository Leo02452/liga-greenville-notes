from .onedrive.handle_onedrive_files import upload_combined_team_images, upload_inverted_color_images, upload_extracted_texts

def extract_notes(season, week):
    upload_combined_team_images(season, week)
    upload_inverted_color_images(season, week)
    upload_extracted_texts(season, week)
