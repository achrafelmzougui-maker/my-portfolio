# TrafficFlow AI — deployment guide (experimental)

## Status

The backend is not deployed yet. This guide packages the API for local/container hosting. **Without an authorized trained model, POST /predict intentionally returns HTTP 503.** The public GitHub Pages demo still uses synthetic scenarios by default.

## Local Python

From `trafficflow-ai/`:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r backend/requirements.txt
python -m uvicorn backend.app:app --reload
```

Open http://127.0.0.1:8000/docs and http://127.0.0.1:8000/health.

## Docker

From `trafficflow-ai/`:

```bash
docker build -t trafficflow-api .
docker run --rm -p 8000:8000 -e CORS_ORIGINS=https://achrafelmzougui-maker.github.io trafficflow-api
```

Open http://localhost:8000/health. If a licensed dataset has been used to train a model, put the trusted model artifact at `ml/traffic_model.joblib` before building, or mount the file read-only into the container. **Never load untrusted joblib/pickle files.**

## Hosting checklist

1. Select a hosting provider with Python/Docker support; GitHub Pages cannot execute FastAPI.
2. Deploy over HTTPS, configure health check `/health`, and use the host's secrets/config for environment variables.
3. Set `CORS_ORIGINS=https://achrafelmzougui-maker.github.io` (no trailing slash).
4. Configure an API URL in the web demo's **API expérimentale** mode. For the mobile starter, set `API_URL` in `mobile/App.js` to the deployed HTTPS endpoint.
5. Confirm `/health` and `/predict` behavior, error handling, network timeouts, and metrics.
6. Before public deployment, add rate limits, observability, resource limits, dependency security checks, and a clear model provenance statement.

**Do not advertise real-time traffic or accuracy until there is suitable real data and independent validation.**
