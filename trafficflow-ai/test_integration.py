"""End-to-end integration smoke test using synthetic data only.

This checks software integration, NOT traffic prediction accuracy.
"""
from pathlib import Path
import sys

import joblib
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "ml"))
sys.path.insert(0, str(ROOT / "backend"))

from generate_demo_data import generate
from train import train
import app as api


def test_synthetic_training_to_api(tmp_path: Path):
    csv_file = tmp_path / "synthetic.csv"
    model_file = tmp_path / "model.joblib"

    generate(csv_file, days=14, seed=42)
    metrics = train(csv_file, model_file, synthetic=True)

    assert model_file.exists()
    assert metrics["rows"] == 14 * 24 * 4
    assert metrics["mae"] >= 0
    assert metrics["rmse"] >= 0
    assert metrics["baseline_mae"] >= 0

    previous_metadata = api.model_metadata
    previous = api.model
    try:
        # The model is produced in this same test, not loaded from an untrusted source.
        api.model = joblib.load(model_file)
        api.model_metadata = metrics
        client = TestClient(api.app)
        health = client.get("/health")
        assert health.status_code == 200
        assert health.json()["model_loaded"] is True
        assert health.json()["live_traffic"] is False

        prediction = client.post("/predict", json={
            "zone": "Centre-ville",
            "hour": 8,
            "day_of_week": 0,
        })
        assert prediction.status_code == 200
        body = prediction.json()
        assert 0 <= body["congestion_index"] <= 100
        assert body["source"] == "trained_model"
        assert body["synthetic_training_data"] is True
        assert body["dataset_verified"] is False
        assert body["dataset_type"] == "synthetic_demo"
        assert body["live_traffic"] is False
        assert body["level"] in {"low", "medium", "high"}
    finally:
        api.model = previous
        api.model_metadata = previous_metadata

def test_unverified_model_is_not_mislabeled_as_verified(tmp_path: Path):
    csv_file = tmp_path / "synthetic.csv"
    model_file = tmp_path / "model.joblib"
    generate(csv_file, days=14, seed=5)
    # Deliberately omit the --synthetic flag to simulate unknown provenance.
    metrics = train(csv_file, model_file)
    previous_model, previous_metadata = api.model, api.model_metadata
    try:
        api.model = joblib.load(model_file)
        api.model_metadata = metrics
        response = TestClient(api.app).post("/predict", json={
            "zone": "Maâmora", "hour": 17, "day_of_week": 2
        })
        assert response.status_code == 200
        body = response.json()
        assert body["dataset_type"] == "user_supplied_unverified"
        assert body["dataset_verified"] is False
        assert "unverified" in body["warning"].lower()
    finally:
        api.model, api.model_metadata = previous_model, previous_metadata
