from ..schemas.book_schema import CreateBook, Book, PatchBook
from ..db.in_memory_db import books
from fastapi import HTTPException, status

class BookCrud():
    
    @staticmethod
    def create_book(book_data:CreateBook):
        book_id = len(book_data.title) + len(book_data.author) + 1000
        for id, book_profile in books.items():
            if book_profile.title == book_data.title and book_profile.author == book_data.author:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Book already exist")
             
        book = Book( id=book_id, **book_data.model_dump())
        books[book_id] = book
        return book
    
    @staticmethod
    def get_book_by_id(book_id:int):
        book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")
        return book
        
    @staticmethod
    def get_books():
        return books
    
    @staticmethod
    def update_book(book_id:int, book_data:PatchBook):
        book:Book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book Not Found")
        for id, book_profile in book_data.model_dump(exclude_unset=True).items():
            setattr(book, id, book_profile)
            
        return book
      
    @staticmethod
    def delete_book(book_id:int):
        book:Book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book Not Found")
        
        del books[book_id] 
        return
       
book_crud = BookCrud()