from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def predict(self, text: str) -> str:
        pass