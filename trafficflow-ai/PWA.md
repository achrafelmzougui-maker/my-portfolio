# TrafficFlow AI — Installable Web App (PWA)

The GitHub Pages prototype includes a web manifest, SVG icon and service worker for **offline access to the static simulation UI**. No API responses are cached. This is not a native iOS or Android binary.

## Try on Android

Open https://achrafelmzougui-maker.github.io/my-portfolio/trafficflow-ai/ in Chrome and use **Install app** or **Add to Home screen** if offered.

## Try on iPhone

Open the same URL in Safari and use **Share → Add to Home Screen**. Browser/OS support varies.

## Offline behavior

After the first successful visit, the static demo can load from cache while offline. Predictions from a remote API require an active network connection; the demo never silently substitutes a synthetic score for a failed API prediction.

## Limitations

SVG-only icons may not be supported by all install prompts. For broad production compatibility, add generated 192px and 512px PNG icons and an Apple touch icon, and validate on actual devices. The web PWA is not equivalent to an App Store or Google Play release.
