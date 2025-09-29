from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import auth, user
from app.database import engine
from app.models.auth import AuthUser


@asynccontextmanager
async def lifespan():
    try:
        AuthUser.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error creating tables: {e}")
    yield


app = FastAPI(
    title="JIGAR APIs",
    lifespan=lifespan
)

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
