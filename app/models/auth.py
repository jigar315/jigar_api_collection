from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base
from app.core.config import settings


class AuthUser(Base):
    __tablename__ = settings.USER_TABLE_NAME

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    firebaseUserId = Column(String, unique=True, index=True)
    createdAt = Column(DateTime, default=func.now())
    isDeleted = Column(Boolean, default=False)
