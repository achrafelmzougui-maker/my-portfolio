"""Unit tests for data validation. Tests do not require real traffic data."""
import tempfile
from pathlib import Path
import pandas as pd
import pytest
from train import train

def test_missing_required_column():
    with tempfile.TemporaryDirectory() as directory:
        csv_path = Path(directory) / "input.csv"
        pd.DataFrame({"zone": ["Centre-ville"], "congestion_index": [50]}).to_csv(csv_path, index=False)
        with pytest.raises(ValueError, match="missing columns"):
            train(csv_path, Path(directory) / "model.joblib")

def test_reject_out_of_range_target():
    with tempfile.TemporaryDirectory() as directory:
        csv_path = Path(directory) / "input.csv"
        pd.DataFrame({"timestamp": ["2026-01-01T00:00:00Z"],
                      "zone": ["Centre-ville"], "congestion_index": [101]}).to_csv(csv_path, index=False)
        with pytest.raises(ValueError, match="between 0 and 100"):
            train(csv_path, Path(directory) / "model.joblib")

def test_reject_small_dataset():
    with tempfile.TemporaryDirectory() as directory:
        csv_path = Path(directory) / "input.csv"
        pd.DataFrame({"timestamp": ["2026-01-01T00:00:00Z"],
                      "zone": ["Centre-ville"], "congestion_index": [42]}).to_csv(csv_path, index=False)
        with pytest.raises(ValueError, match="At least 50"):
            train(csv_path, Path(directory) / "model.joblib")

def test_timezone_metadata(tmp_path):
    from generate_demo_data import generate
    csv_file = tmp_path / 'demo.csv'
    model_file = tmp_path / 'model.joblib'
    generate(csv_file, days=4)
    metrics = train(csv_file, model_file, synthetic=True)
    assert metrics['feature_timezone'] == 'Africa/Casablanca'
