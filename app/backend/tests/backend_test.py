import json
import os
from unittest import mock

from board import create_app
from board.config import DEFAULT_WORKER_NAME
from board.backend import _get_posts, _add_post


def test_info_default(test_client):
    response = test_client.get("/info")
    res = json.loads(response.data.decode("utf-8"))

    assert set(res.keys()) == {"time", "worker"}
    assert res["time"] != ""
    assert res["worker"] == DEFAULT_WORKER_NAME


def test_info():
    TEST_WORKER_NAME = "Test worker"
    with mock.patch.dict(os.environ, {"WORKER_NAME": TEST_WORKER_NAME}):
        test_app = create_app()
        test_client = test_app.test_client()

    params = {"abc": "xyz", "q": "42"}
    response = test_client.get(
        f"/info?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    )
    res = json.loads(response.data.decode("utf-8"))

    assert set(res.keys()) == {"time", "worker", "params"}
    assert res["time"] != ""
    assert res["worker"] == TEST_WORKER_NAME
    assert res["params"] == params


@mock.patch(
    "board.backend._get_posts", return_value=[{"author": "name", "text": "post"}]
)
def test_posts_get(get_posts, test_client):
    response = test_client.get("/posts")

    assert response.status_code == 200
    get_posts.assert_called_once()

    res = json.loads(response.data.decode("utf-8"))
    assert res == get_posts.return_value


@mock.patch("board.backend._get_db_connection", return_value=None)
@mock.patch(
    "board.backend._fake_posts", return_value=[{"author": "name", "text": "post"}]
)
def test_get_posts_no_connection(fake_posts, get_db_connection):
    result = _get_posts()

    get_db_connection.assert_called_once()
    fake_posts.assert_called_once()
    assert result == fake_posts.return_value


@mock.patch("board.backend._get_db_connection")
@mock.patch(
    "board.backend._fetch_posts", return_value=[{"author": "name", "text": "post"}]
)
def test_get_posts_with_connection(fetch_posts, get_db_connection):
    result = _get_posts()

    get_db_connection.assert_called_once()
    fetch_posts.assert_called_once()
    assert result == fetch_posts.return_value


@mock.patch(
    "board.backend._add_post", return_value=[{"author": "name", "text": "post"}]
)
def test_posts_post(add_post, test_client):
    data = {"author": "test-author", "text": "test text"}

    response = test_client.post(
        "/posts", data=json.dumps(data), content_type="application/json"
    )

    assert response.status_code == 200
    add_post.assert_called_once()


@mock.patch("board.backend._get_db_connection", return_value=None)
@mock.patch("board.backend._insert_post")
def test_add_post_no_connection(insert_post, get_db_connection):
    author = ("test-author",)
    text = "test text"

    _add_post(author, text)
    get_db_connection.assert_called_once()
    insert_post.assert_not_called()


@mock.patch("board.backend._get_db_connection")
@mock.patch("board.backend._insert_post")
def test_add_post_with_connection(insert_post, get_db_connection):
    author = "test-author"
    text = "test text"

    _add_post(author, text)
    get_db_connection.assert_called_once()
    insert_post.assert_called_once_with(mock.ANY, author, text)
