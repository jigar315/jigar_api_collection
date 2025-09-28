from fastapi import APIRouter
from app.schemas.auth import SignupAndSignInRequest, AuthResponse
from app.services import auth_service

router = APIRouter()


@router.post("/signup", response_model=AuthResponse)
def signup(signup_data: SignupAndSignInRequest):
    return auth_service.signup_user(signup_data)


@router.post("/signin",response_model=AuthResponse)
def signin(signin_data: SignupAndSignInRequest):
    return auth_service.sign_in(signin_data)


@router.post("/forgot-password")
def forgotPassword(email: str):
    return auth_service.forgot_password_fun(email)
