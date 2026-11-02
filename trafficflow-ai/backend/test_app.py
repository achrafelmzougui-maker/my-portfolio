"""Smoke tests for honest API behavior without a trained model."""
from fastapi.testclient import TestClient
import app as service

client = TestClient(service.app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["city"] == "Kénitra"
    assert body["live_traffic"] is False

def test_invalid_hour_rejected():
    response = client.post("/predict", json={
        "zone": "Centre-ville", "hour": 25, "day_of_week": 0
    })
    assert response.status_code == 422

def test_unknown_zone_rejected():
    response = client.post("/predict", json={
        "zone": "Unknown", "hour": 8, "day_of_week": 0
    })
    assert response.status_code == 422

def test_no_model_returns_503():
    old = service.model
    service.model = None
    try:
        response = client.post("/predict", json={
            "zone": "Centre-ville", "hour": 8, "day_of_week": 0
        })
        assert response.status_code == 503
    finally:
        service.model = old

def test_ready_without_model_returns_503():
    previous = service.model
    try:
        service.model = None
        response = client.get("/ready")
        assert response.status_code == 503
    finally:
        service.model = previous


def test_model_info_without_model_is_explicit():
    previous_model, previous_metadata = service.model, service.model_metadata
    try:
        service.model = None
        service.model_metadata = None
        response = client.get("/model-info")
        assert response.status_code == 200
        info = response.json()
        assert info["model_loaded"] is False
        assert info["dataset_verified"] is False
        assert info["dataset_type"] == "unknown"
        assert info["live_traffic"] is False
    finally:
        service.model, service.model_metadata = previous_model, previous_metadata

def test_nonfinite_model_prediction_returns_503():
    class BrokenModel:
        def predict(self, features):
            return [float("nan")]
    previous = service.model
    try:
        service.model = BrokenModel()
        response = client.post("/predict", json={
            "zone": "Centre-ville", "hour": 8, "day_of_week": 0
        })
        assert response.status_code == 503
        assert "invalid prediction" in response.json()["detail"]
    finally:
        service.model = previous


def test_model_reload_resets_stale_state(monkeypatch, tmp_path):
    previous_model, previous_metadata = service.model, service.model_metadata
    try:
        monkeypatch.setattr(service, "MODEL_PATH", tmp_path / "missing.joblib")
        service.model = object()
        service.model_metadata = {"dataset_type": "synthetic_demo"}
        service.load_model()
        assert service.model is None
        assert service.model_metadata is None
    finally:
        service.model, service.model_metadata = previous_model, previous_metadata
