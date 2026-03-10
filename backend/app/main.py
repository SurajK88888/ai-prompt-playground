from fastapi import FastAPI

app = FastAPI(
    title="AI Prompt Playground API",
    description="Test prompts across multiple LLM providers",
    version="1.0"
)

@app.get("/")
async def root():
    return {"message": "AI Prompt Playground API Running"}