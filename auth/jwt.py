"""The JWT authentication file"""
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login():
    pass
