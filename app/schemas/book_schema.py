from pydantic import BaseModel, EmailStr
from typing import Optional

class BookBase(BaseModel):
    title: str
    author:str

class BookStatus(BaseModel):
    is_available:bool = True
    
class Book(BookBase, BookStatus):
    id: int = 100001

class CreateBook(BookBase):
    title: str = "The Boy from the Book"
    author:str = "Alee Al-marabi"
    
class PatchBook(BaseModel):
    title: Optional[str] = "The Boy from the Book"
    author:Optional[str] = "Alee Al-asawi"