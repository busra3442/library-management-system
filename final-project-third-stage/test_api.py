from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_add_invalid_book():
    response = client.post("/books", json={"isbn": "0000000000"})
    assert response.status_code in [404, 500]
