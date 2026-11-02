# TrafficFlow AI — Kénitra pilot (v0.2)

## Live web concept
https://achrafelmzougui-maker.github.io/my-portfolio/trafficflow-ai/

The published website remains a **responsive, client-side traffic scenario simulator** with synthetic rule-based scores. It is not connected to real traffic measurements or a deployed ML backend.

## Source code now included

- `index.html` — GitHub Pages interactive prototype.
- `ml/train.py` — scikit-learn baseline, input validation, chronological train/test split, MAE/RMSE and median baseline.
- `backend/app.py` — FastAPI health and prediction endpoints; returns HTTP 503 if no trained model is installed rather than inventing results.
- `backend/requirements.txt` — Python dependencies.
- `.gitignore` — excludes local data, models and secrets.

## Run locally

See [ML instructions](ml/README.md) and [API instructions](backend/README.md). No training dataset, model artifact, or validation results are included in this repository yet. A properly licensed and geographically relevant traffic dataset is required for credible predictions.

## Roadmap

1. Source and document a real Kénitra traffic dataset (license, time period, road coverage, collection method).
2. Train and evaluate with held-out future observations and meaningful baselines.
3. Deploy the FastAPI service securely and connect the web interface to the API.
4. Create React Native / Expo Android and iOS apps that share the API.
5. Improve maps using licensed geographic data, accessibility and mobile UX.

## Scope and limitations

The web map is **schematic**, not a georeferenced street map. The web simulation is **not** a real ML prediction. The API is a development scaffold, not a production traffic service. No live navigation or safety-critical decisions should rely on the current version.
