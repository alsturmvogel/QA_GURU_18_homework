get_books_response_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "count": {
      "type": "integer"
    },
    "next": {
      "type": "string"
    },
    "previous": {
      "type": "null"
    },
    "results": {
      "type": "array",
      "items": {}
    }
  },
  "required": [
    "count",
    "next",
    "previous",
    "results"
  ]
}