from typing import List
from src.models.sqlite.interfaces.order_repository import OrderRepositoryInterface
from src.models.sqlite.entities.order import OrderTable

class ListOrderController():
    def __init__(self, order_repository: OrderRepositoryInterface)-> None:
        self.__order_repository = order_repository
    
    def list(self, user_id: int)->dict:
        orders = self.__get_orders_in_db_by_user(user_id)
        return self.__format_response(orders)

    def __get_orders_in_db_by_user(self, user_id: int)-> List[OrderTable]:
        orders = self.__order_repository.list_orders_by_user(user_id)
        return orders
    
    def __format_response(self, orders: List[OrderTable])-> dict:
        formatted_response = []
        for order in orders:
            formatted_response.append({
                "product": order.product,
                "description": order.description,
                "order_date": order.order_date,
                "order_id": order.id
            })
        
        return {
            "data": {
                "type": "Orders",
                "count": len(formatted_response),
                "attributes": formatted_response
            }
        }
