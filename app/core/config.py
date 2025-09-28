from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Professional FastAPI User Management"
    VERSION: str = "1.0.0"
    DATABASE_URL: str
    USER_TABLE_NAME: str = "user"
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
