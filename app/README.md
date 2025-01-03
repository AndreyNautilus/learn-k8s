# Web app

- **frontend** serves html pages
- **backend** handles the logic

## Single container with localhost backend endpoint

Start a single container that operates and both frontend and backend. Frontend requests localhost for backend.

```bash
docker run --rm -p 127.0.0.1:8005:8000/tcp -e WORKER_NAME="same" -e BACKEND_ENDPOINT="http://localhost:8000/backend/time" app-flask-py:1.0.0
curl localhost:8005
```

## 2 containers in the same network

Run frontend and backend as separate containers in the same network and configure communication via contianer name.

Create a user-defined bridge docker network (default bridge network does allow communication by container name):
```bash
docker network create --driver bridge "my-bridge"
docker network ls
```

Start containers in this network:
```bash
docker run --rm -p 127.0.0.1:8007:8000/tcp --network="my-bridge" --name backend -e WORKER_NAME="local_dev" app-flask-py:1.0.0
docker run --rm -p 127.0.0.1:8005:8000/tcp --network="my-bridge" --name frontend -e BACKEND_ENDPOINT="http://backend:8000/backend/time" app-flask-py:1.0.0
docker ps
```

Test:
```bash
curl localhost:8005
```
returns a page with time on local_dev.
