def test_clubs_data_structure(get_clubs):
    response_json = get_clubs().json()

    for club in response_json["results"]:
        assert "id" in club
        assert "bookTitle" in club
        assert "bookAuthors" in club
        assert "publicationYear" in club
        assert "description" in club
        assert "telegramChatLink" in club
        assert "owner" in club
        assert "members" in club
        assert "reviews" in club
        assert "created" in club
        assert "modified" in club
