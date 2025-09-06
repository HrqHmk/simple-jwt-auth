from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.user import UserTable
from .user_repository import UserRepository

class MockConnection():
    def __init__(self)-> None:
        self.session =  UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(UserTable)],
                    [
                        UserTable(
                            username= "Jhon Doe",
                            password= "12345",
                        )
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_insert_user():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)
    repository.insert_user("Jhon Doe", "12345")

    mock_connection.session.add.assert_called_once()

def test_get_user_by_username():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)
    response = repository.get_user_by_username("Jhon Doe")

    mock_connection.session.query.assert_called_once_with(UserTable)
    mock_connection.session.filter.assert_called_once_with(UserTable.username == "Jhon Doe")
    assert response.username == "Jhon Doe"