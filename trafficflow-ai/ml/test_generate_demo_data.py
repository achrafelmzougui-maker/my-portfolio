import csv
from pathlib import Path
from generate_demo_data import generate

def test_generator_has_expected_rows(tmp_path: Path):
    output = tmp_path / "demo.csv"
    generate(output, days=2, seed=7)
    with output.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2 * 24 * 4
    assert all(0 <= float(row["congestion_index"]) <= 100 for row in rows)
    assert set(rows[0]) == {"timestamp", "zone", "congestion_index"}
