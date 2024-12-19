from fastapi.testclient import TestClient
from unittest.mock import patch
from ..main import app
from app.crud.user_crud import users, User


client = TestClient(app)


mock_users : dict[int, User] = {
    10001: User(id=10001, first_name="Alee", last_name="Al-asawi", email="alee@alee.com", password="mypass", is_active=True),
    10015: User(id=10015, first_name="Al-ameen", last_name="Al-marabi", email="alameen@alee.com", password="mypass", is_active=True),
    10099: User(id=10099, first_name="At-telili", last_name="At-tagazuti", email="telili@example.com", password="mypass", is_active=True),
    10088: User(id=10088, first_name="shruti", last_name="Al-hassan", email="shruti@example.com", password="mypass", is_active=True),
    10100: User(id=10100, first_name="Qalam", last_name="Al-farasi", email="qalam@example.com", password="mypass", is_active=True)
}


@patch("app.crud.user_crud.users", mock_users)
def test_get_all_users():
   
    
    response = client.get("/users/")
    assert response.status_code == 200
    
    expected_mock_users = {str(k):v.model_dump() for k, v in mock_users.items()}
    assert response.json()["data"] == expected_mock_users


@patch("app.crud.user_crud.users", mock_users)
def test_add_user():
    
    user_data = {
        "first_name": "Salman",
        "last_name": "Al-asawi",
        "email": "salman@alee.com",  
        "password": "mypass",
        "confirm_password": "mypass",
    }
    
    expected_user_response = {
            "id": len(user_data["first_name"]) + len(user_data["last_name"]) + len(user_data["email"]) + 10000,
            "is_active": True,
            "first_name": "Salman",
            "last_name": "Al-asawi",
            "email": "salman@alee.com",
            "password" : "mypass"
        }
    
    #Register a new user 
    response = client.post("/users/register", json=user_data) 
    assert response.status_code == 201
    assert response.json()["data"] == expected_user_response
    assert response.json()["message"] == "user created successfully"
    
    
@patch("app.crud.user_crud.users", mock_users)
def test_add_user_409_status_code():
   
    existing_user_data = {
        "first_name": "Alee",
        "last_name": "Al-asawi",
        "email": "alee@alee.com",  
        "password": "mypass",
        "confirm_password": "mypass",
    }
    
    #Register an existing user and assert 409 status code (conflict)
    response = client.post("/users/register", json=existing_user_data)
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exist"
    
@patch("app.crud.user_crud.users", mock_users)
def test_user_login():
    user_login_details = {
        "username" :"alee@alee.com",
        "password":"mypass"
    }
    
    response = client.post("/users/login", json=user_login_details)
    assert response.status_code == 200
    assert response.json()["data"] == "Login Successful"
    

@patch("app.crud.user_crud.users", mock_users)
def test_user_login_with_incorrect_details():
    user_login_details = {
        "username" :"ali@alee.com",
        "password":"mypass"
    }
    
    response = client.post("/users/login", json=user_login_details)
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorect Login Credentails"

    
@patch("app.crud.user_crud.users", mock_users)
def test_get_users_by_id():
    expected_user_response = {
            "id": 10001,
            "is_active": True,
            "first_name": "Alee",
            "last_name": "Al-asawi",
            "email": "alee@alee.com",
            "password" : "mypass"
        }
    response = client.get("/users/10001")
    assert response.status_code == 200
    assert response.json()["data"] == expected_user_response 


@patch("app.crud.user_crud.users", mock_users)
def test_update_user_profile():
    user_data = {
        "first_name": "Al-qalam",
        "last_name": "Al-marabi",
    }
    expected_user_response = {
            "id": 10100,
            "is_active": True,
            "first_name": "Al-qalam",
            "last_name": "Al-marabi",
            "email":"qalam@example.com",
            "password" : "mypass"
        }
    response = client.patch("/users/10100", json=user_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_user_response 
    assert response.json()["message"] == "Update Successful" 


@patch("app.crud.user_crud.users", mock_users)
def test_delete_user():
   
    response = client.delete("/users/10088")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

    
@patch("app.services.user_service.users", mock_users)
def test_change_user_password():
    user_data = {
        "old_password": "mypass",
        "new_password": "newpass",
        "confirm_password": "newpass"
    }
    expected_user_response = {
            "id": 10099,
            "is_active": True,
            "first_name": "At-telili",
            "last_name": "At-tagazuti",
            "email":"telili@example.com",
            "password" : "newpass"
        }
    response = client.patch("/users/10099/password", json=user_data)
    assert response.status_code == 201
    assert response.json()["data"] == expected_user_response 

@patch("app.services.user_service.users", mock_users)
def test_deactivate_user():
    
    response = client.patch("/users/10099/deactivate")
    assert response.status_code == 201
    assert response.json()["message"] ==  "User deactivated successfully"  
   
    
@patch("app.services.user_service.users", mock_users)
def test_validate_user_status():
    
    response = client.get("/users/10015/status")
    print(mock_users)
    assert response.status_code == 200
    assert response.json()["message"] ==  "User is active"  