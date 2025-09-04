from abc import ABC, abstractmethod

class InsertUserControllerInterface(ABC):
    @abstractmethod
    def insert(self, username: str, password: str)->dict:
        pass
