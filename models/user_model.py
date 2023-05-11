"""The User Model """
from uuid import UUID, uuid4
from datetime import datetime

from beanie import Document, Indexed
from pydantic import EmailStr, Field
from typing import Optional


class User(Document):
    """The User Model;

    Args:
        Document (Document): A data type resembling the MongoDB document
    """
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Indexed(str, unique=True)
    email: EmailStr = Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool]

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        """Returns when a user was created

        Returns:
            datetime: The time when the user was created
        """
        return self.id.generation_time

    @classmethod
    async def by_email(self, email: str) -> "User | None":
        """Finds a user by email

        Args:
            email (str): The email of the user

        Returns:
            User | None: The user or None
        """
        return await self.find_one(self.email == email)

    class Settings:
        """Contains the name of the db"""
        name = "Users"
