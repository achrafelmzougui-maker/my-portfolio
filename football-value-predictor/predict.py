"""Educational player-value estimator trained ONLY on fictional examples."""
import argparse
import csv
import math
from pathlib import Path

DATA = Path(__file__).with_name("fictional_players.csv")
FIELDS = ("age", "goals", "assists", "minutes")
SCALES = {"age": 15.0, "goals": 35.0, "assists": 20.0, "minutes": 3500.0}

def read_examples(path=DATA):
    with open(path, newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError("No training examples")
    return [{key: float(row[key]) for key in (*FIELDS, "value_m_eur")} for row in rows]

def estimate(features, examples=None, k=3):
    examples = examples if examples is not None else read_examples()
    if any(not math.isfinite(float(features[f])) or float(features[f]) < 0 for f in FIELDS):
        raise ValueError("Features must be finite and nonnegative")
    distances = sorted(
        (math.sqrt(sum(((float(features[f]) - item[f]) / SCALES[f]) ** 2 for f in FIELDS)), item["value_m_eur"])
        for item in examples
    )
    neighbors = distances[:min(k, len(distances))]
    exact = [value for distance, value in neighbors if distance == 0]
    if exact:
        return sum(exact) / len(exact)
    weights = [(1 / max(distance, 1e-9), value) for distance, value in neighbors]
    return sum(weight * value for weight, value in weights) / sum(weight for weight, _ in weights)

def self_test():
    examples = read_examples()
    for example in examples:
        prediction = estimate(example, examples)
        assert math.isfinite(prediction) and prediction >= 0
    assert estimate(examples[0], [examples[0]]) == examples[0]["value_m_eur"]
    print("Demo checks passed (NOT model validation).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fictional football market-value demo")
    for name in FIELDS:
        parser.add_argument("--" + name, type=float)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        self_test()
    else:
        values = vars(args)
        if any(values[name] is None for name in FIELDS):
            parser.error("Provide --age, --goals, --assists and --minutes")
        result = estimate(values)
        print(f"SYNTHETIC demo estimate: {result:.2f} million EUR (NOT a real market valuation)")
