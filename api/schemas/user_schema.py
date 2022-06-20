from datetime import datetime
import imp
from fastapi import FastAPI
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
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

