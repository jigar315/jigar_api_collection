from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class SignupRequest(BaseModel):
    email: str = Field(..., example="abcd@gmail.com")
    password: str = Field(..., example="12345678")
    name: str = Field(..., example="Xyz")


class SigninRequest(BaseModel):
    email: str = Field(..., example="abcd@gmail.com")
    password: str = Field(..., example="12345678")


class AuthResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    name: Optional[str] = None
    firebaseUserId: str
    createdAt: datetime
    idToken: Optional[str] = None
