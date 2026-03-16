from gtts import gTTS

def create_voice(text, filename):
    #removing the special characters...
    text = re.sub(r'^\d+[\.\)\-\s]*:', '', text)
    tts = gTTS(text)

    path = f"outputs/audio/{filename}.mp3"
    tts.save(path)

    return path
