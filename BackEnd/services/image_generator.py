import requests
import os
from PIL import Image
from io import BytesIO

ACCOUNT_ID = "YOUR_ACC_ID"
API_TOKEN = "Your_API_KEY"

API_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_image(prompt, filename):

    # Clean prompt for better images
    prompt = prompt.replace("*", "").replace(":", "").strip()

    payload = {
        "prompt": f"minimal presentation illustration, infographic style, {prompt}"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Image generation failed: {response.text}")

    image = Image.open(BytesIO(response.content))

    path = f"outputs/images/{filename}.png"

    image.save(path)

    return path
