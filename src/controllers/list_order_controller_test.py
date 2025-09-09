from src.models.sqlite.entities.order import OrderTable
from .list_order_controller import ListOrderController

class MockLegalOrderRepository:
    def list_orders_by_user(self, user_id:int):
        return [
            OrderTable(
                product="Product 1", 
                description="Product Test 1",
                created_at="2025-01-01",
                id=1,
                user_id= user_id
            ),
            OrderTable(
                product="Product 2", 
                description="Product Test 2",
                created_at="2025-02-02",
                id=2,
                user_id= user_id
            ),
        ]

def test_list_orders():
    controller = ListOrderController(MockLegalOrderRepository())
    response = controller.list(1)

    expected_response = {
        "data":{
            "type": "Orders",
            "count": 2,
            "attributes": [
                { 
                    "product": "Product 1", 
                    "description":"Product Test 1",
                    "order_date":"2025-01-01",
                    "order_id":1
                },
                { 
                    "product": "Product 2", 
                    "description":"Product Test 2",
                    "order_date":"2025-02-02",
                    "order_id":2
                },
            ]
        }
    }

    assert response == expected_response
