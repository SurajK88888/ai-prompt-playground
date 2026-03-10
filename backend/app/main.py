from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title= settings.APP_NAME,
    description="Test prompts across multiple LLM providers",
    version="1.0"
)

@app.get("/")
async def root():
    return {
        "message": f"{settings.APP_NAME} Running",
        "environment": settings.ENVIRONMENT
    }
