"""Train a reproducible regression baseline on a user-provided, licensed CSV.

Expected columns: timestamp (ISO 8601), zone, congestion_index (0..100).
Rows must be real observations for meaningful evaluation.
"""
import argparse
import json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

HERE = Path(__file__).resolve().parent
ZONES = {"Centre-ville", "Maâmora", "Bir Rami", "Mimosas"}

def train(input_path: Path, output_path: Path):
    data = pd.read_csv(input_path)
    required = {"timestamp", "zone", "congestion_index"}
    if not required.issubset(data.columns):
        raise ValueError(f"CSV missing columns: {sorted(required - set(data.columns))}")
    data["timestamp"] = pd.to_datetime(data["timestamp"], utc=True, errors="raise")
    data["congestion_index"] = pd.to_numeric(data["congestion_index"], errors="raise")
    if data["congestion_index"].isna().any() or not data["congestion_index"].between(0, 100).all():
        raise ValueError("congestion_index must be between 0 and 100")
    if not set(data["zone"]).issubset(ZONES):
        raise ValueError("Unknown zone. Check supported Kénitra zones.")
    data = data.sort_values("timestamp").reset_index(drop=True)
    if len(data) < 50:
        raise ValueError("At least 50 observations required for this baseline.")
    data["hour"] = data["timestamp"].dt.hour
    data["day_of_week"] = data["timestamp"].dt.dayofweek
    cut = int(len(data) * .8)
    train_df, test_df = data.iloc[:cut], data.iloc[cut:]
    xcols = ["zone", "hour", "day_of_week"]
    pipeline = Pipeline([
        ("features", ColumnTransformer([
            ("zone", OneHotEncoder(handle_unknown="ignore"), ["zone"]),
            ("numeric", "passthrough", ["hour", "day_of_week"])
        ])),
        ("model", RandomForestRegressor(n_estimators=120, min_samples_leaf=3,
                                         random_state=42, n_jobs=-1))
    ])
    pipeline.fit(train_df[xcols], train_df["congestion_index"])
    predicted = pipeline.predict(test_df[xcols])
    metrics = {
        "dataset_type": "user_supplied_verify_provenance",
        "rows": len(data), "train_rows": len(train_df), "test_rows": len(test_df),
        "split": "chronological_80_20",
        "mae": round(float(mean_absolute_error(test_df["congestion_index"], predicted)), 4),
        "rmse": round(float(mean_squared_error(test_df["congestion_index"], predicted) ** .5), 4),
        "baseline_mae": round(float(mean_absolute_error(
            test_df["congestion_index"],
            [train_df["congestion_index"].median()] * len(test_df))), 4),
        "note": "Evaluate on a separate future period before claiming real-world accuracy."
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_path)
    print(json.dumps(metrics, indent=2))
    return metrics

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=HERE / "traffic_model.joblib")
    args = parser.parse_args()
    train(args.data, args.output)
