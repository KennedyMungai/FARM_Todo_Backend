"""The User Model """
from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr


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
