FROM python:3.12

# TODO: split build into multiple stages

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY gunicorn.conf.py /app/
COPY board /app/board

# for configurability
ENV SERVICE_PORT=8000
ENV NETWORK_INTERFACE="0.0.0.0"
ENV WORKERS=4

EXPOSE ${SERVICE_PORT}

# TODO: investigate these errors:
#   [CRITICAL] WORKER TIMEOUT (pid:9)
#   [ERROR] Error handling request (no URI read)
#   [ERROR] Worker (pid:9) was sent SIGKILL! Perhaps out of memory?
# Happens when the image is run on Docker Desktop, but not when it's run in WSL directly.
# So, it seems on real VMs it should work fine.

WORKDIR /app
ENTRYPOINT [ \
    "sh", \
    "-c", \
    "gunicorn --config=gunicorn.conf.py \
    --workers=${WORKERS} \
    --bind=${NETWORK_INTERFACE}:${SERVICE_PORT} \
    'board:create_app()' \
    --access-logfile - --error-logfile -" \
]
