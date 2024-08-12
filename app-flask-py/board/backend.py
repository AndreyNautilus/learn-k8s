from flask import Blueprint, current_app
from datetime import datetime

backend_bp = Blueprint("backend", __name__, url_prefix="/backend")


@backend_bp.route("/time", methods=("GET",))
def time():
    msg = datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
    return {
        'time': msg,
        'worker': current_app.config["WORKER_NAME"]
    }


@backend_bp.route("/crash")
def crash():
    raise RuntimeError("Requested crash")
    return "crash"
