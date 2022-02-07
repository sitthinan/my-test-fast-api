from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/order",
    tags=["Order"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
async def get_oder():
    return 0
