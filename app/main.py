from fastapi import FastAPI
from app.routers import auth, user

app = FastAPI(title="JIGAR APIs")

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

handler = app
