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
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
