import firebase_admin
from firebase_admin import credentials, auth
import os
import requests
from fastapi import HTTPException

GOOGLE_APIS_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key="
FIREBASE_API_KEY = "AIzaSyAwXSuTq-uqcP0J7VFiiab7BhaHB1MDwaA"


def initialize_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        cred_path = os.path.join(base_dir, "fast_api_firebase.json")
        if not os.path.exists(cred_path):
            raise FileNotFoundError(f"Service account file not found: {cred_path}")

        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)


def create_firebase_user(email: str, password: str):
    initialize_firebase()
    user = auth.create_user(
        email=email,
        password=password
    )
    return user.uid


def sign_in_user(email: str, password: str):
    url = f"{GOOGLE_APIS_URL}{FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def forgot_password(email: str):
    initialize_firebase()
    try:
        auth.generate_password_reset_link(email)
    except auth.UserNotFoundError:
        raise HTTPException(status_code=400, detail="User not registered")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error sending reset email: {str(e)}")

