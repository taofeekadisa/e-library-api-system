from fastapi import APIRouter, Body, status
from ..crud.user_crud import user_crud
from ..schemas.user_schema import CreateUser, UserLogin, UpdateUser, ChangePassword
from typing import Annotated
from ..services.user_service import user_service


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def signup(payload:CreateUser):
    new_user = user_crud.create_user(payload)
    return {"data":new_user, "message":"user created successfully"}

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(payload:UserLogin):
    user_login = user_crud.user_login(payload)
    return {"data": user_login}

@router.get("/", status_code=status.HTTP_200_OK)
async def get_users():
    users = user_crud.get_users()
    return {"data":users, "message":"Successful"}

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id:int):
    user = user_crud.get_user_by_id(user_id)
    return {"data":user, "message":"Successful"}

@router.patch("/{user_id}", status_code=status.HTTP_201_CREATED)
async def update_profile(user_id:int, payload:UpdateUser):
    updated_user = user_crud.update_user(user_id, payload)
    
    return {"data":updated_user, "message":"Update Successful"}

@router.patch("/{user_id}/password", status_code=status.HTTP_201_CREATED)
async def change_password(user_id:int, payload:ChangePassword):
    updated_user = user_service.change_password(user_id, payload)
    
    return {"data":updated_user, "message":"Password updated successfully"}


@router.patch("/{user_id}/deactivate", status_code=status.HTTP_201_CREATED)
async def deactivate_user(user_id:int):
    user_service.deactivate_user(user_id)
    
    return {"message":"User deactivated successfully"}

@router.get("/{user_id}/status", status_code=status.HTTP_200_OK)
async def validate_active_user(user_id:int):
    is_active = user_service.validate_active_user(user_id)
    
    if is_active:
        return {"message":"User is active"}
    return {"message":"User not active"}

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id:int):
    user_crud.delete_user(user_id)
    
    return {"message":"User deleted successfully"}