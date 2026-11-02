# ML pipeline — TrafficFlow AI

This folder contains a reproducible **baseline training pipeline**, not a pre-trained model. It does not include a real Kénitra traffic dataset, and no performance metrics are claimed.

## Required CSV

Columns: `timestamp,zone,congestion_index`. Example schema (illustrative values only):

```csv
timestamp,zone,congestion_index
2026-01-05T08:00:00Z,Centre-ville,62
2026-01-05T09:00:00Z,Maâmora,41
```

At least 50 observations required. These example rows are **not real measurements**. Obtain a dataset with explicit usage rights and documented sensor/source, geography, temporal coverage, sampling and limitations. The code validates inputs and performs a chronological 80/20 split (not a random split) and reports MAE, RMSE and a constant-median baseline.

## Run

```bash
pip install -r ../backend/requirements.txt
python train.py --data path/to/licensed_kenitra_traffic.csv
cd ../backend
uvicorn app:app --reload
```

The model file `traffic_model.joblib` is created locally and is intentionally **not committed**. Do not load model files from untrusted sources (joblib uses pickle).

## Limitations

This is an initial baseline; a future evaluation should use genuinely held-out future observations, temporal cross-validation, a stronger baseline, and a clear target definition. Without licensed observational data, the published web page remains a simulation.

## End-to-end demonstration with synthetic data (NOT real traffic)

To verify that the training pipeline and API can work together before obtaining licensed observations:

```bash
# From trafficflow-ai/
python -m pip install -r backend/requirements.txt
python ml/generate_demo_data.py --days 90
python ml/train.py --data ml/demo_synthetic.csv --synthetic
python -m uvicorn backend.app:app --reload
```

Then visit `http://127.0.0.1:8000/docs` and submit:

```json
{"zone":"Centre-ville","hour":8,"day_of_week":0}
```

**Critical:** the generator uses a predefined mathematical pattern and random noise. Any ML metrics computed on this data only measure how well a model learns that *artificial* pattern. They do **not** measure Kénitra traffic forecasting quality. The generated CSV and trained model are local-only and ignored by Git. The browser-based GitHub Pages client needs a separately deployed HTTPS API and allowed CORS origin; it cannot reach your local localhost API from another device.

Training writes a sibling `traffic_model.metadata.json` with the evaluation metrics and an explicit synthetic flag. Treat this metadata as a self-declaration, not independent evidence of dataset provenance.
