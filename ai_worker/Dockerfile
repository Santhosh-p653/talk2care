FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/ggerganov/whisper.cpp.git
WORKDIR /app/whisper.cpp
RUN make
RUN bash ./models/download-ggml-model.sh base

WORKDIR /app
COPY . .

CMD ["python", "worker.py"]
