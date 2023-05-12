"""The script to hold the user services"""
from typing import Optional

from core.security import hash_password
from models.user_model import User
from schemas.user_schema import UserAuth


class UserService:
    """The class which is the template for the user services
    """
    @staticmethod
    async def create_user(user: UserAuth):
        """The async function that creates the user for the application

        Args:
            user (UserAuth): The user data

        Returns:
            User: The newly created user
        """
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password)
        )

        await user_in.save()
        return user_in

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        pass
