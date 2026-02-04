from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
import uuid
from pathlib import Path

app = FastAPI()
MIMIC3_URL = "http://127.0.0.1:59125/api/tts"

@app.get("/tts")
def tts(text: str, voice: str = "en_US/ljspeech_low"):
    out = Path(f"/tmp/{uuid.uuid4()}.wav")

    r = requests.get(
        MIMIC3_URL,
        params={"text": text, "voice": voice},
        timeout=30
    )
    r.raise_for_status()

    out.write_bytes(r.content)
    return FileResponse(out, media_type="audio/wav")
