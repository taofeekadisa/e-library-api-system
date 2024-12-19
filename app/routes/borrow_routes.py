from fastapi import APIRouter, Body, status, HTTPException
from ..crud.borrow_crud import borrow_crud
from ..schemas.borrow_schema import Borrow
from typing import Annotated
from ..services.borrow_service import borrow_service
from ..db.in_memory_db import borrow_records


router = APIRouter(tags=["Borrow"])

@router.post("/borrow/{user_id}/{book_id}", status_code=status.HTTP_201_CREATED)
def borrow_book(user_id:int, book_id:int):
    try:
        borrow_record = borrow_service.borrow_book(user_id, book_id)
        return {"message":"Book borrowed successfully", "data":borrow_record}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/borrow/records", status_code=status.HTTP_200_OK)
def get_all_borrow_records():
    borrow_records = borrow_crud.get_all_borrow_records()
    
    if not borrow_records:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No borrow records currently")
    
    return borrow_records

@router.get("/borrow/records/{borrow_id}", status_code=status.HTTP_200_OK)
def get_single_borrow_record(borrow_id:int):
    borrow_record = borrow_crud.get_borrow_record_by_id(borrow_id)
    
    if not borrow_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No record found")
    return borrow_record

@router.get("/borrow/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_borrow_records(user_id:int):
    user_borrow_record = borrow_crud.get_user_borrow_records(user_id)
    
    if not user_borrow_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No borrow record for this user")
    return user_borrow_record


@router.post("/borrow/{borrow_id}", status_code=status.HTTP_201_CREATED)
def return_book(borrow_id:int):
    try:
        borrow_record = borrow_service.return_book(borrow_id)
        return {"data":borrow_record, "message":"Book returned successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))