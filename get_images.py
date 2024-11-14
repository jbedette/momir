import json
from PIL import Image
from io import BytesIO
import requests
import time

with open('./data/creatures.json', 'r', encoding='utf-8') as file:
    creatures = json.load(file)

creature_images = []



def download_cropped_image(image_uri, file_name, delay=0.10):
    # Fetch the cropped image directly using the URI
    time.sleep(delay)
    response = requests.get(image_uri)
    
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        # Save the image with the specified file name
        img.save(f"./images/{file_name}.jpg")
        # print(f"Image saved as {file_name}.jpg")
    else:
        print(f"Failed to download image from {image_uri}")


for c in creatures:
    download_cropped_image(c['image_uris']['art_crop'],c['name'])