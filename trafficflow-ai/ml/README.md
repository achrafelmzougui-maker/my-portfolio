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
