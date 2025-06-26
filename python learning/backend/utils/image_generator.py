import requests
import os
from flask import current_app

def generate_explanation_image(prompt, filename):
    api_key = current_app.config['OPENAI_API_KEY']
    url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'dall-e-3',
        'prompt': prompt,
        'n': 1,
        'size': '1024x1024'
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    image_url = response.json()['data'][0]['url']
    img_data = requests.get(image_url).content
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, filename)
    with open(image_path, 'wb') as f:
        f.write(img_data)
    return image_path 