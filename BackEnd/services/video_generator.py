from moviepy.editor import ImageClip, concatenate_videoclips

def create_video(image_paths, output):

    clips = []

    for img in image_paths:

        clip = ImageClip(img).set_duration(5)
        clips.append(clip)

    final = concatenate_videoclips(clips)

    video_path = f"outputs/videos/{output}.mp4"

    final.write_videofile(video_path, fps=24)

    return video_path