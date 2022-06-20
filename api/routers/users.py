from fastapi import APIRouter, Depends, status, HTTPException
from api.utils.sendmail import send_registration_email
from sqlalchemy.orm import Session
from api.schemas.user_schema import UserCreate, ShowUser
from api.db.database import get_db
from api.operations.user_operation import create_user, get_user_by_email,get_user,get_user_by_name

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

