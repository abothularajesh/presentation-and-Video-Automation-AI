from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from services.image_generator import generate_image
import os


def create_video(images_folder, audio_path, output_path, topic):

    print("Generating extra images for video")

    # Generate two extra images for video only
    extra1 = "extra_1"
    extra2 = "extra_2"

    generate_image(f"{topic} futuristic technology illustration", extra1)
    generate_image(f"{topic} conceptual digital art scene", extra2)
    generate_image(f"{topic} futuristic technology illustration", extra1)
    generate_image(f"{topic} conceptual digital art scene", extra2)

    # Load narration audio
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration

    # Collect all images (including extra ones)
    images = sorted([
        os.path.join(images_folder, img)
        for img in os.listdir(images_folder)
        if img.endswith(".png") or img.endswith(".jpg")
    ])

    if len(images) == 0:
        print("No images found for video")
        return

    # Calculate duration per image
    slide_duration = audio_duration / len(images)

    clips = []

    for img in images:
        clip = ImageClip(img)
        clip = clip.with_duration(slide_duration)
        clips.append(clip)

    video = concatenate_videoclips(clips)

    video = video.with_audio(audio)

    print("Writing video file...")

    video.write_videofile(output_path, fps=24)
