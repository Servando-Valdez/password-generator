from fastapi import APIRouter

router = APIRouter(
    prefix="/password",
    tags=["password"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", summary="Create a password", description="Create a password")
def generate_password():
    return {"password": "1234567890"}
