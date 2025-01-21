# Backend

Written in python using [flask](https://flask.palletsprojects.com/en/3.0.x/).

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
docker build -t app-backend:1.0.0 .
```

Run:
```bash
docker run --rm -it -p 127.0.0.1:8001:8000/tcp --name backend -e WORKER_NAME="local_dev" app-backend:1.0.0
```

## Tests

`pytest` will run all tests.
