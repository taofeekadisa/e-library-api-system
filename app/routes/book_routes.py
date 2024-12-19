from fastapi import APIRouter, Body, status
from ..crud.book_crud import book_crud
from ..schemas.book_schema import CreateBook, Book, PatchBook
from typing import Annotated
from ..services.book_service import book_service


router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(payload:CreateBook):
    new_book = book_crud.create_book(payload)
    return {"data":new_book, "message":"Book added successfully"}

@router.get("/", status_code=status.HTTP_200_OK)
async def get_books():
    books = book_crud.get_books()
    return {"data":books, "message":"Successful"}

@router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id:int):
    book = book_crud.get_book_by_id(book_id)
    return {"data":book, "message":"Successful"}

@router.patch("/{book_id}", status_code=status.HTTP_201_CREATED)
async def update_book(book_id:int, payload:PatchBook):
    updated_book = book_crud.update_book(book_id, payload)
    
    return {"data":updated_book, "message":"Update Successful"}

@router.patch("/{book_id}/mark_unavailable", status_code=status.HTTP_201_CREATED)
async def mark_book_as_unavailable(book_id:int):
    book_service.mark_book_as_unavailable(book_id)
    
    return {"message":"Book successfully marked unvailable"}

@router.get("/{book_id}/status", status_code=status.HTTP_200_OK)
async def validate_book_availability(book_id:int):
    is_available = book_service.validate_book_availabity(book_id)
    
    if is_available:
        return {"message":"Book is available"}
    return {"message":"Book not available"}

@router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id:int):
    book_crud.delete_book(book_id)
    
    return {"message":"Book deleted successfully"}