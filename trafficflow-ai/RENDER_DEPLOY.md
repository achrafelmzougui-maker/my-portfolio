# TrafficFlow AI — Render deployment (SYNTHETIC DEMO ONLY)

The repository root contains `render.yaml`, a Render Blueprint to build and serve a synthetic demonstration model. **This is NOT real Kénitra traffic and must not be described as a live prediction service.**

## Deploy

1. Log in to Render, select **New → Blueprint**, and connect `achrafelmzougui-maker/my-portfolio`.
2. Review the service configuration, pricing, build command, and environment variables **before approving deployment**. Do not assume a free plan is available.
3. Deploy the blueprint. The build creates a synthetic CSV, trains a Random Forest, and saves the model on the service's build filesystem.
4. Copy the resulting HTTPS service URL from the Render dashboard. **No URL is preconfigured or deployed by this repository.**
5. Check `https://YOUR-SERVICE/health`, `/ready`, and `/model-info`. Confirm `dataset_type: synthetic_demo` and `dataset_verified: false`.
6. On the GitHub Pages dashboard, choose **API expérimentale** and paste the HTTPS service URL. Predictions should be labeled as synthetic, and the adjacent hourly chart remains simulated.

## Configuration

- The allowlisted browser origin is `https://achrafelmzougui-maker.github.io` (CORS origins never include a path).
- `/health` is liveness; `/ready` returns 503 when the model is missing.
- The build command is deliberately explicit about `--synthetic`.
- For production, replace the synthetic data with a licensed, documented, verified dataset and retrain/evaluate appropriately. Never merely change metadata flags to claim verification.
- Service availability, cold starts, costs, and allowed resources depend on Render's current plan.

## Safety and limitations

The model is academic, trained on artificial patterns, and not for route guidance or driving decisions. The app does not fetch live traffic. GitHub Pages hosts only the static frontend; Render hosts the optional API. The mobile Expo client needs its `API_URL` configured separately.
