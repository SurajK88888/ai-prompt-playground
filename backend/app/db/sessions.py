from app.db.database import AsyncSessionLocal

async def get_db():
    async with AsyncSessionLocal as session:
        yield session
        
# This provides database session dependency for FastAPI.
# session:- A workplace that is devoted to a particular task for a period of time. 
# So that you can perform operation and work.