from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    first_name:str 
    last_name:str
    email: EmailStr
    password:str
 
class UserStatus(BaseModel):
    is_active:bool = True
              
class User(UserBase, UserStatus):
    id: int = 10001


class CreateUser(UserBase):
    first_name:str = "Alee"
    last_name:str = "Al-asawi"
    email: EmailStr = "alee@alee.com"
    password:str = "mypass"
    confirm_password:str = "mypass"
    
class UserLogin(BaseModel):
    username:str = "alee@alee.com"
    password:str = "mypass"
        
class UpdateUser(BaseModel):
    first_name:Optional[str] = "Al-ameen"
    last_name:Optional[str] = "Al-marabi"
    
class ChangePassword(BaseModel):
    old_password:str = "mypass"
    new_password:str = "newpass"
    confirm_password:str = "newpass" 
