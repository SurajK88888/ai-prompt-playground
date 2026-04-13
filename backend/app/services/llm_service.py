from app.providers.openai_provider import OpenAIProvider
from app.providers.groq_provider import GroqProvider
from app.services.cache_service import CacheService
from app.core.logging import logger

import asyncio

class LLMService:
    def __init__(self):
        self.openai_provider = OpenAIProvider()
        self.groq_provider = GroqProvider()
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
        openai_result = await self.openai_provider.generate_response(prompt=prompt,model=model)
        # groq_result = await self.groq_provider.generate_response(prompt=prompt,model=model)
        
        # 3. Store in cache
        await self.cache_service.set(cache_key, openai_result)
        # await self.cache_service.set(cache_key, groq_result)
        
        print(result)
        # return {"openai_result": openai_result,"groq_result":groq_result}
        return openai_result
    
    async def compare(self, prompt:str,models:list):
        tasks=[]
        for model in models:
            if model == "openai":
                tasks.append(
                    await self.openai_provider.generate_response(prompt=prompt,model=model)
                )
            elif model == "groq":
                tasks.append(
                    await self.groq_provider.generate_response(prompt=prompt,model=model)
                )
        results = await asyncio.gather(*tasks)
        output = {}
        
        for model, result in zip(models, results):
            output[model] = result

        return {"results": output}