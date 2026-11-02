# Technical report — Football Value Predictor

**Status:** newly reconstructed educational demo; fictional observations only.

## Problem
Explore whether a small set of player-season statistics can be mapped to an illustrative market-value estimate.

## Data
12 manually fabricated rows in `fictional_players.csv`. Columns: age, goals, assists, minutes and illustrative value in EUR millions. No claim of real-player observations.

## Algorithm
Normalized weighted k-nearest neighbors with inverse-distance weights (k=3). A standard-library implementation makes the example reproducible without package installation.

## Evaluation
The included `--test` checks program invariants, not predictive accuracy. A legitimate evaluation requires authorized historical observations, temporal holdout, MAE and comparisons with naive baselines.

## Ethical / scientific limitations
Market values are negotiated estimates; selection bias and changing markets matter. Do not use demo outputs in scouting or financial decisions.

## Future work
Acquire verified data, engineer per-90-minute statistics, compare Random Forest / gradient boosting, and publish reproducible splits.
