from src.models.sqlite.entities.order import OrderTable
from src.models.sqlite.interfaces.order_repository import OrderRepositoryInterface

class OrderRepository(OrderRepositoryInterface):
    def __init__(self, db_connection)-> None:
        self.__db_connection = db_connection
    
    def create_order(self, product: str, description: str, user_id: int)-> int:
        with self.__db_connection as database:
            try:
                order_data = OrderTable(
                    product=product,
                    description=description,
                    user_id=user_id
                )

                database.session.add(order_data)
                database.session.commit()
                return order_data.id
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_orders_by_user(self, user_id: int)->list[OrderTable]:
        with self.__db_connection as database:
            orders = (
                database.session
                    .query(OrderTable)
                    .filter(OrderTable.user_id == user_id)
                    .all()
            )
            return orders
