"""Generate clearly labeled SYNTHETIC observations for end-to-end pipeline testing.

This dataset is NOT real Kénitra traffic and must never be used to claim
real-world prediction accuracy. Do not publish metrics as real performance.
"""
import argparse
import csv
import math
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

ZONES = {"Centre-ville": 14, "Maâmora": 5, "Bir Rami": 10, "Mimosas": 7}

def generate(output: Path, days: int = 90, seed: int = 42):
    if days < 1 or days > 3650:
        raise ValueError("days must be between 1 and 3650")
    rng = random.Random(seed)
    output.parent.mkdir(parents=True, exist_ok=True)
    start = datetime(2025, 1, 1, tzinfo=timezone.utc)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "zone", "congestion_index"])
        for d in range(days):
            for hour in range(24):
                timestamp = start + timedelta(days=d, hours=hour)
                weekend = timestamp.weekday() >= 5
                morning = math.exp(-((hour - 8) / 2.1) ** 2) * 43
                evening = math.exp(-((hour - 18) / 2.6) ** 2) * 46
                for zone, offset in ZONES.items():
                    value = (18 + morning + evening + offset) * (0.64 if weekend else 1)
                    value = round(min(100, max(0, value + rng.gauss(0, 6))), 1)
                    writer.writerow([timestamp.isoformat(), zone, value])
    print(f"Created SYNTHETIC dataset: {output} ({days * 24 * len(ZONES)} rows)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "demo_synthetic.csv")
    parser.add_argument("--days", type=int, default=90)
    args = parser.parse_args()
    generate(args.output, args.days)
