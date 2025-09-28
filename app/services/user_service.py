from app.models.auth import AuthUser
from app.database import get_auth_database


def get_all_users():
    db = get_auth_database()
    try:
        users = db.query(AuthUser).filter(AuthUser.isDeleted == False).all()
        return users
    finally:
        db.close()
