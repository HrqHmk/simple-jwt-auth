from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.order_repository import OrderRepository
from src.controllers.list_order_controller import ListOrderController
from src.views.list_order import ListOrderView

def list_order_composer():
    model = OrderRepository(db_connection_handler)
    controller = ListOrderController(model)
    view = ListOrderView(controller)

    return view
