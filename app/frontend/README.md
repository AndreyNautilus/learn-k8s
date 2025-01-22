# Frontend

Written in python using [flask](https://flask.palletsprojects.com/en/3.0.x/).

## Local runs

Running the app (win):

```bash
$env:BACKEND_ENDPOINT="http://localhost:8001"; python -m flask --app=board run --port=8000 --debug
```

## Docker

Build:

```bash
docker build -t app-frontend:1.0.0 .
```

Run:

```bash
docker run --rm -it -p 127.0.0.1:8000:8000/tcp --name backend app-frontend:1.0.0
```

-e BACKEND_ENDPOINT="http://backend:8000/backend"
