import pytest
from src.drivers.password_handler import PasswordHandler
from .login_controller import LoginController

USERNAME = "Jhon Doe"
PASSWORD = "passwordTest"
hashed_password = PasswordHandler().encrypt_password(PASSWORD)

class MockUser:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class MockUserRepository():
    def get_user_by_username(self, username: str):
        return MockUser(10, username, hashed_password)

def test_login():
    login_controller = LoginController(MockUserRepository())
    response = login_controller.login(USERNAME, PASSWORD)

    assert response["access"] is True
    assert response["username"] == USERNAME
    assert response["token"] is not None

def test_create_with_invalid_credentials():
    login_controller = LoginController(MockUserRepository())
    
    with pytest.raises(Exception):
        login_controller.login(USERNAME, "wrong")
