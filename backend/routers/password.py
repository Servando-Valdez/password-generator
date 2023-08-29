import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import APIRouter, Depends, HTTPException, Header
from services.generate_password import create_password

router = APIRouter(
    prefix="/api/password",
    tags=["password"],
    responses={404: {"description": "Not found"}},
)

def get_authorization_token(authorization: str = Header(None)):
    if authorization != os.getenv("X-API-Key"):
        raise HTTPException(status_code=400, detail="Authorization header invalid")
    return authorization

@router.get("/", summary="Create a password", description="Create a password")
def generate_password(length: int = 0, uppercase: bool = False, lowercase: bool=False,
                    digits: bool=False, symbols: bool=False,authorization_token: str = Depends(get_authorization_token) ):
    password = create_password(
        length=length,
        uppercase_bool=uppercase,
        lowercase_bool=lowercase,
        digits_bool=digits,
        symbols_bool=symbols
    )
    return {"password": password}


