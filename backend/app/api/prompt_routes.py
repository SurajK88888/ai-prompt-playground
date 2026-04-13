from fastapi import APIRouter,Depends
from app.services.llm_service import LLMService
from app.schemas.prompt_schema import PromptRequest,PromptResponse
from app.schemas.prompt_schema import CompareRequest, CompareResponse
from app.core.logging import logger

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.prompt_repository import PromptRepository
from app.db.sessions import get_db

# Used to separate endpoints into modules.
router = APIRouter()
llmservice = LLMService()
prompt_repo = PromptRepository()

@router.post("/prompt/test",response_model=PromptResponse)
async def test_prompt(request:PromptRequest,db: AsyncSession = Depends(get_db)):
    logger.info("Prompt received")
    result = await llmservice.generate(prompt=request.prompt,model=request.model)
    
    await prompt_repo.save_repository(
        db=db,
        prompt=request.prompt,
        response=result.get("response"),
        model=request.model,
        tokens=result.get("tokens_used"),
        cost=result.get("total_cost")
    )
    
    return result

@router.post("/prompt/compare", response_model=CompareResponse)
async def compare_prompt(request: CompareRequest):

    logger.info("Multi-model comparison request received")

    result = await llmservice.compare(
        prompt=request.prompt,
        models=request.models
    )

    return result