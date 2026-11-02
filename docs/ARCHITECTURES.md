# Architectures des prototypes — Master ISI

> Les diagrammes ci-dessous décrivent les prototypes **présents dans ces dépôts**, et non des architectures de production. Ils ne prouvent pas que des services externes sont déployés.

## 1. TrafficFlow AI — prototype à données synthétiques

```mermaid
flowchart TD
  A[Script de génération de données synthétiques] --> B[Jeu de données de démonstration]
  B --> C[Entraînement Python Random Forest]
  C --> D[Artefact modèle et métadonnées]
  D --> E[API FastAPI locale ou déployable]
  F[Dashboard web GitHub Pages] --> G[Simulation horaire intégrée]
  F -. Endpoint configuré facultatif .-> E
  H[Prototype mobile Expo] -. Configuration API .-> E
  E --> I[Prédiction numérique]
```

**Vérifiable :** source Python, tests du modèle/API et interface web avec simulation. **Non revendiqué :** données routières temps réel, backend actuellement hébergé, application mobile publiée, précision sur données réelles.

## 2. Smart Attendance — démonstration web

```mermaid
flowchart TD
  A[Utilisateur du navigateur] --> B[Interface de gestion des présences]
  C[Étudiants fictifs] --> B
  B --> D[Statut manuel: présent / absent / retard]
  D --> E[Tableau de bord]
  D --> F[Export CSV]
```

**Important :** cette version GitHub Pages n'utilise ni caméra ni reconnaissance faciale. Le prototype Python/OpenCV antérieur doit être récupéré et audité séparément avant toute revendication de détection réelle.

## 3. Chatbot Rasa — dépôt séparé

```mermaid
flowchart LR
  A[Questions administratives exemples] --> B[data/nlu.yml]
  B --> C[Pipeline Rasa NLU]
  D[data/rules.yml] --> E[Gestion du dialogue]
  C --> E
  F[domain.yml: réponses] --> E
  E --> G[Réponse FAQ]
```

**Vérifiable :** fichiers de configuration et scénarios de test. **Non revendiqué :** modèle entraîné, données officielles d'une école, intégration avec un système scolaire, déploiement public.

## 4. Football Value Predictor — reconstruction pédagogique

```mermaid
flowchart LR
  A[12 exemples fictifs CSV] --> B[Normalisation / distance]
  C[Âge, buts, passes, minutes] --> B
  B --> D[k plus proches voisins]
  D --> E[Estimation pédagogique]
```

Ce prototype n'est pas un modèle de valorisation professionnelle; ses données fictives ne permettent pas de mesurer une performance de marché.

## 5. Jeu de dames Prolog — règles simplifiées

```mermaid
flowchart LR
  A[Plateau 8x8] --> B[Prédicats de validation]
  B --> C[Déplacements simples]
  B --> D[Captures]
  C --> E[Tests PlUnit]
  D --> E
```

Le jeu ne couvre pas toutes les règles des dames internationales.

## Recommandations pour la soutenance

Pour chaque projet, présenter **problème → architecture → implémentation → démonstration → tests → limites → perspectives**. Ajouter de vraies captures d'écran uniquement après avoir exécuté l'application. Éviter toute capture simulée présentée comme une preuve de fonctionnement.
