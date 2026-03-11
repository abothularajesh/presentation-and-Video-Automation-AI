import os

def ensure_directories():

    folders = [
        "outputs/images",
        "outputs/slides",
        "outputs/videos",
        "outputs/audio"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)