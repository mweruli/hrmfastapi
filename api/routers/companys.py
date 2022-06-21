from fastapi import APIRouter, Depends
from api.models.data_models import User
from api.utils.auth2 import get_current_user
from api.schemas.company_schema import Company


router = APIRouter(
    tags=["Company Creation"],
    prefix="/company"
)

@router.post("/")
def create(request: Company, current_user: User = Depends(get_current_user)):
    return request