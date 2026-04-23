import pytest
import requests

from tests.schemas.get_books_response_schema import get_books_response_schema


BASE_URL = "https://book-club.qa.guru"
CLUBS_ENDPOINT = f"{BASE_URL}/api/v1/clubs/"


@pytest.fixture
def clubs_schema():
    return get_books_response_schema


@pytest.fixture
def get_clubs():
    def _get_clubs(params=None):
        response = requests.get(CLUBS_ENDPOINT, params=params)
        assert response.status_code == 200, (
            f"Ожидали статус 200, получили {response.status_code}"
        )
        return response

    return _get_clubs