from fastapi import APIRouter

from api.schemas.company_schema import Company


router = APIRouter(
    tags=["Company Creation"],
    prefix="/company"
)

@router.post("/")
def create(request: Company):
    return request