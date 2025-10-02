from typing import Optional

from fastapi import HTTPException

from app.models.auth import AuthUser
from app.database import get_auth_database
from app.firebaseConfig import delete_user
from app.core.auth_middleware import verify_firebase_token


def get_all_users():
    db = next(get_auth_database())
    try:
        users = db.query(AuthUser).filter(AuthUser.isDeleted == False).all()
        return users
    finally:
        db.close()


def get_user_by_id(user_id: str):
    db = next(get_auth_database())
    try:
        user = db.query(AuthUser).filter(AuthUser.id == user_id).first()
        if user is None:
            db.close()
            raise HTTPException(status_code=400, detail="User Not found")
        return user
    finally:
        db.close()


def delete_user_from_db(user_id: str):
    db = next(get_auth_database())
    try:
        user = db.query(AuthUser).filter(AuthUser.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        deleteUser = delete_user(user.firebaseUserId)

        if deleteUser == False:
            return HTTPException(status_code=404, detail="Something want wrong!")

        user.isDeleted = True
        db.commit()
        db.refresh(user)
        db.delete(user)
        return user
    finally:
        db.close()


def update_user_by_id(userId: str, name: Optional[str] = None):
    db = next(get_auth_database())
    try:
        user = db.query(AuthUser).filter(AuthUser.id == userId).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if name is not None:
            user.name = name

        db.commit()
        db.refresh(user)
        return user

    finally:
        db.close()


def get_user_by_firebase_uid(firebase_uid: str):
    db = next(get_auth_database())
    try:
        user = db.query(AuthUser).filter(AuthUser.firebaseUserId == firebase_uid).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    finally:
        db.close()
