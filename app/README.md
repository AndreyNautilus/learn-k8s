# Web app

- **frontend** serves html pages
- **backend** handles the logic

## Run via docker-compose

```bash
docker-compose watch
# or
docker-compose up --build

# and at the end
docker-compose down
```

Double Ctrl+C to "down" the compose.

## Run containers manually

Run frontend and backend in the same network and configure communication via container name.

Create a user-defined bridge docker network (default bridge network does allow communication by container name):

```bash
docker network create --driver bridge "my-bridge"
docker network ls
```

Start containers in this network:

```bash
docker run --rm -it -p 127.0.0.1:8001:8001/tcp --network=my-bridge --name backend -e SERVICE_PORT=8001 -e WORKER_NAME="local_dev" app-backend:1.0.0
docker run --rm -it -p 127.0.0.1:8000:8000/tcp --network=my-bridge --name frontend -e BACKEND_ENDPOINT="http://backend:8001" app-frontend:1.0.0
docker ps
```

(note the 8001 port in `BACKEND_ENDPOINT` envvar)

Test (from host):

```bash
curl localhost:8001  # backend
curl localhost:8000  # frontend
```

returns a page with time on local_dev.
