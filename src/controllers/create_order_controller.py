from src.models.sqlite.interfaces.order_repository import OrderRepositoryInterface

class CreateOrderController():
    def __init__(self, order_repository: OrderRepositoryInterface)-> None:
        self.__order_repository = order_repository
    
    def create(self, product: str, description: str)->dict:
        order_id = self.__create_new_order(product, description)
        return self.__format_response(order_id)

    def __create_new_order(self, product: str, description: str)-> int:
        order_id = self.__order_repository.create_order(product, description)
        return order_id
    
    def __format_response(self, order_id: int)-> dict:
        return {
            "type": "Order",
            "count": 1,
            "order_id": order_id
        }
