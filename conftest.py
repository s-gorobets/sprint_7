import requests
from urls import *
import pytest

@pytest.fixture()
def delet_curier():
    courier_ids = []
    yield courier_ids
    for courier_id in courier_ids:
        response = requests.delete(f"{DELET_CURIER_URL}/{courier_id}")
        assert response.status_code == 200
        assert response.json().get("ok") is True
