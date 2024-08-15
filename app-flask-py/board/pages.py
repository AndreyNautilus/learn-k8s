from flask import Blueprint, render_template, current_app
import requests

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def home():    
    # TODO: use async here?
    # See: https://docs.python-requests.org/en/latest/user/advanced/#blocking-or-non-blocking
    timestamp = fetch_timestamp_sync()
    return render_template("pages/home.html", timestamp=timestamp)


def fetch_timestamp_sync(default="no time"):
    backend_url = current_app.config.get("BACKEND_ENDPOINT")
    if (not backend_url):
        return default

    try:
        r = requests.get(current_app.config["BACKEND_ENDPOINT"])
        if (r.status_code != 200):
            return f"Error: {r.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

    timestamp = r.json().get('time')
    worker = r.json().get('worker')

    return f"{timestamp} ({worker})"


@pages_bp.route("/about")
def about():
    return render_template("pages/about.html")
