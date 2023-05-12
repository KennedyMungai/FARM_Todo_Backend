"""The JWT authentication file"""
from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth", tags=["auth"])
