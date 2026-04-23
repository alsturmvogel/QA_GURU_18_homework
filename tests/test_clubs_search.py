def test_search_by_book_title(get_clubs):
    search_value = "Сети"
    response_json = get_clubs(params={"search": search_value}).json()

    assert isinstance(response_json["results"], list), "Поле results должно быть списком"
    assert len(response_json["results"]) > 0, "Поиск должен вернуть хотя бы один результат"

    for club in response_json["results"]:
        assert search_value.lower() in club["bookTitle"].lower(), (
            f"Клуб с id={club['id']} не содержит '{search_value}' в названии книги"
        )