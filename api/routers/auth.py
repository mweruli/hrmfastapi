from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.models.data_models import User
from api.utils.hash import verify_password
from api.utils.auth2 import create_access_token
from api.schemas.user_schema import Login

router = APIRouter(
    tags=["User Login"],
    prefix="/login"
)
  
@router.post("", status_code=status.HTTP_200_OK)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
     user_login = db.query(User).filter(User.username == user_credentials.username).first()

     if not user_login:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid User"
        )

     if not verify_password(user_login.password, user_credentials.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Password"
        )

     access_token = create_access_token(playload={"sub": user_login.username})
     return ({"access_token": access_token, "token_type": "bearer"})

    #  return user_login
    
    # if  and verify_password(user_credentials.password, hashed_password):
    #     access_token = create_access_token({"id":user["id"]})

    #     return ({"access_token": access_token, "token_type": "bearer"})

    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail=f"User not valid"
    #     )
     
    
