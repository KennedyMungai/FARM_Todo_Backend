"""The file that contains the security for the backend application"""
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from core.config import settings

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    """
    Hashes a password using the passlib library
    :param password: the password to be hashed
    :return: the hashed password
    """
    return password_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Function verifies the password using the passlib library.

    Returns:
        bool: _description_
    """
    return password_context.verify(plain_password, hashed_password)


def create_access_token(_subject: Union[str, Any], _expires_delta: int = None) -> str:
    """Function creates the access token

    Args:
        _subject (Union[str, Any]): The subject of the token.
        _expires_delta (int, optional): The expiration time of the token.
        Defaults to None.

    Returns:
        str: The access token
    """
    if _expires_delta is not None:
        _expires_delta = datetime.utcnow() + _expires_delta
    else:
        _expires_delta = datetime.utcnow(
        ) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_MINUTES)

    to_encode = {"exp": _expires_delta, "sub": str(_subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)

    return encoded_jwt
