"""The JWT authentication file"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any


auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login(login: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Login endpoint
    """
    pass
