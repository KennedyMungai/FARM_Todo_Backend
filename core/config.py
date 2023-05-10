"""The file that will contain the configuration logic for the application"""
import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """The settings class

    Args:
        BaseSettings (Pydantic): Contains the base logic for defining the settings logic
    """
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = os.environ.get("JWT_REFRESH_SECRET_KEY")
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRATION_MINUTES: int = 60 * 24 * 7         # 7 days
    PROJECT_NAME: str = "Todo App"

    # Database
    MONGODB_URL: str = os.environ.get("MONGODB_URL")

    class Config:
        """The configuration subclass"""
        case_sensitive = True


settings = Settings()
