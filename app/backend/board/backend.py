from flask import abort, Blueprint, current_app, request
from datetime import datetime
import urllib.parse
import pymysql.cursors

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
        safe_key = urllib.parse.unquote_plus(key)
        safe_value = urllib.parse.unquote_plus(value)
        result.setdefault('params', {})[safe_key] = safe_value

    return result


@backend_bp.route("/posts", methods=("GET", "POST"))
def posts():
    if request.method == "GET":
        return _get_posts()

    if request.method == "POST":
        return _add_post(request)


def _get_db_connection():
    # TODO:
    # - handle connection errors
    # - connection pool
    # - different connections for read/write operations. Is it really needed?
    db_connection_config = {
        'host': current_app.config["DATABASE_URL"],
        'port': current_app.config["DATABASE_PORT"],
        'database': current_app.config["DATABASE_NAME"],
        'user': current_app.config["DATABASE_USERNAME"],
        'password': current_app.config["DATABASE_PASSWORD"],
    }
    if any(not bool(v) for v in db_connection_config.values()):
        return None

    return pymysql.connect(**db_connection_config)


def _get_posts():
    connection = _get_db_connection()
    if connection:
        with connection:
            return _fetch_posts(connection)
    else:
        return _fake_posts()


def _fake_posts():
    posts = [
        {
            'author': 'fake user 1',
            'text': 'fake text 1'
        },
        {
            'author': 'fake user 2',
            'text': 'fake text 2'
        },
        {
            'author': 'fake user 3',
            'text': 'fake text 3'
        },
    ]
    return posts


def _fetch_posts(connection):
    with connection.cursor() as cursor:
        query = (
            "SELECT authors.name AS author, posts.message AS text "
            "FROM posts "
            "INNER JOIN authors "
            "ON posts.author_id = authors.id")
        cursor.execute(query)

        posts = []
        for (author, message) in cursor:
            posts.append({'author': author, 'text': message})

        return posts


def _add_post(request):
    if request.json == None:
        return abort(400, description='Data must not be empty')

    author = request.json.get('author')
    text = request.json.get('text')

    connection = _get_db_connection()
    if connection:
        with connection:
           current_app.logger.info(f"Add post: author='{author}', text='{text}'")
           _insert_post(connection, author, text)
    else:
        current_app.logger.info(f"Fake-Add post: author='{author}', text='{text}'")

    return "Success", 200


def _find_author_id(cursor, author_name):
    find_author_query = "SELECT id FROM authors WHERE name = %s"
    cursor.execute(find_author_query, (author_name))
    author_id_result = cursor.fetchone()

    if author_id_result is None:
        return None

    (author_id,) = author_id_result
    return author_id


def _upsert_author(cursor, author_name):
    author_id = _find_author_id(cursor, author_name)
    if author_id is None:
        insert_author_query = "INSERT INTO authors (name) VALUES (%s)"
        cursor.execute(insert_author_query, (author_name,))
    return _find_author_id(cursor, author_name)


def _insert_post(connection, author, text):
    with connection.cursor() as cursor:
        author_id = _upsert_author(cursor, author)
        print(f"Author_id = {author_id}")

        insert_message_query = (
            "INSERT INTO posts (author_id, message) "
            "VALUES (%s, %s)")
        cursor.execute(insert_message_query, (author_id, text))
        connection.commit()  # TODO: can it be called here or should it be called on a higher level?
