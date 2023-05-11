"""The file that contains the security for the backend application"""
from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
