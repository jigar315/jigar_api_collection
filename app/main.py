from fastapi import FastAPI
from app.routers import auth, user
from app.database import engine
from app.models.auth import AuthUser

AuthUser.metadata.create_all(bind=engine)

app = FastAPI(title="JiGAR APIs")

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    user.appRouter,
    prefix="/users",
    tags=["Users"]
)