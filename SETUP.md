# 🛠 Setup & Installation Guide

This guide will help you get the **Talk2Care** environment running locally using Docker. This setup automates the installation of PostgreSQL, Flask, Streamlit, and the Whisper.cpp AI engine.

---

## 📋 Prerequisites

Before starting, ensure you have the following installed on your machine:
* **Docker & Docker Compose** (Desktop or Engine)
* **Git**
* **SSH Key** (configured for GitHub access)

---

## ⚙️ Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone git@github.com:Santhosh-p653/talk2care.git
cd talk2care
touch .env
POSTGRES_USER=santhosh
POSTGRES_PASSWORD=secret
POSTGRES_DB=talk2care_db
DATABASE_URL=postgresql://santhosh:secret@db:5432/talk2care_db
WHISPER_MODEL=base
FLASK_ENV=development
docker compose up --build
