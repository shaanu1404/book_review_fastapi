from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

fake_book_data = [
    {
        "title": "Harry Potter",
        "author": "J K Rowling",
        "publication_year": 1995,
        "id": 1
    },
    {
        "title": "Harry Potter 2",
        "author": "J K Rowling",
        "publication_year": 1997,
        "id": 2
    },
    {
        "title": "3 Idiots",
        "author": "Chetan Bhagat",
        "publication_year": 2012,
        "id": 3
    },
    {
        "title": "2 States",
        "author": "Chetan Bhagat",
        "publication_year": 2015,
        "id": 4
    },
    {
        "title": "Way to Jurassic Park",
        "author": "Anonymous",
        "publication_year": 2015,
        "id": 5
    },
    {
        "title": "Jurassic Park 4",
        "author": "Writer",
        "publication_year": 2024,
        "id": 6
    },
    {
        "title": "Jurassic Park 5",
        "author": "Writer",
        "publication_year": 2024,
        "id": 7
    },
    {
        "title": "Jurassic Park 6",
        "author": "Writer",
        "publication_year": 2024,
        "id": 8
    },
    {
        "title": "Jurassic Park 6",
        "author": "Writer",
        "publication_year": 2024,
        "id": 9
    },
    {
        "title": "Jurassic Park 6",
        "author": "Writer",
        "publication_year": 2024,
        "id": 10
    }
]


def test_get_all_books():
    response = client.get('/api/v1/books')
    assert response.status_code == 200
    assert response.json() == fake_book_data
