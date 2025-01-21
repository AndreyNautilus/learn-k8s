import os
from flask import Flask

from board import backend
from board import stress

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    print(f"db url: {app.config["DATABASE_URL"]}")
    print(f"db port: {app.config["DATABASE_PORT"]}")
    print(f"db name: {app.config["DATABASE_NAME"]}")
    print(f"db username: {app.config["DATABASE_USERNAME"]}")
    print(f"db password: {app.config["DATABASE_PASSWORD"]}")

    if not app.config["DATABASE_PORT"].isnumeric():
        raise RuntimeError("DATABASE_PORT must be numeric")

    app.config["DATABASE_PORT"] = int(app.config["DATABASE_PORT"])

    app.register_blueprint(backend.backend_bp)
    app.register_blueprint(stress.stress_bp)

    return app
