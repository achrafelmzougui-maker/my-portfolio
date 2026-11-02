# Reproducibility and portfolio review guide

This guide helps a recruiter or academic supervisor distinguish runnable code, educational reconstructions, and historical experience.

## Fast review

| Project | Open | What can be verified |
| --- | --- | --- |
| Main portfolio | [Live site](https://achrafelmzougui-maker.github.io/my-portfolio/) | Responsive static site, FR/EN, project links |
| TrafficFlow AI | [Web demo](https://achrafelmzougui-maker.github.io/my-portfolio/trafficflow-ai/) | Synthetic traffic visualization; Python model and API tests in GitHub Actions |
| Smart Attendance | [Web demo](https://achrafelmzougui-maker.github.io/my-portfolio/smart-attendance/) | Fictional manual attendance workflow; no live face recognition |
| Arabic Learning Game | [Web demo](https://achrafelmzougui-maker.github.io/my-portfolio/arabic-learning-game/) | Standalone reconstructed vocabulary quiz |
| NFC Digital Card | [Web demo](https://achrafelmzougui-maker.github.io/my-portfolio/nfc-digital-card/) | Standalone digital card landing page |
| Football Value Predictor | [Python code](../football-value-predictor/) | kNN demonstration on fictional records |
| Prolog Checkers | [Prolog code](../prolog-checkers/) | Simplified rule-based checkers logic |
| Rasa school chatbot | [Separate repository](https://github.com/achrafelmzougui-maker/rasa-chatbot-scolarite) | NLU/rules starter scaffold; not deployed |

## Run local checks

From the repository root:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python football-value-predictor/predict.py --test
```

With SWI-Prolog installed:

```bash
swipl -q -s prolog-checkers/checkers.pl -g run_tests -t halt
```

For TrafficFlow Python/API tests, follow [TrafficFlow README](../trafficflow-ai/README.md) and the [GitHub workflow](../.github/workflows/trafficflow-python-tests.yml).

## What the automated tests mean

- **Portfolio integrity:** local static links, page titles, duplicate IDs and FR/EN controls.
- **Academic demo checks:** Python demo invariants and simplified Prolog rules.
- **TrafficFlow Python tests:** synthetic training and API behavior.

Passing CI is **not** evidence of real-world ML accuracy, accessibility certification, security audit, or deployment of the TrafficFlow backend.

## Publishing rules

Only publish screenshots from running applications, not AI-generated imagery presented as proof. Never commit API keys, personal student records, biometric templates, private customer information, employer-owned code without permission, or unlicensed PDFs.

## Roadmap for PFE applications

1. Capture real screenshots from each functioning demo.
2. Recover authorized original code for historical projects.
3. Document architecture diagrams, requirements, tests and quantitative results.
4. Validate the Rasa starter in a compatible local environment.
5. Deploy TrafficFlow's explicitly synthetic API demo after reviewing hosting costs.
6. Collect authorized traffic data and evaluate a real model before making real-world prediction claims.
