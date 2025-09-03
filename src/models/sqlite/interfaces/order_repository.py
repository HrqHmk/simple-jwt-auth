from abc import ABC, abstractmethod
from src.models.sqlite.entities.order import OrderTable

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create_order(
        self,
        product:str,
        description:str,
        user_id: int
    )-> None:
        pass
    
    @abstractmethod
    def list_orders_by_user(self, user_id)-> list[OrderTable]:
        pass
