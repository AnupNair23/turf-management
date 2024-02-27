# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str
    MONGO_DB_NAME: str
    OPENWEATHER_API_KEY: str  # Assuming you're using OpenWeatherMap API
    ALLOWED_HOSTS: list[str] = ['*']  # Default to allowing all hosts
    class Config:
        env_file = ".env"

settings = Settings()
