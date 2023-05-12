"""The JWT authentication file"""
from fastapi import APIRouter


auth_router = APIRouter(prefix="/login", tags=["auth"])


@auth_router.post("/")
async def login():
    pass
