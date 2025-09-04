from abc import ABC, abstractmethod

class CreateOrderControllerInterface(ABC):
    @abstractmethod
    def create(self, product: str, description: str)->dict:
        pass
