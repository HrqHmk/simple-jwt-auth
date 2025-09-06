from abc import ABC, abstractmethod
from src.models.sqlite.entities.user import UserTable

class UserRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(self, username:str, password:str)-> None:
        pass
    
    @abstractmethod
    def get_user_by_username(self, username: str)-> UserTable:
        pass
