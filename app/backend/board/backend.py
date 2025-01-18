from flask import abort, Blueprint, current_app, request
from datetime import datetime
import urllib.parse

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


@backend_bp.route("/posts", methods=("GET", "POST"))
def posts():
    if request.method == "GET":
        return fetch_posts()

    if request.method == "POST":
        return add_post(request)


def fetch_posts():
    posts = [
        {
            'author': 'user 1',
            'text': 'text 1'
        },
        {
            'author': 'user 2',
            'text': 'text 2'
        },
        {
            'author': 'user 3',
            'text': 'text 3'
        },
    ]
    return posts


def add_post(request):
    if request.json == None:
        return abort(400, description='Data must not be empty')

    author = request.json.get('author')
    text = request.json.get('text')

    current_app.logger.info(f"Add post: author='{author}', text='{text}'")

    return "Success", 200
