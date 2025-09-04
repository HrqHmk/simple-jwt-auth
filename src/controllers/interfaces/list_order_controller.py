from abc import ABC, abstractmethod

class ListOrderControllerInterface(ABC):
    @abstractmethod
    def list(self, user_id: int)->dict:
        pass
