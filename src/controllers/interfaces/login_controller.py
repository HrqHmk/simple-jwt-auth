from abc import ABC, abstractmethod

class LoginControllerInterface(ABC):
    @abstractmethod
    def login(self, username:str, password:str)->dict:
        pass
