def test_get_reviews(get_reviews):
    response = get_reviews()

    assert response.status_code == 200, (
        f"Ожидали статус 200, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    assert "count" in response.json(), "В ответе отсутствует поле count"
    assert "next" in response.json(), "В ответе отсутствует поле next"
    assert "previous" in response.json(), "В ответе отсутствует поле previous"
    assert "results" in response.json(), "В ответе отсутствует поле results"
