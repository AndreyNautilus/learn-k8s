# Web app

- **frontend-vue** serves html pages
- **backend** handles the logic

## Run via docker-compose

```bash
docker-compose watch
# or
docker-compose up --build

# and at the end
docker-compose down  # or Ctrl+C
```

Double Ctrl+C to force-"down" the compose.

Compose runs NGINX as reverse proxy to route traffic (see config file).

## Run containers manually

The setup can't be easily run locally, because in manual mode there's no traffic routing.
