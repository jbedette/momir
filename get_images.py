import json
from PIL import Image
from io import BytesIO
import requests
import time

# with open('./data/creatures.json', 'r', encoding='utf-8') as file:
#     creatures = json.load(file)




def download_cropped_image(image_uri, file_name, delay=0.10):
    # Fetch the cropped image directly using the URI
    time.sleep(delay)
    response = requests.get(image_uri)
    
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img = convert_to_black_and_white(img)
        img.show()
        # Save the image with the specified file name
        img.save(f"./images/{file_name}.jpg")
        # print(f"Image saved as {file_name}.jpg")
        return img
    else:
        print(f"Failed to download image from {image_uri}")




def convert_to_black_and_white(img):
    
    # Convert the image to grayscale (black and white)
    bw_img = img.convert("L")
    
    # Save the black and white image
    # bw_img.save(output_path)
    return bw_img

if __name__ == "__main__":
    download_cropped_image()