from fastapi import HTTPException
from app.models.auth import AuthUser
from app.database import get_auth_database
from app.schemas.auth import SignupRequest, SigninRequest
from app.firebaseConfig import create_firebase_user, sign_in_user, forgot_password


def signup_user(signup_data: SignupRequest):
    db = next(get_auth_database())
    existing_user = db.query(AuthUser).filter(AuthUser.email == signup_data.email, AuthUser.isDeleted == False).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Email already exists")

    firebase_uid, id_token = create_firebase_user(signup_data.email, signup_data.password)

    new_user = AuthUser(
        email=signup_data.email,
        firebaseUserId=firebase_uid,
        name=signup_data.name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return {
        "id": new_user.id,
        "email": new_user.email,
        "name": new_user.name,
        "firebaseUserId": new_user.firebaseUserId,
        "createdAt": new_user.createdAt,
        "isDeleted": new_user.isDeleted,
        "idToken": id_token
    }


def sign_in(signin_data: SigninRequest):
    db = next(get_auth_database())
    user = db.query(AuthUser).filter(AuthUser.email == signin_data.email, AuthUser.isDeleted == False).first()
    if not user:
        db.close()
        raise HTTPException(status_code=400, detail="User not registered")

    firebase_user = sign_in_user(signin_data.email, signin_data.password)
    if not firebase_user:
        db.close()
        raise HTTPException(status_code=400, detail="Invalid credentials")

    db.close()

    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "firebaseUserId": user.firebaseUserId,
        "createdAt": user.createdAt,
        "isDeleted": user.isDeleted,
        "idToken": firebase_user["idToken"]
    }


def forgot_password_fun(email: str):
    db = next(get_auth_database())
    user = db.query(AuthUser).filter(AuthUser.email == email, AuthUser.isDeleted == False).first()
    if not user:
        db.close()
        raise HTTPException(status_code=400, detail="User not registered")
    forgot_password(email)
    db.close()
    return {"message": "Password reset email sent successfully"}
