"""Created the router file for the user"""
import pymongo
from fastapi import APIRouter, HTTPException, status

from schemas.user_schema import UserAuth
from services.user_service import UserService

user_router = APIRouter(prefix="/user", tags=["Users"])


@user_router.get(
    "/",
    name="Default User Router",
    description="The root route for Users",
    tags=["Users"]
)
async def user_test():
    """The default user router used for testing user routes

    Returns:
        dict[str, str]: Returns a message to show good execution
    """
    return {"message": "The user route is working"}


@user_router.post(
    "/create",
    name="Create User",
    description="An endpoint to create users",
    tags=["Users"],
    status_code=status.HTTP_201_CREATED
)
async def create_user_router(data: UserAuth):
    """The endpoint to create a user

    Args:
        data (UserAuth): The data to create a user

    Returns:
        User: Returns the newly created user
    """
    try:
        await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{error}: Username or email address already in use"
        )
