# TrafficFlow API (FastAPI)

Run from this folder after installing dependencies:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

- `GET /health` — reports whether a trained model exists.
- `POST /predict` — request JSON: `{"zone":"Centre-ville","hour":8,"day_of_week":0}`.
- Returns **503** until a trained model is available; this is intentional, to avoid fabricating AI predictions.
- Not a live traffic or routing service. Do not use for safety-critical driving decisions.

GitHub Pages cannot run this Python backend. Production deployment requires separate backend hosting, access control and validation.
