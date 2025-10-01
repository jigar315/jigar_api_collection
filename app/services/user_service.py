from app.models.auth import AuthUser
from app.database import get_auth_database


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
        return user
    finally:
        db.close()