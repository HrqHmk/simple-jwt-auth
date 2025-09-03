from .insert_user_controller import InsertUserController

class MockUserRepository:
    def __init__(self)-> None:
        self.registry_user_attributes = {}

    def insert_user(self, username, password)-> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password

def test_insert_user():
    repository = MockUserRepository()
    controller = InsertUserController(repository)

    username = "Jhon Doe"
    password = "Password"

    response = controller.insert(username, password)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password
