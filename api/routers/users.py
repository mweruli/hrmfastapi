from fastapi import APIRouter, Depends, status, HTTPException
from api.utils.sendmail import send_registration_email
from sqlalchemy.orm import Session
from api.schemas.user_schema import UserCreate, ShowUser
from api.db.database import get_db
from api.operations.user_operation import create_user,get_user, get_user_by_email, get_user_by_name, get_users
from typing import List


router = APIRouter(
    tags=["Users Registration"],
    prefix="/user"
)

@router.post("/", response_description="user registration", response_model=ShowUser)
async def user_registration(user:UserCreate, db: Session = Depends(get_db)):
    username_found = get_user_by_name(db, username=user.username)
    email_found = get_user_by_email(db, email=user.email)

    if username_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Username already taken")
    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already taken")


    await send_registration_email("Registration Successful", user.email, {
        "title": "Registration Sucessful",
        "name": user.username
    })
    
    return create_user(db=db, user=user)

@router.get("/users", response_model=List[ShowUser])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User not found")
    return db_user


