import os
from dotenv import load_dotenv

# Loads variables from .env into Python environment.
load_dotenv()

# Why Use a Settings Class?
# Instead of: os.getenv("OPENAI_API_KEY") everywhere,
# We use: settings.OPENAI_API_KEY, (Cleaner and scalable).
class Settings:
    """
    Central configuration system for the application.
    """
    
    APP_NAME:str = os.getenv("APP_NAME","AI Prompt Playground")
    ENVIRONMENT:str = os.getenv("ENVIRONMENT","development")
    OPENAI_API_KEY:str = os.getenv("OPENAI_API_KEY")
    LOG_LEVEL:str = os.getenv("LOG_LEVEL", "INFO")    
    
# Singleton settings object
settings = Settings()