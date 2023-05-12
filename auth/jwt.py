"""The JWT authentication file"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login(login: OAuth2PasswordRequestForm = Depends()):
    """
    Login endpoint
    """
    pass
