# Simple web server in python

Uses `http.server` [library](https://docs.python.org/3/library/http.server.html).
Based on [this tutorial](https://realpython.com/python-http-server/).

## Usage

To run as python script (default port is 8000):
```bash
app-py$ python -B main.py 8000
```

To build to docker image:
```bash
app-py$ docker build -t app-py:1.0.0 .
```

To run docker image:
```bash
app-py$ docker run --rm -p 127.0.0.1:8000:8000/tcp app-py:1.0.0
```

## Testing

```bash
$ curl localhost:8000
Hello world! 07/11/2024, 17:10:48
```