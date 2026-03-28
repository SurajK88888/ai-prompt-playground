from sqlalchemy import Column,Integer,String,Float,Text,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime,timezone

# 1. The Registry (The Parent)
Base = declarative_base()

# 2. The Blueprint (The Table)
class PromptHistory(Base):
    __tablename__ = "prompt_history"
    id = Column(Integer, primary_key=True,index=True)
    prompt = Column(Text)
    response = Column(Text)
    model = Column(String)
    tokens_used = Column(Integer)
    cost = Column(Float)
    created_at = Column(DateTime,default=datetime.now(timezone.utc))
    
# In short: The Schema is the "Check" at the door. The Model is the "Storage" in the basement.
    