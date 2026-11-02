# Football Value Predictor — reproducible academic demo

A **newly reconstructed educational prototype** based on an earlier university project idea: estimate football player market value from numeric attributes. **The original project source and real training data have not been recovered.** This version is not an official valuation tool.

## Run
```bash
python3 football-value-predictor/predict.py --age 23 --goals 12 --assists 7 --minutes 2200
python3 football-value-predictor/predict.py --test
```
Requires Python 3.9+; no external dependencies.

## Method
Weighted k-nearest neighbors (k=3), with normalized age, goals, assists and minutes played. The bundled records are **fictional**, and predicted values are synthetic examples in millions of euros, **not actual transfer prices**.

## Limitations
No licensed transfer-market dataset, no independent benchmark, no production model. Features omit contract length, league strength, injuries, position and inflation. Never present the demo's numeric output as a real player's value.

## Next steps
Acquire authorized, dated player-season observations; add player position, league, season and contract information; compare against baseline; validate using a chronological split and MAE.
