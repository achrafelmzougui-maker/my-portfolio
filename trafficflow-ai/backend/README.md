# TrafficFlow API (FastAPI)

Run from this folder after installing dependencies:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

- `GET /health` — liveness check (HTTP 200 even if no model is loaded).
- `GET /ready` — readiness check (HTTP 503 if no trained model is loaded).
- `GET /model-info` — model provenance and evaluation metadata, or explicit unknown fields if unavailable. Metadata is not independent verification of data quality.
- `POST /predict` — request JSON: `{"zone":"Centre-ville","hour":8,"day_of_week":0}`.
- Returns **503** until a trained model is available; this is intentional, to avoid fabricating AI predictions.
- Not a live traffic or routing service. Do not use for safety-critical driving decisions.

GitHub Pages cannot run this Python backend. Production deployment requires separate backend hosting, access control and validation.

## Deployment health checks

Use `/health` for process liveness. Use `/ready` when the hosting platform must know whether the prediction service is usable. A deployment without a trained model will intentionally fail readiness. `/model-info` helps debug provenance without returning training records.

From the `trafficflow-ai/backend` directory, run tests with `python -m pytest -q test_app.py` after installing `pytest httpx`.
