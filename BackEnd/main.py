import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from google.oauth2 import id_token
from google.auth.transport import requests

from auth import router as auth_router
from utils.file_manager import ensure_directories
from services.ai_content import generate_slide_content
from services.image_generator import generate_image
from services.ppt_generator import create_ppt
from services.voice_generator import create_voice
from services.video_generator import create_video


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

ensure_directories()

GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
security = HTTPBearer()


# -----------------------------
# VERIFY GOOGLE TOKEN
# -----------------------------
def verify_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )

        return idinfo

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Google Token")


# -----------------------------
# PARSE AI SLIDES
# -----------------------------
def parse_slides(text):

    slides = []
    blocks = text.split("Slide")

    for block in blocks:

        lines = block.strip().split("\n")

        if len(lines) > 1:

            title = lines[0].replace("*", "").strip()

            points = []

            for line in lines[1:]:

                if "-" in line or "*" in line:
                    points.append(
                        line.replace("-", "")
                        .replace("*", "")
                        .strip()
                    )

            slides.append({
                "title": title,
                "points": points
            })

    return slides


# -----------------------------
# DOWNLOAD PPT
# -----------------------------
@app.get("/download/ppt/{filename}")
def download_ppt(filename: str):

    path = f"outputs/slides/{filename}"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="PPT not found")

    return FileResponse(
        path,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        filename=filename
    )


# -----------------------------
# DOWNLOAD VIDEO
# -----------------------------
@app.get("/download/video/{filename}")
def download_video(filename: str):

    path = f"outputs/videos/{filename}"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Video not found")

    return FileResponse(
        path,
        media_type="video/mp4",
        filename=filename
    )


# -----------------------------
# DOWNLOAD AUDIO
# -----------------------------
@app.get("/download/audio/{filename}")
def download_audio(filename: str):

    path = f"outputs/audio/{filename}"

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Audio not found")

    return FileResponse(
        path,
        media_type="audio/mpeg",
        filename=filename
    )


# -----------------------------
# GENERATE PRESENTATION
# -----------------------------
@app.post("/generate")
def generate(topic: str, slides: int):

    print("API CALLED")

    ai_text = generate_slide_content(topic, slides)

    slide_data = parse_slides(ai_text)
    print("PARSED SLIDES:", slide_data)

    image_paths = []

    for i, slide in enumerate(slide_data):

        # -------- GENERATE IMAGE ONLY FOR FEW SLIDES --------
        if i % 3 == 0 and i != 0:   # every 3rd slide except title slide
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
                slide["image"] = None

        else:
            slide["image"] = None

    # ---------- CREATE PPT ----------
    try:
        print("Creating PPT")

        ppt_file = create_ppt(
            slide_data,
            topic.replace(" ", "_")
        )

    except Exception as e:
        print("PPT ERROR:", e)
        ppt_file = None

    # ---------- CREATE AUDIO ----------
    try:
        narration = " ".join(
            [s["title"] + " " + " ".join(s["points"]) for s in slide_data]
        )

        print("Creating voice")

        audio_file = create_voice(
            narration,
            topic.replace(" ", "_")
        )

    except Exception as e:
        print("VOICE ERROR:", e)
        audio_file = None

    # ---------- CREATE VIDEO ----------
    # video_name = None
    # if video_file:
    #     video_name = os.path.basename(video_file)
    try:
        print("Creating video")

        video_file = create_video(
            "outputs/images",
            audio_file,
            f"outputs/videos/{topic.replace(' ','_')}.mp4",
            topic
        )

    except Exception as e:
        print("VIDEO ERROR:", e)
        video_file = None

    # ---------- RETURN LINKS ----------
    return {
        "ppt": f"/download/ppt/{os.path.basename(ppt_file)}" if ppt_file else None,
        "video": f"/download/video/{os.path.basename(video_file)}" if video_file else None,
        "audio": f"/download/audio/{os.path.basename(audio_file)}" if audio_file else None,
        "slides": slide_data,
        "images": image_paths
    }
