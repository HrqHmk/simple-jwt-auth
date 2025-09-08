from .create_order_controller import CreateOrderController

class MockUserRepository:
    def __init__(self)-> None:
        self.registry_order_attributes = {}

    def create_order(self, product, description, user_id)-> int:
        self.registry_order_attributes["product"] = product
        self.registry_order_attributes["description"] = description
        self.registry_order_attributes["user_id"] = user_id
        order_id = 1
        self.registry_order_attributes["order_id"] = order_id
        return order_id

def test_create_order():
    repository = MockUserRepository()
    controller = CreateOrderController(repository)

    product = "Product"
    description = "Product Test"

    response = controller.create(product, description, 1)

    assert response["type"] == "Order"
    assert response["order_id"] == 1
