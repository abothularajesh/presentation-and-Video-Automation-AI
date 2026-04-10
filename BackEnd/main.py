from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.file_manager import ensure_directories
from services.ai_content import generate_slide_content
from services.image_generator import generate_image
from services.ppt_generator import create_ppt
from services.voice_generator import create_voice
from services.video_generator import create_video

app = FastAPI()

from fastapi.staticfiles import StaticFiles
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ensure_directories()

def parse_slides(text):

    slides = []
    blocks = text.split("Slide")

    for block in blocks:
        lines = block.strip().split("\n")

        if len(lines) > 1:

            title = lines[0]
            points = []

            for line in lines[1:]:
                if "-" in line or "*" in line:
                    points.append(line.replace("-", "").replace("*", "").strip())

            slides.append({
                "title": title,
                "points": points
            })

    return slides


@app.post("/generate")
def generate(topic: str, slides: int):

    print("API CALLED")

    ai_text = generate_slide_content(topic, slides)
    print("AI TEXT:", ai_text)

    slide_data = parse_slides(ai_text)
    print("PARSED SLIDES:", slide_data)

    image_paths = []

    for i, slide in enumerate(slide_data):
        try:
            print("Generating image for:", slide["title"])

            img_path = generate_image(
                slide["title"],
                f"{topic.replace(' ','_')}_slide_{i}"
            )

            image_paths.append(img_path)
            slide["image"] = img_path

        except Exception as e:
            print("IMAGE ERROR:", e)

    try:
        print("Creating PPT")
        ppt_file = create_ppt(slide_data, topic.replace(" ", "_"))
    except Exception as e:
        print("PPT ERROR:", e)
        ppt_file = None

    try:
        narration = " ".join(
            [s["title"] + " " + " ".join(s["points"]) for s in slide_data]
        )

        print("Creating voice")
        audio_file = create_voice(narration, topic.replace(" ", "_"))

        safe_topic = topic.replace(" ", "_")

        video_path = f"outputs/videos/{safe_topic}.mp4"

        # DELETE OLD FILE IF EXISTS (VERY IMPORTANT)
        import os
        if os.path.exists(video_path):
            os.remove(video_path)

        create_video(
            "outputs/images",
            audio_file,
            video_path,
            topic,
            narration
        )

    except Exception as e:
        print("VOICE ERROR:", e)
        audio_file = None

    return {
        "ppt": f"http://127.0.0.1:8000/{ppt_file}",
        "audio": audio_file,
        "video": f"http://127.0.0.1:8000/{video_path}",
        "slides": slide_data,
        "images": image_paths
    }             

