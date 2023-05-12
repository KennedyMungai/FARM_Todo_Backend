"""The JWT authentication file"""
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.user_service import UserService

auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login(_form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Login endpoint
    """
    _user = await UserService.authenticate(email=_form_data.email, password=_form_data.password)
