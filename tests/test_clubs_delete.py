import uuid

import requests

from tests.conftest import CLUBS_ENDPOINT


def test_delete_club_by_owner_returns_204_and_empty_body(create_club, login_user, existing_user):
    uid = uuid.uuid4().hex[:8]
    club = create_club({
        "bookTitle": f"Delete Test {uid}",
        "bookAuthors": "Author",
        "publicationYear": 2024,
        "description": "desc",
        "telegramChatLink": "https://t.me/qa.guru",
    }).json()

    token = login_user(existing_user["username"], existing_user["password"]).json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.delete(f"{CLUBS_ENDPOINT}{club['id']}/", headers=headers)

    assert response.status_code == 204, (
        f"Ожидали 204, получили {response.status_code}. Тело: {response.text}"
    )
    assert response.text == "", (
        f"Тело ответа должно быть пустым, получили: {response.text}"
    )


def test_delete_club_without_token_returns_401(create_club):
    uid = uuid.uuid4().hex[:8]
    club = create_club({
        "bookTitle": f"Delete Test {uid}",
        "bookAuthors": "Author",
        "publicationYear": 2024,
        "description": "desc",
        "telegramChatLink": "https://t.me/qa.guru",
    }).json()

    response = requests.delete(f"{CLUBS_ENDPOINT}{club['id']}/")

    assert response.status_code == 401, (
        f"Ожидали 401, получили {response.status_code}. Тело: {response.text}"
    )
    assert "detail" in response.json(), "В теле ошибки должно быть поле detail"
