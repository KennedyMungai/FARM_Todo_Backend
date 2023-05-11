"""Created the router file for the user"""
from fastapi import APIRouter

from schemas.user_schema import UserAuth
from services.user_service import UserService

user_router = APIRouter(prefix="/user", tags=["User"])


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
    tags=["Users"]
)
async def create_user_router(data: UserAuth):
    pass
