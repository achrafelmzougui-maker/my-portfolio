# Achraf El Mzougui — Portfolio

Portfolio professionnel en français, basé sur le CV d'Achraf El Mzougui (Master 2 ISI, Université Ibn Tofail).

## Fonctionnalités
- Interface dark moderne et responsive
- Animations légères avec respect de la préférence « réduire les animations »
- Présentation, compétences, projets, expériences, formation et contact
- HTML, CSS et JavaScript natifs : aucun build, aucune dépendance npm
- Liens e-mail, LinkedIn et GitHub

## Prévisualisation
Ouvrir `index.html` dans un navigateur, ou activer GitHub Pages via **Settings → Pages → Deploy from a branch → main / (root)**.

## À compléter
- Ajouter un PDF du CV et un bouton de téléchargement si souhaité.
- Ajouter des captures d'écran et liens vérifiés vers les projets.
- Ajouter une photo professionnelle si souhaité.

Les informations de parcours sont reprises du CV fourni. Aucun lien de projet ni réalisation non confirmée n'a été inventé.


## Catalogue complet des projets

Consultez [PROJECT_CATALOG.md](PROJECT_CATALOG.md) pour les projets, les technologies, les preuves disponibles et les limites de chaque démo.

### Démonstrations et code

- [TrafficFlow AI](trafficflow-ai/) — PWA, API FastAPI et prototype mobile; données synthétiques uniquement pour les démos.
- [Smart Attendance](smart-attendance/) — démonstration web de suivi manuel de présence avec étudiants fictifs.
- [Football Value Predictor](football-value-predictor/) — nouvelle démo Python, données fictives.
- [Jeu de dames Prolog](prolog-checkers/) — nouvelles règles simplifiées, code Prolog.
- [Jeu éducatif arabe](arabic-learning-game/) — nouvelle mini-démo web, distincte du projet JavaFX original.
- [Carte NFC](nfc-digital-card/) — nouvelle landing page démo.
- [Rasa Chatbot Scolarité](https://github.com/achrafelmzougui-maker/rasa-chatbot-scolarite) — scaffold de chatbot FAQ, dépôt séparé.

### Rapports

- [Rapport de synthèse](docs/PROJECTS_REPORT.md)
- [Catalogue et statut des sources](PROJECT_CATALOG.md)

**Transparence :** plusieurs projets historiques (LV Manager, stock VB.NET, e-commerce PHP, bibliothèque PDF, site de location) sont documentés dans le catalogue, mais leurs sources originales ne sont pas disponibles ici. Les reconstructions ne sont pas présentées comme des copies de ces projets.

## Validation continue

[![TrafficFlow Python tests](https://github.com/achrafelmzougui-maker/my-portfolio/actions/workflows/trafficflow-python-tests.yml/badge.svg)](https://github.com/achrafelmzougui-maker/my-portfolio/actions/workflows/trafficflow-python-tests.yml)
[![Academic demo checks](https://github.com/achrafelmzougui-maker/my-portfolio/actions/workflows/academic-demos.yml/badge.svg)](https://github.com/achrafelmzougui-maker/my-portfolio/actions/workflows/academic-demos.yml)

Les workflows GitHub Actions vérifient le pipeline Python de TrafficFlow (données **synthétiques**, API et tests) et les nouvelles démos Python/Prolog. Les badges affichent le statut GitHub actuel; ils ne prouvent pas une validation sur données réelles, ni un déploiement du backend.
