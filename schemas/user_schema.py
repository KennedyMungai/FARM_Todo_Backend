"""The file with the user schemas"""
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    """The schema used by the user when authenticating

    Args:
        BaseModel (Pydantic): The base library for the UserAuth schema
    """
    email: EmailStr = Field(..., description="User Email")
    username: str = Field(..., min_length=5, max_length=50,
                          description="The username of the User")
    password: str = Field(..., min_length=5, max_length=24)


class UserOut(BaseModel):
    """User data template send back ti the front end

    Args:
        BaseModel (Pydantic): The base library for the UserOut schema
    """
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False
