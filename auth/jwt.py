"""The JWT authentication file"""
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.user_service import UserService


auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login(login: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Login endpoint
    """
    pass
