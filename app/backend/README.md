# Backend

Written in python using [flask](https://flask.palletsprojects.com/en/3.0.x/).
[Exposed via](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/) `gunicorn`.

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # activate the venv
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

## Local runs

Running the app (win):

```bash
$env:WORKER_NAME="local_dev"; python -m flask --app=board run --port=8001 --debug
```

or (linux):

```bash
WORKER_NAME="local_dev" python -m flask --app=board run --port=8001 --debug
```

## Docker

Build:

```bash
# using raw docker
docker build -t app-backend:1.0.0 .
# using Docker BuildX (env can be omitted when using default version)
$env:BACKEND_VERSION="1.0.1"; docker buildx bake --load
```

Run:

```bash
docker run --rm -it -p 8001:8000/tcp --name backend -e WORKER_NAME="local_dev" app-backend:1.0.0
```

## Tests

win:

```bash
$env:PROMETHEUS_MULTIPROC_DIR=$env:temp; pytest -v
```

## Metrics

Using [prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter).
Exposed on `/metrics` endpoint.
