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


@app.get("/")
def root():
    return {"message": "JIGAR APIs is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
