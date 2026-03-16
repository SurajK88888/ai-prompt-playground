import asyncio
from app.db.database import engine
from app.models.prompt_model import Base


async def init_models():
    async with engine.begin() as connection:
        connection.run_sync(Base.metadata.create_all)


asyncio.run(init_models())    