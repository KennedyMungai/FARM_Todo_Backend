"""The file that will contain the configuration logic for the application"""
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv


class Settings(BaseSettings):
    """The settings class

    Args:
        BaseSettings (Pydantic): Contains the base logic for defining the settings logic
    """
    pass
