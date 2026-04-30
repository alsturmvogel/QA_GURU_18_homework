from jsonschema import validate


def test_auth_new_user(register_user, login_user, random_user, auth_schema):
    register_user()
    response = login_user(random_user["username"], random_user["password"])

    assert response.status_code == 200, (
        f"Ожидали статус 200, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "access" in response.json(), "В ответе отсутствует access токен"
    assert "refresh" in response.json(), "В ответе отсутствует refresh токен"
    assert len(response.json()["access"].split(".")) == 3, "access токен не является JWT"
    assert len(response.json()["refresh"].split(".")) == 3, "refresh токен не является JWT"
    validate(instance=response.json(), schema=auth_schema)


def test_auth_existing_user(login_user, existing_user, auth_schema):
    response = login_user(existing_user["username"], existing_user["password"])

    assert response.status_code == 200, (
        f"Ожидали статус 200, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "access" in response.json(), "В ответе отсутствует access токен"
    assert "refresh" in response.json(), "В ответе отсутствует refresh токен"
    assert len(response.json()["access"].split(".")) == 3, "access токен не является JWT"
    assert len(response.json()["refresh"].split(".")) == 3, "refresh токен не является JWT"
    validate(instance=response.json(), schema=auth_schema)


def test_auth_wrong_password(login_user, existing_user):
    response = login_user(existing_user["username"], "wrong_password")

    assert response.status_code == 401, (
        f"Ожидали статус 401, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "detail" in response.json(), "В ответе отсутствует текст ошибки"


def test_auth_wrong_username(login_user):
    response = login_user("nonexistent_user", "some_password")

    assert response.status_code == 401, (
        f"Ожидали статус 401, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "detail" in response.json(), "В ответе отсутствует текст ошибки"


def test_auth_empty_password(login_user, existing_user):
    response = login_user(existing_user["username"], "")

    assert response.status_code == 400, (
        f"Ожидали статус 400, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "password" in response.json(), "В ответе отсутствует текст ошибки"


def test_auth_empty_username(login_user, existing_user):
    response = login_user("", existing_user["password"])

    assert response.status_code == 400, (
        f"Ожидали статус 400, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "username" in response.json(), "В ответе отсутствует текст ошибки"


def test_auth_empty_both_fields(login_user):
    response = login_user("", "")

    assert response.status_code == 400, (
        f"Ожидали статус 400, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "username" in response.json(), "В ответе отсутствует текст ошибки для username"
    assert "password" in response.json(), "В ответе отсутствует текст ошибки для password"


def test_auth_spaces_instead_of_values(login_user):
    response = login_user(" ", " ")

    assert response.status_code == 400, (
        f"Ожидали статус 400, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "detail" in response.json() or "username" in response.json(), (
        "В ответе отсутствует текст ошибки"
    )
