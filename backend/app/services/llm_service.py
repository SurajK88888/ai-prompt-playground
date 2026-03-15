from app.providers.openai_provider import OpenAIProvider


class LLMService:
    def __init__(self):
        self.openai_provider = OpenAIProvider()
    
    async def generate(self,prompt:str,model:str):
        result = await self.openai_provider.generate_response(prompt=prompt,model=model)
        print(result)
        return result