import os
from flask import Flask

from board import pages


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(pages.pages_bp)

    return app
