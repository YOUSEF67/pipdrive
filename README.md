# Pipedrive DevOps Challenge

A Python Flask application that:
- Fetches a user’s public GitHub gists.
- Creates a mock "deal" for each gist via a `/deals` endpoint (instead of Pipedrive API).
- Provides scheduled scans every 3 hours (via Render cron job).

---

## 🚀 Features
- REST API built with Flask
- Dockerized (Python 3.11-slim)
- CI/CD with GitHub Actions:
  - Tests (pytest)
  - Docker build + health check
- Cloud deployment on [Render](https://render.com) (free tier)
- Automatic gist scans every 3 hours

---

## 📂 API Endpoints
- `GET /health` → Health check
- `POST /track/<username>` → Start tracking a GitHub user
- `GET /gists/<username>` → List gists for a user
- `GET /deals` → List all mock deals
- `POST /scan` → Trigger scan for all tracked users (called by cron job)

---

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- [Poetry](https://python-poetry.org/) or pip
- Docker (optional, for containerized run)

### Setup (without Docker)
```bash
git clone https://github.com/YOUSEF67/pipdrive.git
cd pipdrive
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
