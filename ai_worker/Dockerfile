FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    wget \
    ffmpeg \
    cmake \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone whisper.cpp explicitly
RUN git clone https://github.com/ggerganov/whisper.cpp.git /app/whisper.cpp

WORKDIR /app/whisper.cpp
RUN make

# Download base model
RUN bash ./models/download-ggml-model.sh base

WORKDIR /app
COPY worker.py ./

CMD ["python", "worker.py"]
