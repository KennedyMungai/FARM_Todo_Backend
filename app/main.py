"""The entrypoint for the application"""
from beanie import init_beanie
from fastapi import FastAPI

from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)


@app.get("/", name="Home", tags=["Home"], description="Home endpoint")
async def home_endpoint_get() -> dict[str, str]:
    """Home endpoint"""
    return {"message": "Hello World"}
