# FastAPI Basic Project

This project contains a minimal FastAPI application.

## Setup

1. Create a virtual environment:
   python -m venv .venv
2. Activate it:
   - Windows: .venv\Scripts\activate
   - macOS/Linux: source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Run the API:
   uvicorn app.main:app --reload

## Endpoints

- GET /
- GET /health
