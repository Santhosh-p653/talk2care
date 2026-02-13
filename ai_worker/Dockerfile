FROM python:3.10-slim
RUN apt-get update && apt-get install -y build-essential git wget ffmpeg && rm -rf /var/lib/apt/lists/*
# Clone and compile whisper.cpp
RUN git clone https://github.com/ggerganov/whisper.cpp.git /whisper
WORKDIR /whisper
RUN make
# Download the 'base' model automatically
RUN bash ./models/download-ggml-model.sh base
COPY . .
# Keep it running or start a simple python wrapper
CMD ["./main", "-m", "models/ggml-base.bin", "--port", "8000"]

