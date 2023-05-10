"""The entrypoint for the application"""
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)


@app.on_event("startup")
async def startup():
    """Initialize the database"""
    db_client = AsyncIOMotorClient(f"{settings.MONGODB_URL}todolist")
    await init_beanie(database=db_client.get_default_database(), document_models=[])


@app.get("/", name="Home", tags=["Home"], description="Home endpoint")
async def home_endpoint_get() -> dict[str, str]:
    """Home endpoint"""
    return {"message": "Hello World"}
