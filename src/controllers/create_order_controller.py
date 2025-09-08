from src.controllers.interfaces.create_order_controller import CreateOrderControllerInterface
from src.models.sqlite.interfaces.order_repository import OrderRepositoryInterface

class CreateOrderController(CreateOrderControllerInterface):
    def __init__(self, order_repository: OrderRepositoryInterface)-> None:
        self.__order_repository = order_repository
    
    def create(self, product: str, description: str, user_id: int)->dict:
        order_id = self.__create_new_order(product, description, user_id)
        return self.__format_response(order_id)

    def __create_new_order(self, product: str, description: str, user_id: int)-> int:
        order_id = self.__order_repository.create_order(product, description, user_id)
        return order_id
    
    def __format_response(self, order_id: int)-> dict:
        return {
            "type": "Order",
            "count": 1,
            "order_id": order_id
        }
