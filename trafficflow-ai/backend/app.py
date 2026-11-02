"""TrafficFlow AI API. Requires an explicitly trained and saved model."""
import os
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
app = FastAPI(title="TrafficFlow AI", version="0.2.0",
              description="Experimental traffic-congestion prediction API. No live traffic data.")
# Set CORS_ORIGINS to an explicit comma-separated allowlist of trusted web origins.
# Example: https://achrafelmzougui-maker.github.io
origins = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",") if origin.strip()]
if origins:
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["GET", "POST"], allow_headers=["Content-Type"])
model = None

@app.on_event("startup")
def load_model():
    global model
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)

class PredictionRequest(BaseModel):
    zone: Literal["Centre-ville", "Maâmora", "Bir Rami", "Mimosas"]
    hour: int = Field(ge=0, le=23)
    day_of_week: int = Field(ge=0, le=6, description="Monday=0, Sunday=6")

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None,
            "live_traffic": False, "city": "Kénitra"}

@app.post("/predict")
def predict(request: PredictionRequest):
    if model is None:
        raise HTTPException(status_code=503,
                            detail="No trained model installed. Train on an authorized dataset first.")
    features = pd.DataFrame([request.model_dump()])
    value = float(model.predict(features)[0])
    score = round(max(0.0, min(100.0, value)), 1)
    return {"city": "Kénitra", "zone": request.zone, "hour": request.hour,
            "day_of_week": request.day_of_week, "congestion_index": score,
            "level": "high" if score >= 68 else "medium" if score >= 40 else "low",
            "source": "trained_model", "live_traffic": False,
            "warning": "Experimental estimate; not suitable for navigation decisions."}
