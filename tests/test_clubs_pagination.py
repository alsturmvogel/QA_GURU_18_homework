def test_get_clubs_pagination_fields(get_clubs):
    response_json = get_clubs(params={"page": 1}).json()

    assert "count" in response_json
    assert "next" in response_json
    assert "previous" in response_json
    assert "results" in response_json


def test_first_page_contains_results(get_clubs):
    response_json = get_clubs(params={"page": 1}).json()
    assert len(response_json["results"]) > 0, "На первой странице должны быть результаты"
