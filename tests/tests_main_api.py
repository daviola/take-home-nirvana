from fastapi.testclient import TestClient
from main_api.main import app
from .responses import (
    main_invalid_request,
    main_invalid_strategy,
)

client = TestClient(app)


def test_invalid_request():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json() == main_invalid_request


def test_invalid_strategy_request():
    response = client.get("/?member_id=1&strategy=invalid")
    assert response.status_code == 400
    assert response.json() == main_invalid_strategy


def test_valid_request(httpx_mock):
    # TODO figure out how to mock only the 'external' api requests
    httpx_mock.add_response(json=main_invalid_strategy)
    response = client.get("?member_id=1&strategy=mean")
    assert response.status_code == 200
    assert response.json() == main_invalid_strategy
