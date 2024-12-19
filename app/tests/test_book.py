from fastapi.testclient import TestClient
from unittest.mock import patch
from ..main import app
from app.crud.user_crud import users
from app.crud.book_crud import books, Book

client = TestClient(app)

mock_books : dict[int, Book] = {
    1056: Book(id=1056, title="The Boy from the Book", author="Alee Al-asawi", is_available=True),
    1093: Book(id=1093, title="In the Jungle", author="Al-ameen Al-marabi", is_available=True),
    1100: Book(id=1100, title="Th End", author="Qosi", is_available=True)
}


@patch("app.crud.book_crud.books", mock_books)
def test_get_all_books():
    
    response = client.get("/books/")
    assert response.status_code == 200
    
    expected_mock_books = {str(k):v.model_dump() for k, v in mock_books.items()}
    assert response.json()["data"] == expected_mock_books


@patch("app.crud.book_crud.books", mock_books)
def test_add_book():
    
    book_data = {
        "title": "In the Moon",
        "author": "Al-asawi",
    }
    
    expected_book_response = {
            "id": len(book_data["title"]) + len(book_data["author"]) + 1000,
            "is_available": True,
            "title": "In the Moon",
            "author": "Al-asawi"       
        }
    
    #Register a new user 
    response = client.post("/books/", json=book_data) 
    assert response.status_code == 201
    assert response.json()["data"] == expected_book_response
    assert response.json()["message"] == "Book added successfully"
    
@patch("app.crud.book_crud.books", mock_books)
def test_book_by_id():
    
    expected_book_response = {
            "id": 1056,
            "is_available": True,
            "title":"The Boy from the Book",
            "author": "Alee Al-asawi",

        }
    response = client.get("/books/1056")
    assert response.status_code == 200
    assert response.json()["data"] == expected_book_response
    
@patch("app.crud.book_crud.books", mock_books)
def test_update_book():
    book_data = {
        "title": "Qalam",
        "author": "Al-farasi",
    }
    expected_book_response = {
            "id": 1056,
            "is_available": True,
            "title": "Qalam",
            "author": "Al-farasi",

        }
    response = client.patch("/books/1056", json=book_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_book_response
    assert response.json()["message"] =="Update Successful"
    
@patch("app.crud.book_crud.books", mock_books)
def test_delete_book():
    
    response = client.delete("/books/1100")
    
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"
    

@patch("app.crud.book_crud.books", mock_books)
def test_mark_book_unavailable():
    
    response = client.patch("/books/1093/mark_unavailable")
    
    assert response.status_code == 201
    assert response.json()["message"] == "Book successfully marked unvailable"


@patch("app.crud.book_crud.books", mock_books)
def test_check_book_availablility():
    
    response = client.get("/books/1056/status")
    
    assert response.status_code == 200
    assert response.json()["message"] == "Book is available"