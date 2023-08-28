import random
from fastapi import APIRouter
from services.generate_password import create_password

router = APIRouter(
    prefix="/api/password",
    tags=["password"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", summary="Create a password", description="Create a password")
def generate_password(length: int = 0, uppercase: bool = False, lowercase: bool=False, digits: bool=False, symbols: bool=False):
    password = create_password(
        length=length,
        uppercase_bool=uppercase,
        lowercase_bool=lowercase,
        digits_bool=digits,
        symbols_bool=symbols
    )
    return {"password": password}



