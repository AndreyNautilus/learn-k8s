from flask import Blueprint, render_template, current_app
import requests
import urllib.parse

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def home():
    # TODO: use async here?
    # See: https://docs.python-requests.org/en/latest/user/advanced/#blocking-or-non-blocking
    timestamp = _fetch_timestamp_sync()
    posts = _fetch_posts()
    return render_template("pages/home.html", timestamp=timestamp, posts=posts)


def _fetch_timestamp_sync(default="no time"):
    backend_url = current_app.config.get("BACKEND_ENDPOINT")
    if (not backend_url):
        return default

    params = {}
    backend_secret = current_app.config.get("BACKEND_SECRET")
    if backend_secret:
        params["msg"] = urllib.parse.quote_plus(backend_secret)

    try:
        r = requests.get(backend_url + "/info", params=params)
        if (r.status_code != 200):
            return f"Error: {r.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

    r_json = r.json()

    result = f"{r_json.get('time', 'no time')} ({r_json.get('worker', 'no worker')})"
    echoed_msg = r_json.get('params', {}).get('msg')
    if echoed_msg:
        result += f" - {echoed_msg}"
    return result


def _fetch_posts():
    backend_url = current_app.config.get("BACKEND_ENDPOINT")
    if (not backend_url):
        return []

    try:
        r = requests.get(backend_url + "/posts")
        if (r.status_code != 200):
            return []
    except Exception as e:
        return []

    return r.json()


@pages_bp.route("/about")
def about():
    return render_template("pages/about.html")
