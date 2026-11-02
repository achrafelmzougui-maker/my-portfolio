# TrafficFlow AI — Android and iOS prototype

A React Native / Expo mobile interface for the Kénitra pilot. It supports the same four zones and a transparent **synthetic simulation mode**.

## Getting started

Install Node.js and npm, then from this folder:

```bash
npm install
npx expo start
```

Scan the development QR code with Expo Go on a compatible device, or use a configured Android/iOS simulator. Exact Expo Go support depends on the installed SDK version; align packages with `npx expo install --fix` if prompted.

## API integration

Set `API_URL` at the top of `App.js` to a deployed **HTTPS** FastAPI URL. The app sends `POST /predict` with zone, hour and weekday index. The current UI offers only a weekday/weekend choice, mapping to Monday or Saturday; replace with a real calendar selector before production. If API requests fail, an error is shown instead of silently displaying simulated predictions.

## Important

- This is **source code only**, not an APK, App Store release or verified iOS build.
- GitHub Pages hosts the browser demo, not this native mobile app.
- No location permission, live traffic feed or background tracking is used.
- All default simulation scores are synthetic and should not guide driving decisions.
- Building iOS apps for distribution requires Apple's platform tooling and developer account requirements.
