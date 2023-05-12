"""The entrypoint for the application"""
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from auth.jwt import auth_router
from core.config import settings
from models.user_model import User
from routers.user_router import user_router

app = FastAPI(
    title=settings.PROJECT_NAME,
)


@app.on_event("startup")
async def startup():
    """Initialize the database"""
    db_client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(database=db_client.todolist, document_models=[User])


@app.get("/", name="Home", tags=["Home"], description="Home endpoint")
async def home_endpoint_get() -> dict[str, str]:
    """Home endpoint"""
    return {"message": "Hello World"}


# The users router
app.include_router(user_router)
app.include_router(auth_router)
