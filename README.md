<h1> E-Library API System </h1>

<h3> Description</h3>
<p>
The **E-Library API System** is a backend service for managing an online library. It provides endpoints to manage users, books, and borrowing operations, allowing users to borrow and return books while keeping track of book availability and user activity. 
</p>
<p>
This project is built with **FastAPI** and uses **in-memory data structures** for storage, making it lightweight and easy to set up.
</p>

<h3> Features </h3>

<h4> **User Management** : </h4>
- Create, read, update, and delete users.
- Deactivate user accounts.

<h4> **Book Management** : </h4>
- Create, read, update, and delete books.
- Mark books as unavailable for borrowing.

<h4> **Borrow Operation** : </h4>
- Borrow available books if the user is active.
- Return borrowed books and update their availability.
- Prevent duplicate borrowing of the same book by the same user.

<h4> **Borrow Record Management** : </h4>
- View all borrowing records.
- View borrowing records for a specific user.

<h3> Tech Stack </h3>
- **Framework** : FastAPI
- **Language** : Python
- **Data Storage** : In-memory structures (dictionaries)

<h3> Installation </h3>
- Python 3.9 or higher
- `pip` package manager

<h3> Steps </h3>

<h4> 1. Clone the repository: </h4>

```
git clone https://github.com/taofeekadisa/e-library-api-system.git

```

<h4> 2. Create a virtual environment: </h4>

```
python -m venv venv
source venv/bin/activate  

```
On windows
```
python -m venv venv
source venv/Scripts/activate

```

<h4> 3. Install dependencies: </h4>

```
pip install -r requirements.txt 

```
<h4> 4. Run the FastAPI server: </h4>

```
uvicorn main:app --reload

```

<h4> 5. Open the API documentation in your browser: </h4>

- Swagger UI : http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

<h3> Project Structure </h3>

```
e-library-api
|
├── app/
│   ├── __init__.py
│   ├── main.py
|   |
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── book_crud.py
│   │   ├── borrow_crud.py
|   |   └── borrow_crud.py
|   |
│   ├── db/
│   │   ├── __init__.py
│   │   └── in_memory_db.py  
|   |
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── book_routes.py
│   │   ├── borrow_routes.py
│   │   └── user_routes 
|   |
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── book_schema.py
│   │   ├── borrow_schema.py
|   |   └── user_schema.py
|   |
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_servic.py
│   │   ├── borrow_service.py
|   |   └── user_service.py
|   |
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_book.py
│   │   ├── test_borrow.py
|   |   └── user_user.py
|   |
│   ├── utils/
│       ├── __init__.py
│
│
├── .gitignore
├── venv
├── requirements.txt
├── project_details.md
└── README.md          

```

<h3> API Enfpoints </h3>

<h4> User Endpoints </h4>

- POST /users/register - Create a new user.
- POST /users/login - User login
- GET /users/ - Retrieve all users
- GET /users/{user_id} - Retrieve a user by ID.
- PATCH /users/{user_id} - Update user details.
- DELETE /users/{user_id} - Delete a user.
- PATCH /users/{user_id}/password - Change password
- PATCH /users/{user_id}/deactivate - Deactivate a user.
- GET /users/{user_id}/status - Validate Activate User

<h4> Book Endpoints </h4>
- POST /books/ - Add a new book.
- GET /books/ - Retrieve all books
- GET /books/{book_id} - Retrieve a book by ID.
- PATCH /books/{book_id} - Update book details.
- DELETE /books/{book_id} - Delete a book.
- PATCH /books/{book_id}/mark-unavailable - Mark a book as unavailable.
- GET /books/{book_id}/status - Validate book availability

<h4> Borrow Endpoints </h4>
- POST /borrow/ - Borrow a book.
- PATCH /borrow/return/{borrow_id} - Return a borrowed book.
- GET /borrow/records - Get all borrowing records.
- GET /borrow/records/{borrow_d} - Get single borrow record
- GET /borrow/records/{user_id} - Get borrowing records for a specific user.

<h3> Testing </h3>

```
pytest

```
Tests are located in the tests/ directory and cover:

- Endpoint behavior.
- Logic in services.

<h3> Future Improvements</h3>

- Integrate a database (e.g., PostgreSQL) for persistent data storage.
- Implement authentication and authorization for secure access.
- Add pagination and filtering for large datasets in endpoints.
- Provide rate-limiting to prevent abuse of the API.
- Add database migration using alembic