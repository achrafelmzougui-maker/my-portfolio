"""TrafficFlow AI API. Requires an explicitly trained and saved model."""
import os
import json
from pathlib import Path
from typing import Literal
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "ml" / "traffic_model.joblib"
ZONES = ("Centre-ville", "Maâmora", "Bir Rami", "Mimosas")
app = FastAPI(title="TrafficFlow AI", version="1.1.0",
              description="Experimental traffic-congestion prediction API. No live traffic data.")
# Set CORS_ORIGINS to an explicit comma-separated allowlist of trusted web origins.
# Example: https://achrafelmzougui-maker.github.io
origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",") if origin.strip()]
if origins:
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])
model = None
model_metadata = None

@app.on_event("startup")
def load_model():
    global model, model_metadata
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        metadata_path = MODEL_PATH.with_suffix(".metadata.json")
        if metadata_path.exists():
            model_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

class PredictionRequest(BaseModel):
    zone: Literal["Centre-ville", "Maâmora", "Bir Rami", "Mimosas"]
    hour: int = Field(ge=0, le=23)
    day_of_week: int = Field(ge=0, le=6, description="Monday=0, Sunday=6")

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None,
            "live_traffic": False, "city": "Kénitra",
            "dataset_type": model_metadata.get("dataset_type", "unknown") if model_metadata else "unknown"}

@app.get("/ready")
def ready():
    """Deployment readiness: returns 503 until a trained model is loaded."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"ready": True, "live_traffic": False}


@app.get("/model-info")
def model_info():
    """Non-sensitive model provenance; no training rows or filesystem paths."""
    info = model_metadata or {}
    dataset_type = info.get("dataset_type", "unknown")
    return {
        "model_loaded": model is not None,
        "city": "Kénitra",
        "live_traffic": False,
        "dataset_type": dataset_type,
        "dataset_verified": dataset_type == "verified_observations" and info.get("verified") is True,
        "synthetic_training_data": dataset_type == "synthetic_demo",
        "feature_timezone": info.get("feature_timezone", "unknown"),
        "validation_split": info.get("split"),
        "mae": info.get("mae"),
        "rmse": info.get("rmse"),
        "baseline_mae": info.get("baseline_mae"),
        "notice": "Metadata is self-declared, not independent proof of dataset authenticity.",
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=503,
                            detail="No trained model installed. Train on an authorized dataset first.")
    features = pd.DataFrame([request.model_dump()])
    value = float(model.predict(features)[0])
    score = round(max(0.0, min(100.0, value)), 1)
    dataset_type = model_metadata.get("dataset_type", "unknown") if model_metadata else "unknown"
    synthetic = dataset_type == "synthetic_demo"
    verified = dataset_type == "verified_observations" and model_metadata.get("verified") is True if model_metadata else False
    return {"city": "Kénitra", "zone": request.zone, "hour": request.hour,
            "day_of_week": request.day_of_week, "congestion_index": score,
            "level": "high" if score >= 68 else "medium" if score >= 40 else "low",
            "source": "trained_model", "live_traffic": False,
            "synthetic_training_data": synthetic,
            "dataset_verified": verified,
            "dataset_type": dataset_type,
            "warning": ("Synthetic training data; NOT a real-world traffic prediction." if synthetic
                        else "Dataset provenance unverified; NOT a validated traffic prediction." if not verified
                        else "Experimental estimate based on documented data; not for navigation decisions.")}
