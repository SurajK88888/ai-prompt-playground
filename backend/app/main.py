from fastapi import FastAPI,Request
from app.core.config import settings
from app.core.logging import logger
from app.api.prompt_routes import router as prompt_routes

app = FastAPI(
    title= settings.APP_NAME,
    description="Test prompts across multiple LLM providers",
    version="1.0"
)

app.include_router(prompt_routes)

@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {
        "message": f"{settings.APP_NAME} Running",
        "environment": settings.ENVIRONMENT
    }