from fastapi.testclient import TestClient
from external_apis.externals import external_app
from .responses import (
    externals_invalid_request,
    externals_member_1,
    externals_member_20,
    externals_member_2000,
)

client = TestClient(external_app)


def test_invalid_request():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json() == externals_invalid_request


def test_request_member_1():
    response = client.get("?member_id=1")
    assert response.status_code == 200
    assert response.json() == externals_member_1


def test_request_member_20():
    response = client.get("?member_id=20")
    assert response.status_code == 200
    assert response.json() == externals_member_20


def test_request_member_2000():
    response = client.get("?member_id=2000")
    assert response.status_code == 200
    assert response.json() == externals_member_2000
