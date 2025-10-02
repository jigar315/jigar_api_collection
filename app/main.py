from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routers import auth, user
from app.firebaseConfig import initialize_firebase


initialize_firebase()

app = FastAPI(
    title="JIGAR APIs",
    description="Collection of authentication and user APIs",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.appRouter, prefix="/users", tags=["Users"])


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
