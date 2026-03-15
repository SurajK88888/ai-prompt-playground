MODEL_PRICING = {
    "gpt-4o-mini":{
        "input": 0.00000015,
        "output": 0.00000060
    }
}

def calculate_cost(prompt_tokens:str,completion_tokens:str,model:str):
    """
    Calculate the cost of an LLM request.
    """
    
    pricing = MODEL_PRICING.get(model)
    
    if not pricing:
        return 0
    
    input_cost = prompt_tokens*pricing.get("input",0)
    output_cost = prompt_tokens*pricing.get("output",0)
    
    total_cost = input_cost + output_cost
    return round(total_cost,8)