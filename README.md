# Career Match Engine

**Status: In Active Development**

A small FastAPI foundation for a future job-matching service. The current repository intentionally contains only the API skeleton, a health check, and initial request/data schemas; it does not yet perform matching or recommendations.

## Implemented today

- FastAPI application entry point
- `GET /health` readiness endpoint
- Initial Pydantic `Job` and `UserPreference` schemas
- Local setup and environment examples

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the generated API documentation or request `http://127.0.0.1:8000/health`.

## Roadmap

- [ ] Add job ingestion and persistence
- [ ] Add user preference endpoints
- [ ] Introduce PostgreSQL and pgvector
- [ ] Add embeddings and semantic retrieval
- [ ] Add transparent ranking and recommendation logic
- [ ] Add automated tests and deployment configuration

The roadmap describes planned work, not currently available features.
