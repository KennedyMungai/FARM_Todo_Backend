"""The JWT authentication file"""
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.security import create_access_token, create_refresh_token
from services.user_service import UserService

auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login(_form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Login endpoint
    """
    _user = await UserService.authenticate(_email=_form_data.email, _password=_form_data.password)

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(_user.user_id),
        "refresh_token": create_refresh_token(_user.user_id)
    }
