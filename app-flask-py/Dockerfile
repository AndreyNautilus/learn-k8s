FROM python:3.12

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY board /app/board

# for configurability
ENV SERVICE_PORT=8000
ENV NETWORK_INTERFACE="0.0.0.0"

EXPOSE ${SERVICE_PORT}

# TODO: switch to Production WSGI server (gunicorn or something else?)
# See: https://flask.palletsprojects.com/en/3.0.x/deploying/

# shell form of entrypoint
ENTRYPOINT [ "sh", "-c", "python -m flask --app /app/board run --host ${NETWORK_INTERFACE} --port ${SERVICE_PORT}" ]
