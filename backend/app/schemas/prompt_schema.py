from pydantic import BaseModel,Field
from typing import Annotated, List, Dict, Any


class PromptRequest(BaseModel):
    # user_id: Annotated[str,Field(min_length=5,max_length=15)]
    prompt: Annotated[str,Field(min_length=0,max_length=3000)]
    model: Annotated[str,Field(default="gpt-4o-mini")]
    
class PromptResponse(BaseModel):
    response: Annotated[str,Field(default=" ")]
    token_used: Annotated[int,Field(default=0)]
    total_cost: Annotated[float,Field(default=0,ge=0)]
    

class CompareRequest(BaseModel):
    prompt: str
    models: List[str]


class CompareResponse(BaseModel):
    results: Dict[str, Any]
# In short: The Schema is the "Check" at the door. The Model is the "Storage" in the basement.