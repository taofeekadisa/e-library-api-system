from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime



class BorrowBase(BaseModel):
    user_id :int = 10001
    book_id : int = 100001
    borrow_date : datetime = Field(default_factory=datetime.now)
    return_date: None
    
class Borrow(BorrowBase):
    id:int = 2000001
    
