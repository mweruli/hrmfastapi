from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas.user_schema import UserCreate, ShowUser
from api.db.database import get_db
from api.operations.user_operation import create_user

router = APIRouter(
    tags=["Users Registration"],
    prefix="/user"
)

@router.post("/", response_description="user registration", response_model=ShowUser)
async def user_registration(user:UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

