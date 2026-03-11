import requests
import os
from PIL import Image
from io import BytesIO

# Hugging api key.
HF_API_KEY = "*********************************"  

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_image(prompt, filename):

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception("Image generation failed")

    image = Image.open(BytesIO(response.content))

    path = f"outputs/images/{filename}.png"

    image.save(path)

    return path