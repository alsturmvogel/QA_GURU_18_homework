import uuid


def test_create_club(create_club):
    unique_id = uuid.uuid4().hex[:10]
    data = {
        "bookTitle": f"Book {unique_id}",
        "bookAuthors": "Test Author",
        "publicationYear": 2024,
        "description": "string",
        "telegramChatLink": "https://t.me/qa.guru",
    }
    response = create_club(data)

    assert response.status_code == 201, (
        f"Ожидали статус 201, получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
