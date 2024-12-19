from ..schemas.user_schema import User
from ..schemas.book_schema import Book
from ..schemas.borrow_schema import Borrow

users: dict[int:User] = {}

books:dict[int:Book] = {}

borrow_records:dict[int: Borrow] = {}
