from sqlalchemy import Column,Integer,String,Float,Text,DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime,timezone

Base = declarative_base()

class PromptHistory(Base):
    __tablename__ = "prompt_history"
    id = Column(Integer, primary_key=True,index=True)
    prompt = Column(text)
    response = Column(text)
    model = Column(String)
    tokens_used = Column(Integer)
    cost = Column(Float)
    created_at = Column(DateTime,default=datetime.now(timezone.utc))