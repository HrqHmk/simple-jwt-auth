from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.order_repository import OrderRepository
from src.controllers.create_order_controller import CreateOrderController
from src.views.create_order_view import CreateOrderView

def create_order_composer():
    model = OrderRepository(db_connection_handler)
    controller = CreateOrderController(model)
    view = CreateOrderView(controller)

    return view
