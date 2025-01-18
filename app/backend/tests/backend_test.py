import json
import os
from unittest import mock

from board import create_app
from board.config import DEFAULT_WORKER_NAME


def test_info_default(test_client):
    response = test_client.get('/info')
    res = json.loads(response.data.decode('utf-8'))

    assert set(res.keys()) == {'time', 'worker'}
    assert res['time'] != ''
    assert res['worker'] == DEFAULT_WORKER_NAME


def test_info():
    TEST_WORKER_NAME = "Test worker"
    with mock.patch.dict(os.environ, {"WORKER_NAME": TEST_WORKER_NAME}):
        test_app = create_app()
        test_client = test_app.test_client()

    params = {
        'abc': 'xyz',
        'q': '42'
    }
    response = test_client.get(f'/info?{'&'.join([f"{k}={v}" for k,v in params.items()])}')
    res = json.loads(response.data.decode('utf-8'))

    assert set(res.keys()) == {'time', 'worker', 'params'}
    assert res['time'] != ''
    assert res['worker'] == TEST_WORKER_NAME
    assert res['params'] == params


@mock.patch('board.backend.fetch_posts', return_value=[{'author': 'name', 'text': 'post'}])
def test_posts_get(fetch_posts, test_client):
    response = test_client.get('/posts')

    assert response.status_code == 200
    fetch_posts.assert_called_once()

    res = json.loads(response.data.decode('utf-8'))
    assert res == fetch_posts.return_value


def test_posts_post(test_client):
    data = {
        'author': 'test-author',
        'text': 'test text'
    }

    response = test_client.post(
        '/posts',
        data=json.dumps(data),
        content_type='application/json')

    assert response.status_code == 200
