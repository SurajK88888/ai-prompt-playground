from app.providers.openai_provider import OpenAIProvider
from app.services.cache_service import CacheService
from app.core.logging import logger

class LLMService:
    def __init__(self):
        self.openai_provider = OpenAIProvider()
        self.cache_service = CacheService()
    
    async def generate(self,prompt:str,model:str):
        
        cache_key = f"{model}:{prompt}"
        
        # 1. Check cache
        cached = await self.cache_service.get(cache_key)
        
        if cached:
            logger.info("Cache HIT")
            return cached
        
        logger.info("Cache MISS")
        
        # 2. Call LLm
        result = await self.openai_provider.generate_response(prompt=prompt,model=model)
        
        # 3. Store in cache
        await self.cache_service.set(cache_key, result)
        print(result)
        return result