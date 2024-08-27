from flask import Blueprint, current_app, request
from datetime import datetime
import urllib.parse

backend_bp = Blueprint("backend", __name__, url_prefix="/backend")


@backend_bp.route("/time", methods=("GET",))
def time():
    time_msg = datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
    worker = current_app.config["WORKER_NAME"]
    msg = urllib.parse.unquote_plus(request.args.get("msg", "no msg"))
    return {
        'time': time_msg,
        'worker': f"{worker} - {msg}",
        'echo': msg
    }


@backend_bp.route("/crash")
def crash():
    raise RuntimeError("Requested crash")
    return "crash"
