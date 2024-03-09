import requests, datetime

from .generate_access_token import GRAPH_API_ENDPOINT, headers
from ..image import combine_images, invert_colors
from ..converters import extract_image_to_text
from ..normalize_data import normalize

def get_string_now_date(file_extension):
    now_date = datetime.datetime.now()
    date_format = "%Y-%m-%d_%H-%M-%S"
    date_formatted = now_date.strftime(date_format)
    return f"{date_formatted}.{file_extension}"

def get_file_content(file_id):
    return requests.get(
        GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}/content',
        headers=headers,
    ).content

def get_images_list(season, week, folder):
    response = requests.get(
        GRAPH_API_ENDPOINT + f'/me/drive/root:/Notas/{season}/{week}/Fotos/{folder}:/children?select=id,webUrl,image,name&orderby=name%20asc',
        headers=headers,
    )

    files = response.json()['value']
    return files

def get_texts_list(season, week):
    response = requests.get(
        GRAPH_API_ENDPOINT + f'/me/drive/root:/Notas/{season}/{week}/Dados:/children?select=id,name&orderby=name%20asc',
        headers=headers,
    )

    files = response.json()['value']
    return files

def upload_file_content(folder_path, headers, data):
        requests.put(
            GRAPH_API_ENDPOINT + folder_path,
            headers=headers,
            data=data
        )

def upload_combined_team_images(season, week):
    images_list = get_images_list(season, week, 'Originais')
    for index in range(0, len(images_list), 2):
        file_1_id = images_list[index]['id']
        file_2_id = images_list[index + 1]['id']

        file_1_content = get_file_content(file_1_id)
        file_2_content = get_file_content(file_2_id)
        combined_image = combine_images(file_1_content, file_2_content)
        file_name = get_string_now_date('png')

        folder_path = f'/me/drive/items/root:/Notas/{season}/{week}/Fotos/Completas/{file_name}:/content'
        upload_file_content(folder_path, headers, combined_image)

def upload_inverted_color_images(season, week):
    images_list = get_images_list(season, week, 'Completas')
    for image in images_list:
        image_id = image['id']
        image_name = image['name']

        image_content = get_file_content(image_id)
        inverted_image = invert_colors(image_content)

        folder_path = f'/me/drive/items/root:/Notas/{season}/{week}/Fotos/Invertidas/{image_name}:/content'
        upload_file_content(folder_path, headers, inverted_image)

def upload_extracted_texts(season, week):
    images_list = get_images_list(season, week, 'Invertidas')
    for image in images_list:
        image_id = image['id']

        image_content = get_file_content(image_id)
        extracted_text = extract_image_to_text(image_content)
        normalized_content = normalize(extracted_text)
        txt_file_name = get_string_now_date('txt')

        folder_path = f'/me/drive/items/root:/Notas/{season}/{week}/Dados/{txt_file_name}:/content'
        upload_file_content(folder_path, headers, normalized_content)
