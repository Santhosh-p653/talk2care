M python:3.10-slim
WORKDIR /app
# Install system deps for Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# This line automates the NLTK download during build
RUN python -m nltk.downloader punkt stopwords wordnet
COPY . .
CMD ["python", "app.py"]

