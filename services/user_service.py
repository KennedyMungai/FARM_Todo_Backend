"""The script to hold the user services"""
from typing import Optional

from core.security import hash_password, verify_password
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
    async def authenticate(_email: str, _password: str) -> Optional[User]:
        """A function to authenticate a user who has already signed in

        Args:
            _email (str): The email of the user
            _password (str): The password of the user

        Returns:
            Optional[User]: The user object
        """
        _user = UserService.get_user_by_email(_email)

        if not _user:
            return None
        if not verify_password(_password, _user.hashed_password):
            return None

        return _user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        """A static method that gets the user by email from the database

        Args:
            email (str): The User email

        Returns:
            Optional[User]: The return of the user is optional
        """
        _user = await User.find_one(User.email == email)
        return _user
