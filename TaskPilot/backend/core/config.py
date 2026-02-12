from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Manages application settings using environment variables.
    """
    PROJECT_NAME: str = "TaskPilot"
    API_V1_STR: str = "/api/v1"

    # Database URL
    DATABASE_URL: str = "sqlite:///./taskpilot.db"

    # Celery & Redis settings
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    # Connector settings
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_CHAT_ID: str = ""
    GMAIL_API_KEY: str = "" # Placeholder for now

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()