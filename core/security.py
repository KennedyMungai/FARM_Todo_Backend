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
