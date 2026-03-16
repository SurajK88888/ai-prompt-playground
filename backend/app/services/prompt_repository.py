from sqlalchemy.ext.asyncio import AsyncSession
from app.models.prompt_model import PromptHistory


class PromptRepository:
    async def save_repository(self,db:AsyncSession,prompt:str,response:str,model:str,tokens:int,cost:float):
        record = PromptHistory(
            prompt=prompt,
            response=response,
            model=model,
            tokens_used=tokens,
            cost=cost
        )

        db.add(record)

        await db.commit()

        await db.refresh(record)

        return record