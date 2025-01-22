import pytest


@pytest.mark.parametrize("ticks,result", ((6, 3), (10, 21)))
def test_stress(test_client, ticks, result):
    response = test_client.get(f"/stress?ticks={ticks}")
    res = response.data.decode("utf-8")

    expected = f"Done: {result}"
    assert res[: len(expected)] == expected


def test_crash(test_client):
    response = test_client.get("/crash")
    assert response.status_code == 500
