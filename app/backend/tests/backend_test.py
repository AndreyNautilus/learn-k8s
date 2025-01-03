import json
import os
from unittest import mock
import pytest

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


@pytest.mark.parametrize("ticks,result", (
    (6, 3),
    (10, 21)))
def test_stress(test_client, ticks, result):
    response = test_client.get(f'/stress?ticks={ticks}')
    res = response.data.decode('utf-8')

    expected = f"Done: {result}"
    assert res[:len(expected)] == expected


def test_crash(test_client):
    response = test_client.get('/crash')
    assert response.status_code == 500
