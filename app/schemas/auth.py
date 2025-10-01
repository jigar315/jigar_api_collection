from pydantic import BaseModel, ConfigDict
from datetime import datetime


class SignupAndSignInRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    firebaseUserId: str
    createdAt: datetime
    isDeleted: bool