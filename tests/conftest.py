import uuid

import pytest
import requests

from tests.schemas.auth_schema import successful_auth_response_schema
from tests.schemas.get_books_response_schema import get_books_response_schema

BASE_URL = "https://book-club.qa.guru"
CLUBS_ENDPOINT = f"{BASE_URL}/api/v1/clubs/"
REVIEWS_ENDPOINT = f"{BASE_URL}/api/v1/clubs/reviews/"
REGISTER_ENDPOINT = f"{BASE_URL}/api/v1/users/register/"
AUTH_ENDPOINT = f"{BASE_URL}/api/v1/auth/token/"


@pytest.fixture
def clubs_schema():
    return get_books_response_schema


@pytest.fixture
def auth_schema():
    return successful_auth_response_schema


@pytest.fixture
def get_clubs():
    def _get_clubs(params=None):
        response = requests.get(CLUBS_ENDPOINT, params=params)
        assert response.status_code == 200, (
            f"Ожидали статус 200, получили {response.status_code}"
        )
        return response

    return _get_clubs


@pytest.fixture
def random_user():
    unique_id = uuid.uuid4().hex[:10]
    return {
        "username": f"user_{unique_id}",
        "password": f"pass_{unique_id}",
    }


@pytest.fixture
def existing_user():
    return {
        "username": "j6gh9FQjPRADVNsPtpHwwXgnRQE8MkXblfHieZ6B",
        "password": "string",
    }


@pytest.fixture
def register_user(random_user):
    def _register_user():
        response = requests.post(REGISTER_ENDPOINT, json=random_user)
        return response

    return _register_user


@pytest.fixture
def login_user():
    def _login_user(username, password):
        response = requests.post(AUTH_ENDPOINT, json={"username": username, "password": password})
        return response

    return _login_user


@pytest.fixture
def get_reviews():
    def _get_reviews():
        response = requests.get(REVIEWS_ENDPOINT)
        return response

    return _get_reviews


@pytest.fixture
def create_club(login_user, existing_user):
    def _create_club(data):
        token = login_user(existing_user["username"], existing_user["password"]).json()["access"]
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(CLUBS_ENDPOINT, json=data, headers=headers)
        return response

    return _create_club
