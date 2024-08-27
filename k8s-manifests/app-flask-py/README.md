# app-flask manifests

## app-flask.yaml - combined pods

Pods start 2 separate images: for backend and frontend.
Frontend connects to backend via container name.

### Requirements

- `configmap-dev` in `dev` namespace
- `secret-dev` in `dev` namespace

## app-flask-backend/frontend.yaml - separate services

2 separate services for frontend and backend.
