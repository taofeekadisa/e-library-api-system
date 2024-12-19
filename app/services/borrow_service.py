import app
from ..schemas.borrow_schema import Borrow
from ..db.in_memory_db import borrow_records
from ..crud.user_crud import users, user_crud
from ..crud.book_crud import books, book_crud
from ..crud.borrow_crud import borrow_crud
from ..services.book_service import book_service
from datetime import datetime

class BorrowService():
    
    @staticmethod
    def borrow_book(user_id:int, book_id:int):
        user = user_crud.get_user_by_id(user_id)
        book = book_crud.get_book_by_id(book_id)
        
        if not user:
            raise Exception("User not Found")
        if not user.is_active:
            raise Exception("User not Active")
        if not book:
            raise Exception("Book Not Found")
        if not book.is_available:
            raise Exception("Book Not Available")
    
        for record in borrow_records.values():
            if (
                record.user_id == user_id and
                record.book_id == book_id and
                not record.return_date
            ):
                raise Exception("User already borrow this book")
            
        borrow_record = borrow_crud.create_borrow_record(user_id, book_id)
        
        book_service.mark_book_as_unavailable(book_id)
        
        return borrow_record
    
    @staticmethod
    def return_book(borrow_id:int):
        borrow_record = borrow_crud.get_borrow_record_by_id(borrow_id)
        book_id =  borrow_record.book_id
        if not borrow_record:
            raise Exception("Borrow record not found")
        
    
        borrow_record.return_date = datetime.now()
    
              
        book_service.mark_book_as_available(book_id)
        
        return borrow_record
    
borrow_service = BorrowService()