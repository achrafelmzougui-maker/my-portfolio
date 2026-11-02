# TrafficFlow AI — end-to-end integration test

The test `test_integration.py` checks that the software pipeline works from a synthetic CSV through training, model loading, FastAPI health and prediction endpoints.

## Run locally

From `trafficflow-ai/`:

```bash
python -m pip install -r backend/requirements.txt pytest httpx
python -m pytest -q test_integration.py
```

The test marks generated data as `synthetic_demo` and checks that the API exposes `synthetic_training_data: true`. It creates temporary data and model files, so it does not modify the deployed website or save a model to the repository. It checks API contract and integration, **not real-world model quality**.

## CI

The repository workflow `.github/workflows/trafficflow-python-tests.yml` also runs the integration test on supported pushes and pull requests. Check GitHub Actions for actual pass/fail status; committed test code alone does not establish a passing build.

## Still required for production

- Authorized Kénitra measurements with a clearly defined target.
- Out-of-time validation on real observations.
- Hosting the backend over HTTPS with resource limits and monitoring.
- Testing the web app and mobile client against the deployed API.
