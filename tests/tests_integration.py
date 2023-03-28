from fastapi.testclient import TestClient
from main_api.main import app
import requests
from .responses import (
    main_integration_mean,
    main_integration_fmean,
    main_integration_geometric_mean,
    main_integration_harmonic_mean,
    main_integration_median,
    main_integration_median_high,
    main_integration_median_low,
    main_integration_max,
    main_integration_min,
)

client = TestClient(app)

member_id = "1"


# These tests require the containers to be running
def test_integration_mean():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=mean"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_mean


def test_integration_fmean():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=fmean"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_fmean


def test_integration_geometric_mean():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=geometric_mean"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_geometric_mean


def test_integration_harmonic_mean():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=harmonic_mean"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_harmonic_mean


def test_integration_median():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=median"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_median


def test_integration_median_high():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=median_high"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_median_high


def test_integration_median_low():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=median_low"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_median_low


def test_integration_min():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=min"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_min


def test_integration_max():
    response = requests.get(
        f"http://localhost:8000/?member_id={member_id}&strategy=max"
    )
    assert response.status_code == 200
    assert response.json() == main_integration_max
