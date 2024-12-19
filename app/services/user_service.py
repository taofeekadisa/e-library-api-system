from ..schemas.user_schema import UserBase, User, UpdateUser, ChangePassword, UserLogin, UserStatus, CreateUser, UpdateUser
#from ..db.in_memory_db import users
from fastapi import HTTPException, status
from ..crud.user_crud import users

class UserService():
     
    @staticmethod
    def change_password(user_id:int, user_data:ChangePassword):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        for id, user_profile in users.items():
            if user_profile.password != user_data.old_password:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
            if user_data.new_password != user_data.confirm_password:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "The passwords provided do not match. Please try again.")

            user_profile.password = user_data.new_password
        return user
    
  
    @staticmethod
    def deactivate_user(user_id:int):
        user:User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        if user.is_active != True:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already deactivated")
            
        user.is_active = False
        
        return
    
    @staticmethod
    def validate_active_user(user_id:int):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
        
        if user.is_active == True:
                return True
        return False
user_service = UserService()