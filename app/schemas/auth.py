from pydantic import BaseModel
from datetime import datetime


class SignupAndSignInRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    id: int
    email: str
    firebaseUserId: str
    createdAt: datetime
    isDeleted: bool

    class Config:
        orm_mode = True
