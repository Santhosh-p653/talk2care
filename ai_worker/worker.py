import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

WHISPER_BIN = "/app/whisper.cpp/main"
MODEL_PATH = "/app/whisper.cpp/models/ggml-base.bin"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio = request.files["file"]
    audio_path = "/tmp/input_audio.wav"
    audio.save(audio_path)

    cmd = [
        WHISPER_BIN,
        "-m", MODEL_PATH,
        "-f", audio_path,
        "-nt",    # no timestamps
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return jsonify({"error": result.stderr}), 500

    return jsonify({"transcript": result.stdout.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
