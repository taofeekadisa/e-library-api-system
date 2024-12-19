from ..schemas.borrow_schema import Borrow
from ..db.in_memory_db import borrow_records
from datetime import datetime
from .user_crud import user_crud

class BorrowCrud():
    
    @staticmethod
    def create_borrow_record(user_id:int, book_id:int):
        borrow_id = user_id + book_id + 2000000
        borrow_record = Borrow(
            id = borrow_id, 
            user_id = user_id, 
            book_id = book_id,
            borrow_date = datetime.now(),
            return_date = None)
    
        borrow_records[borrow_id] = borrow_record
        
        return borrow_record
    
    @staticmethod
    def get_all_borrow_records():
        return borrow_records
    
    @staticmethod
    def get_borrow_record_by_id(borrow_id:int):
        borrow_record = borrow_records.get(borrow_id)
        return borrow_record
    
    @staticmethod
    def get_user_borrow_records(user_id:int):
        user = user_crud.get_user_by_id(user_id)
        
        if not user:
            raise Exception("User not found")
        
        user_borrow_records = {id:record for id, record in borrow_records.items() if record.user_id == user.id}

        if not user_borrow_records:
            raise Exception("No borrow record for user")
        
        return user_borrow_records
borrow_crud = BorrowCrud()