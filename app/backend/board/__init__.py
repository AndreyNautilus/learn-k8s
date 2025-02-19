from flask import Flask

from board import backend
from board import stress
from board.metrics import metrics, metric_count_by_path


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    if not app.config["DATABASE_PORT"].isnumeric():
        raise RuntimeError("DATABASE_PORT must be numeric")

    app.config["DATABASE_PORT"] = int(app.config["DATABASE_PORT"])

    app.register_blueprint(backend.backend_bp)
    app.register_blueprint(stress.stress_bp)

    metrics.register_default(metric_count_by_path, app=app)
    metrics.init_app(app)

    return app
