from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = settings.DATABASE_URL

# .env → config.py → database.py

# Create an SQL database
# Lazy connecting is done internally
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Explanation

# Engine: Connects to the database.

# Base: Serves as the foundation for model definitions.

# Session: Manages transactions and queries.

# Models: Map Python classes to database tables.