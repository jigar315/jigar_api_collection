from app.models.auth import AuthUser
from app.schemas.auth import SignupAndSignInRequest
from app.database import get_auth_database
from app.firebaseConfig import create_firebase_user, sign_in_user, forgot_password
from fastapi import HTTPException


def signup_user(signup_data: SignupAndSignInRequest):
    db = get_auth_database()
    existing_user = db.query(AuthUser).filter(AuthUser.email == signup_data.email).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Email already exists")

    try:
        firebase_uid = create_firebase_user(signup_data.email, signup_data.password)

        new_user = AuthUser(
            email=signup_data.email,
            firebaseUserId=firebase_uid
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()

        return new_user

    except Exception as e:
        db.close()
        raise HTTPException(status_code=400, detail=f"Firebase error: {str(e)}")


def sign_in(signin_data: SignupAndSignInRequest):
    db = get_auth_database()
    user = db.query(AuthUser).filter(AuthUser.email == signin_data.email).first()

    if not user:
        db.close()
        raise HTTPException(status_code=400, detail="User not registered")

    try:
        firebase_user = sign_in_user(signin_data.email, signin_data.password)

        if not firebase_user:
            db.close()
            raise HTTPException(status_code=400, detail="Invalid credentials")

        db.close()
        return user

    except Exception as e:
        db.close()
        raise HTTPException(status_code=400, detail=f"Invalid credentials")


def forgot_password_fun(email: str):
    db = get_auth_database()
    user = db.query(AuthUser).filter(AuthUser.email == email).first()

    if not user:
        db.close()
        raise HTTPException(status_code=400, detail="User not registered")

    try:
        forgot_password(email)
        db.close()
        return {"message": "Password reset email sent successfully"}

    except Exception as e:
        db.close()
        raise HTTPException(status_code=400, detail=f"Error sending reset email: {str(e)}")




