# frontend

Vue3 + Vite

## Project setup

```
npm install
```

### Local commands

- `npm run dev` - run local server with hot reload;
- `npm run build` - compile the prod;
- `npm run serve` - preview the prod locally;
- `npm run lint` - lint files

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## Docker

Build:

```bash
docker build -t app-frontend-vue:1.0.0 .
```

Run:

```bash
docker run --rm -it -p 127.0.0.1:80:80/tcp --name frontend-vue app-frontend-vue:1.0.0
```
