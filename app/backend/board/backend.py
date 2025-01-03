from flask import Blueprint, current_app, request
from datetime import datetime
import urllib.parse
import math

backend_bp = Blueprint("backend", __name__)


@backend_bp.route("/info", methods=("GET",))
def info():
    time_msg = datetime.now().strftime("%m/%d/%Y - %H:%M:%S")
    worker = current_app.config["WORKER_NAME"]

    result = {
        'time': time_msg,
        'worker': worker,
    }

    for key, value in request.args.items():
        result.setdefault('params', {})[urllib.parse.unquote_plus(key)] = urllib.parse.unquote_plus(value)

    return result


@backend_bp.route("/stress", methods=("Get",))
def stress():
    ticks = int(request.args.get("ticks", 1000000))

    res = 0
    for i in range(ticks):
        res = (res + int(math.sqrt(i * 65)) % 17) % 23  # some "heavy" computation

    return f"Done: {res}"


@backend_bp.route("/crash")
def crash():
    # TODO: how to crash the service?
    raise RuntimeError("Requested crash")
    return "crash"
