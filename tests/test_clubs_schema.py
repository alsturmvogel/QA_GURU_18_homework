from jsonschema import validate


def test_get_clubs_response_matches_json_schema(get_clubs, clubs_schema):
    response = get_clubs()
    validate(instance=response.json(), schema=clubs_schema)
