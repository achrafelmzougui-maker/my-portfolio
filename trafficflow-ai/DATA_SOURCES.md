# TrafficFlow AI — data source assessment (Kénitra)

Reviewed 2026-11-02. **No verified open, hourly, neighborhood-level Kénitra congestion dataset has been identified.** Do not label the synthetic dashboard as real-time traffic or validated AI predictions.

| Source | Link | What it contains | Suitability |
|---|---|---|---|
| CNER traffic publications | https://www.cner.ma/portail-applicatif.html | Moroccan national road traffic count publications by year | Useful context; availability of neighborhood-hourly Kénitra measurements not established |
| CNER institution | https://www.cner.ma/ | Road counting and traffic research activities | Potential institution to contact for permission and dataset scope |
| Casablanca traffic research dataset | https://data.mendeley.com/datasets/8hj76bpzpv/1 | Casablanca travel-time index / trajectories; CC BY 4.0 | Useful to prototype a separate **Casablanca** experimental model; cannot be relabeled as Kénitra observations |
| Morocco Transport Starter Data Kit | https://zenodo.org/records/10410212 | Annual nationwide historical transport statistics | Context only; insufficient temporal/spatial resolution for hourly neighborhood congestion |
| Moroccan open-data portal | https://www.data.gov.ma/data/dataset/?groups=finance&tags=transport | National transport indicators | Not an identified hourly Kénitra dataset |

## Requirements for a credible Kénitra training dataset

- Explicit authorization/license to reuse and publish derived results.
- Timestamped road/segment or area-level traffic measurements, with source and sensor methodology.
- Defined target: congestion index, travel time index, or traffic speed; do not conflate these.
- Coverage across weekdays, weekends, seasons and multiple roads in Kénitra.
- Hold out the most recent period for validation; compare with simple historical baselines.
- Assess missing observations, holidays, roadworks, distribution shift and uncertainty.

## Current schema

The existing baseline expects `timestamp,zone,congestion_index` where congestion_index is an **explicitly defined 0–100 target**. No verified data currently matches this exact schema. Converting another dataset to this target requires a justified documented methodology, not invented values.

## Next data acquisition step

Request anonymized aggregated counts / speed or travel time observations from relevant road or mobility stakeholders, with written permission. Do not scrape restricted mapping services or fabricate observations.
