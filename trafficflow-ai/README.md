# TrafficFlow AI — Kénitra pilot

A responsive **web concept demo** for a future smart-traffic forecasting system covering Kénitra, Morocco.

## Live demo
https://achrafelmzougui-maker.github.io/my-portfolio/trafficflow-ai/

## Current state
- Responsive traffic dashboard, illustrative schematic and simulated hourly chart
- Selectable Kénitra neighborhoods, time and weekday/weekend scenario
- Fully client-side; no personal data collected
- **Important:** synthetic rule-based scores, not real traffic observations or trained machine-learning predictions. Neighborhood positions are schematic, not geographic coordinates.

## Roadmap
1. Identify licensed, reliable local traffic data and document provenance.
2. Establish baseline and time-aware train/validation/test split; evaluate MAE and calibration as applicable.
3. Train scikit-learn models and publish reproducible notebooks and metrics.
4. Expose predictions with a Python FastAPI backend.
5. Build Android and iOS clients using React Native / Expo.
6. Deploy web, API and mobile distribution separately; GitHub Pages hosts only static frontend.

## Structure
The current GitHub Pages proof of concept is self-contained in `index.html`. Production apps will be split into `web/`, `mobile/`, `backend/`, and `ml/` once data and backend requirements are established.
