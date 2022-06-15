from fastapi import APIRouter


router = APIRouter(
    tags=["Company Creation"],
    prefix="/company",
)

@router.get("/")
def read_root():
    return {"Hello": "Company"}