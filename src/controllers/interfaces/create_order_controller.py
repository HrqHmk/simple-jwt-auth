from abc import ABC, abstractmethod

class CreateOrderControllerInterface(ABC):
    @abstractmethod
    def create(self, product: str, description: str, user_id: int)->dict:
        pass
