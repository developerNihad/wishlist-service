import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):

    DATABASE_URL = os.getenv("DATABASE_URL", "")

    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "")


    PROJECT_NAME: str = "Wishlist Service"
    API_V1_STR: str = "/api/v1"


    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()