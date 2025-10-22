# frontend

Vue3 + Vite + nginx

## Project setup

- install `nodejs` and `npm`
- `npm install` to install all deps;

### Local commands

- `npm run dev` - run local server with hot reload (routes `/api/` requests to `localhost:8001`, see `vite.config.js`);
- `npm run build` - compile the prod;
- `npm run serve` - preview the prod locally;
- `npm run lint` - lint files

### Using local backend

- (optionally) start `DB` container;
- start `backend` container and (optionally) connect it to the `DB` container;

## Docker

Uses `nginx` as webserver.

Build:

```bash
# using raw docker
docker build -t app-frontend-vue:1.0.0 .
# using Docker BuildX (env can be omitted when using default version)
$env:FRONTEND_VERSION="1.0.1"; docker buildx bake --load
```

Run:

```bash
docker run --rm -it -p 127.0.0.1:80:80/tcp --name frontend-vue app-frontend-vue:1.0.0
```
