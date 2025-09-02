from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .user_repository import UserRepository

class MockConnection():
    def __init__(self)-> None:
        self.session =  UnifiedAlchemyMagicMock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_insert_user():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)
    repository.insert_user("Jhon Doe", "12345")

    mock_connection.session.add.assert_called_once()
