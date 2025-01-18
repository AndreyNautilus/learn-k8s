from flask import Blueprint, request
import math

stress_bp = Blueprint("stress", __name__)


def heavy_computations(ticks: int):
    res = 0
    for i in range(ticks):
        res = (res + int(math.sqrt(i * 65)) % 17) % 23  # some "heavy" computation
    return res


@stress_bp.route("/stress", methods=("Get",))
def stress():
    ticks = int(request.args.get("ticks", 1000000))
    res = heavy_computations(ticks)
    return f"Done: {res}"


@stress_bp.route("/crash")
def crash():
    # TODO: how to crash the service?
    raise RuntimeError("Requested crash")
    return "crash"
