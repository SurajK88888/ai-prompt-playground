from groq import AsyncGroq
from app.core.config import settings
from app.core.logging import logger
from app.providers.base_Provider import BaseLLMProvider
from app.core.cost_tracker import calculate_cost

class GroqProvider(BaseLLMProvider):
    def __init__(self):
        client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        pass

    async def generate_response(self, prompt: str, model: str = "mixtral"):

        logger.info("Sending request to Groq")
        
        # response = client.chat.completions.create(
        #     model="llama-3.3-70b-versatile",
        #     messages=[
        #         {
        #         "role": "user",
        #          "content": prompt,
        #          }
        #     ],  
        # )

        # text  = response.choices[0].message.content
        # prompt_tokens = response.usage.prompt_tokens
        # completion_tokens = response.usage.completion_tokens
        # total_tokens = response.usage.total_tokens
        
        # total_cost = calculate_cost(prompt_tokens=prompt_tokens,completion_tokens=completion_tokens,model=model)
       
        # logger.info(f"Tokens used: {total_tokens}")
        # logger.info(f"Cost: ${total_cost}")

        return {
            "response": f"[Groq simulated] {prompt}",
            "tokens_used": 100,
            "cost": 0.0
        }