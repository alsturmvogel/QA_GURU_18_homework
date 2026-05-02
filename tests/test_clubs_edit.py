import uuid

import requests

from tests.conftest import CLUBS_ENDPOINT


def test_put_full_update_returns_200_and_all_fields_updated(create_club, login_user, existing_user):
    uid = uuid.uuid4().hex[:8]
    original_data = {
        "bookTitle": f"Edit Test Book {uid}",
        "bookAuthors": "Original Author",
        "publicationYear": 2024,
        "description": "Original description",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    club = create_club(original_data).json()

    token = login_user(existing_user["username"], existing_user["password"]).json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    new_data = {
        "bookTitle": f"Updated Title {uid}",
        "bookAuthors": "New Author",
        "publicationYear": 2022,
        "description": "Updated description",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    response = requests.put(f"{CLUBS_ENDPOINT}{club['id']}/", json=new_data, headers=headers)

    assert response.status_code == 200, (
        f"Ожидали 200, получили {response.status_code}. Тело: {response.text}"
    )
    body = response.json()
    assert body["bookTitle"] == new_data["bookTitle"]
    assert body["bookAuthors"] == new_data["bookAuthors"]
    assert body["publicationYear"] == new_data["publicationYear"]
    assert body["description"] == new_data["description"]
    assert body["modified"] is not None, (
        "Поле modified должно быть заполнено после обновления"
    )


def test_patch_single_field_updates_only_that_field(create_club, login_user, existing_user):
    uid = uuid.uuid4().hex[:8]
    original_data = {
        "bookTitle": f"Edit Test Book {uid}",
        "bookAuthors": "Original Author",
        "publicationYear": 2024,
        "description": "Original description",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    club = create_club(original_data).json()

    token = login_user(existing_user["username"], existing_user["password"]).json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    new_title = f"Patched Title {uid}"
    response = requests.patch(f"{CLUBS_ENDPOINT}{club['id']}/", json={"bookTitle": new_title}, headers=headers)

    assert response.status_code == 200, (
        f"Ожидали 200, получили {response.status_code}. Тело: {response.text}"
    )
    body = response.json()
    assert body["bookTitle"] == new_title
    assert body["bookAuthors"] == club["bookAuthors"], (
        "PATCH не должен затрагивать поле bookAuthors"
    )
    assert body["publicationYear"] == club["publicationYear"], (
        "PATCH не должен затрагивать поле publicationYear"
    )
    assert body["description"] == club["description"], (
        "PATCH не должен затрагивать поле description"
    )


def test_patch_all_fields_updates_everything(create_club, login_user, existing_user):
    uid = uuid.uuid4().hex[:8]
    original_data = {
        "bookTitle": f"Edit Test Book {uid}",
        "bookAuthors": "Original Author",
        "publicationYear": 2024,
        "description": "Original description",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    club = create_club(original_data).json()

    token = login_user(existing_user["username"], existing_user["password"]).json()["access"]
    headers = {"Authorization": f"Bearer {token}"}

    new_data = {
        "bookTitle": f"All Patched {uid}",
        "bookAuthors": "All Patched Author",
        "publicationYear": 2020,
        "description": "All patched description",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    response = requests.patch(f"{CLUBS_ENDPOINT}{club['id']}/", json=new_data, headers=headers)

    assert response.status_code == 200, (
        f"Ожидали 200, получили {response.status_code}. Тело: {response.text}"
    )
    body = response.json()
    assert body["bookTitle"] == new_data["bookTitle"]
    assert body["bookAuthors"] == new_data["bookAuthors"]
    assert body["publicationYear"] == new_data["publicationYear"]
    assert body["description"] == new_data["description"]
