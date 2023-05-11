"""Created the router file for the user"""
from fastapi import APIRouter

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
