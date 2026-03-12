from openai import AsyncOpenAI
from app.core.config import settings
from app.core.logging import logger
from app.providers.base_Provider import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        
    async def generate_response(self,prompt:str,model:str="gpt-4o-mini"):
        logger.info("Sending request to OpenAI")
        
        response = await self.client.chat.completions.create(
            model=model,
            messages=[
                {"role":"user","content":prompt}
            ]
        ) 
        
        text = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        
        return {
            "response":text,
            "tokens_used":tokens_used
        }


# response.choices
# The LLM returns multiple possible responses.
        
# response.usage 
# OpenAI return token usage
# 1. prompt_tokens
# 2. completion_tokens
# 3. total_tokens -> We choose this to compute token cost