from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, username:str, password:str)-> None:
        pass
