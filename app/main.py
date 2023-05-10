"""The entrypoint for the application"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/", name="Home", tags=["Home"], description="Home endpoint")
async def home_endpoint_get() -> dict[str, str]:
    """Home endpoint"""
    return {"message": "Hello World"}
