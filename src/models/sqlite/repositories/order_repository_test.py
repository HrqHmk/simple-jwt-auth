from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.order import OrderTable
from .order_repository import OrderRepository


class MockConnection():
    def __init__(self)-> None:
        self.session =  UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(OrderTable)],
                    [
                        OrderTable(product="PRODUCT1", description="DESCRIPTION1", user_id=1),
                        OrderTable(product="PRODUCT2", description="DESCRIPTION2", user_id=1)
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_create_order():
    mock_connection = MockConnection()
    repository = OrderRepository(mock_connection)

    def fake_add(obj):
        obj.id = 10  # simula que o flush preencheu
    mock_connection.session.add.side_effect = fake_add
    response = repository.create_order("Computer", "Dell computer", 1)

    mock_connection.session.add.assert_called_once()
    response = repository.create_order("Computer", "Dell computer", 1)
    assert response == 10

def test_list_orders_by_user():
    mock_connection = MockConnection()
    repository = OrderRepository(mock_connection)
    response = repository.list_orders_by_user(1)

    mock_connection.session.query.assert_called_once_with(OrderTable)
    assert response[0].product == "PRODUCT1"
