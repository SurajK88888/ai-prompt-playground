from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Abstract base class for all LLM providers.
    """
    @abstractmethod
    def generate_response(self,prompt:str,model:str):
        pass