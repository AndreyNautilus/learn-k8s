import os
from flask import Flask

from board import backend

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    app.register_blueprint(backend.backend_bp)
    
    return app
