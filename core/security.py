"""The file that contains the security for the backend application"""
from passlib.context import CryptContext


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
