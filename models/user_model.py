"""The User Model """
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import EmailStr, Field


class User(Document):
    """The User Model;

    Args:
        Document (Document): A data type resembling the MongoDB document
    """
    user_id: UUID = Field(default_factory=uuid4)
    username: str = Indexed(str, unique=True)
    email: EmailStr = Indexed(EmailStr, unique=True)
    hashed_password: str
    first_name: str
    last_name: str
    disabled: bool

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
