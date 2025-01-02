from flask import Blueprint, current_app, request
from datetime import datetime
import urllib.parse
import math

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


@backend_bp.route("/stress", methods=("Get",))
def stress():
    ticks = int(request.args.get("ticks", 1000000))

    res = 0
    for i in range(ticks):
        res = (res + i * math.sqrt(65) % 17) % 23  # some "heavy" computation

    return f"Done: {res}"


@backend_bp.route("/crash")
def crash():
    # TODO: how to crash the service?
    raise RuntimeError("Requested crash")
    return "crash"
