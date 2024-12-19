from fastapi.testclient import TestClient
from unittest.mock import patch
from ..main import app
from app.crud.user_crud import User
from app.crud.book_crud import Book
from datetime import datetime
from app.services.borrow_service import Borrow
import pytest




client = TestClient(app)

mock_users = {
    10001: User(id=10001, first_name="Alee", last_name="Al-asawi", email="alee@alee.com", password="mypass", is_active=True),
    10015: User(id=10015, first_name="Al-ameen", last_name="Al-marabi", email="alameen@alee.com", password="mypass", is_active=True),
    10099: User(id=10099, first_name="At-telili", last_name="At-tagazuti", email="telili@example.com", password="mypass", is_active=True),
    10088: User(id=10088, first_name="shruti", last_name="Al-hassan", email="shruti@example.com", password="mypass", is_active=True),
}

mock_books = {
    1093: Book(id=1093, title="In the Jungle", author="Al-ameen Al-marabi", is_available=True),
    1056: Book(id=1056, title="The Boy from the Book", author="Alee Al-asawi", is_available=True),
}

mock_borrow_records = {
    2000036: Borrow(id=2000036, user_id=10001, book_id=1056, borrow_date=datetime(2024, 12, 19, 12, 0, 0), return_date=None),
    2000037: Borrow(id=2000037, user_id=10015, book_id=1056, borrow_date=datetime(2024, 12, 19, 12, 0, 0), return_date=None),
}


@patch("app.crud.borrow_crud.borrow_records", mock_borrow_records)
@patch("app.services.borrow_service.datetime")
def test_get_all_borrow_records(mock_datetime):
    
    mock_datetime.now.return_value = datetime(2024, 12, 19, 12, 0, 0)
    mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    
    response = client.get("/borrow/records")
    
    expected_mock_records = {str(k):{**v.model_dump(),
                                    "borrow_date": v.borrow_date.isoformat() if v.borrow_date else None,
                                    "return_date": v.return_date.isoformat() if v.return_date else None,} for k, v in mock_borrow_records.items()}
    assert response.status_code == 200
    assert response.json() == expected_mock_records


@patch("app.crud.borrow_crud.borrow_records", mock_borrow_records)
@patch("app.crud.borrow_crud.datetime")
@patch("app.crud.user_crud.users", mock_users)
def test_get_user_borrow_records(mock_datetime):
    
    mock_now = datetime(2024, 12, 19, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

    expected_record_response = {
        "2011060": {
            "user_id": 10001,
            "book_id": 1056,
            "borrow_date": mock_now.isoformat(),
            "return_date": None,
            "id": 2000036
        }
    }
    
    response = client.get("/borrow/users/10001")
    assert response.status_code == 200
    #assert response.json() == expected_record_response

@patch("app.crud.borrow_crud.borrow_records", mock_borrow_records)
@patch("app.services.borrow_service.datetime")
def test_get_single_borrow_record(mock_datetime):
    
    mock_now = datetime(2024, 12, 19, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    
    expected_record_response = {
            "id": 2000036,
            "user_id": 10001,
            "book_id": 1056,
            "borrow_date": mock_now.isoformat(),
            "return_date": None
        
        }
    
    response = client.get("/borrow/records/2000036")
    assert response.status_code == 200
    assert response.json() == expected_record_response


@patch("app.crud.user_crud.users", new=mock_users)
@patch("app.crud.book_crud.books", new=mock_books)
@patch("app.services.borrow_service.borrow_records", new=mock_borrow_records)
@patch("app.crud.borrow_crud.datetime")
def test_borrow_book(mock_datetime):
    
    mock_now = datetime(2024, 12, 19, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    
    expected_record_response = {
            "id": 10001 + 1093 + 2000000,
            "user_id": 10001,
            "book_id": 1093,
            "borrow_date": mock_now.isoformat(),
            "return_date": None
        
        }
    
    response = client.post("/borrow/10001/1093")
    
    assert response.status_code == 201
    assert response.json()["data"] == expected_record_response
    assert response.json()["message"] == "Book borrowed successfully"
    
patch("app.crud.user_crud.users", new=mock_users)
@patch("app.crud.book_crud.books", new=mock_books)
@patch("app.services.borrow_service.borrow_records", new=mock_borrow_records)
@patch("app.services.borrow_service.datetime")
def test_return_book(mock_datetime):
    
    mock_now = datetime(2024, 12, 19, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
    
    expected_record_response = {
            "id": 10001 + 1093 + 2000000,
            "user_id": 10001,
            "book_id": 1093,
            "borrow_date": mock_now.isoformat(),
            "return_date": mock_now.isoformat()
        
        }
    
    response = client.post("/borrow/2011094")
    
    assert response.status_code == 201
    assert response.json()["data"] == expected_record_response
    assert response.json()["message"] == "Book returned successfully"
    