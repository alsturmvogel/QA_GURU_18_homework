def test_register_status_code(register_user):
    response = register_user()

    assert response.status_code == 201, (
        f"Ожидали статус 201, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
