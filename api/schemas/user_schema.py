from datetime import datetime
from pydantic import BaseModel, EmailStr
from datetime import datetime



class UserCreate(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    password: str
    created_at: datetime
    updated_at: datetime

class ShowUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    username: str

