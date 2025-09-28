from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Professional FastAPI User Management"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "postgresql://neondb_owner:npg_X9Qoyv6ZkauE@ep-flat-fire-admw4x5q-pooler.c-2.us-east-1.aws" \
                        ".neon.tech/neondb?sslmode=require&channel_binding=require"
    USER_TABLE_NAME: str = "user"
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool = True

    class Config:
        case_sensitive = True


settings = Settings()