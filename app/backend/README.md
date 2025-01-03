# Backend

Written in python using [flask](https://flask.palletsprojects.com/en/3.0.x/).

Running the app (win):
```bash
$env:WORKER_NAME="local_dev"; python -m flask --app=board run --port=8001 --debug
```
or (linux):
```bash
WORKER_NAME="local_dev" python -m flask --app=board run --port=8001 --debug
```

