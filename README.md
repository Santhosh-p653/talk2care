# Talk2Care: Agentic AI Assistant

An advanced, multi-service AI platform combining speech-to-text, natural language processing, and persistent data storage. Talk2Care leverages **Whisper.cpp** for high-performance transcription and **NLTK** for linguistic analysis.

## 🚀 Tech Stack
- **Frontend:** Streamlit (Interactive UI)
- **Backend:** Flask (REST API)
- **AI Engine:** Whisper.cpp (C++ Inference)
- **Database:** PostgreSQL (SQLAlchemy ORM)
- **Containerization:** Docker Compose
- **NLP:** NLTK (Tokenization & Analysis)

## 🛠 Architecture
The system is built using a microservices architecture:
1. **Frontend**: Handles user interaction and audio uploads.
2. **Backend**: Managed business logic, database transactions, and NLP tasks.
3. **AI Worker**: A high-performance C++ service dedicated to audio processing.
4. **Database**: Securely stores user logs and transcription history.



## 🏗 Setup
Please refer to [SETUP.md](./SETUP.md) for detailed installation and deployment instructions.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.
