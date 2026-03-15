from fastapi import APIRouter
from app.services.llm_service import LLMService
from app.schemas.prompt_schema import PromptRequest,PromptResponse
from app.core.logging import logger

# Used to separate endpoints into modules.
router = APIRouter()
llmservice = LLMService()

@router.post("/prompt/test",response_model=PromptResponse)
async def test_prompt(request:PromptRequest):
    logger.info("Prompt received")
    result = await llmservice.generate(prompt=request.prompt,model=request.model)
    return result
