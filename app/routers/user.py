from typing import List, Optional
from fastapi import APIRouter, Depends
from app.schemas.user import UserResponse
from app.services import user_service
from app.core.auth_middleware import verify_firebase_token

appRouter = APIRouter(dependencies=[Depends(verify_firebase_token)])


@appRouter.get("/getAllUsers", response_model=List[UserResponse])
def get_all_users():
    return user_service.get_all_users()


@appRouter.get("/getUserById", response_model=UserResponse)
def get_user_by_id(userId: str):
    return user_service.get_user_by_id(userId)


@appRouter.delete("/deleteUser", response_model=UserResponse)
def delete_user(userId: str):
    return user_service.delete_user_from_db(userId)


@appRouter.post("/updateUser", response_model=UserResponse)
def update_user(userId: str, name: Optional[str] = None):
    return user_service.update_user_by_id(userId, name)


@appRouter.get("/me", response_model=UserResponse)
def get_current_user(token_data: dict = Depends(verify_firebase_token)):
    firebaseUid = token_data.get("uid")
    return user_service.get_user_by_firebase_uid(firebaseUid)
