import cohere
from app.core.config import settings
from app.core.logging import logger
from app.providers.base_Provider import BaseLLMProvider
from app.core.cost_tracker import calculate_cost

class CohereProvider(BaseLLMProvider):
    def __init__(self):
        # self.client = cohere.ClientV2(api_key=settings.COHERE_API_KEY)
        pass
    
    async def generate_response(self,prompt:str,model:str):
        logger.info("Sending request to Cohere")
        
        # response = await co.chat(
        # # model="command-a-03-2025", 
        # model=model, 
        # messages=[{"role": "user", "content": prompt}]
        # )

        # text  = response.message.content[0].text
        # prompt_tokens = co.tokenize(text=prompt)
        # completion_tokens = co.tokenize(text=text)
        # total_tokens = prompt_tokens + completion_tokens
        
        # total_cost = calculate_cost(prompt_tokens=prompt_tokens,completion_tokens=completion_tokens,model=model)
       
        # logger.info(f"Tokens used: {total_tokens}")
        # logger.info(f"Cost: ${total_cost}")
        
        return {
            "response":"AI is a digital working model, which are capable of thicking, taking decision based on given scenerio. ",
            "tokens_used": 15,
            "total_cost": 25
        }
   
