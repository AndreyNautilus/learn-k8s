FROM python:3.12

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY board /app/board

EXPOSE 8000

# TODO: switch to Production WSGI server (gunicorn or something else?)
# See: https://flask.palletsprojects.com/en/3.0.x/deploying/

# Not CMD to accept parameters
ENTRYPOINT [ "python", "-m", "flask", "--app", "/app/board", "run", "--host", "0.0.0.0", "--port", "8000" ]
