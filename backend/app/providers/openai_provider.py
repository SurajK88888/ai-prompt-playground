from openai import AsyncOpenAI
from app.core.config import settings
from app.core.logging import logger
from app.providers.base_Provider import BaseLLMProvider
from app.core.cost_tracker import calculate_cost


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
        prompt_token = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens
        
        total_cost = calculate_cost(prompt_tokens=prompt_tokens,completion_tokens=completion_tokens,model=model)
       
        logger.info(f"Tokens used: {total_tokens}")
        logger.info(f"Cost: ${cost}")
        
        return {
            "response":text,
            "tokens_used":total_tokens,
            "total_cost":total_cost
        }


# response.choices
# The LLM returns multiple possible responses.
        
# response.usage 
# OpenAI return token usage
# 1. prompt_tokens
# 2. completion_tokens
# 3. total_tokens -> We choose this to compute token cost