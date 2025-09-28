from typing import List
from fastapi import APIRouter
from app.schemas.auth import AuthResponse
from app.services import user_service

appRouter = APIRouter()


@appRouter.get("/getAllUsers", response_model=List[AuthResponse])
def get_all_users():
    return user_service.get_all_users()
