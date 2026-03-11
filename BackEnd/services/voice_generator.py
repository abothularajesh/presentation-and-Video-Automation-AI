from gtts import gTTS

def create_voice(text, filename):

    tts = gTTS(text)

    path = f"outputs/audio/{filename}.mp3"
    tts.save(path)

    return path