from fastapi import APIRouter
from app.schemas.auth import SigninRequest,SignupRequest, AuthResponse
from app.services import auth_service

router = APIRouter()


@router.post("/signUp", response_model=AuthResponse)
def signup(signup_data: SignupRequest):
    return auth_service.signup_user(signup_data)


@router.post("/signIn", response_model=AuthResponse)
def signin(signin_data: SigninRequest):
    return auth_service.sign_in(signin_data)


@router.post("/forgotPassword")
def forgotPassword(email: str):
    return auth_service.forgot_password_fun(email)
