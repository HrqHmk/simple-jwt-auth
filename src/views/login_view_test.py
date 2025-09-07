import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .login_view import LoginView

class MockController:
    def login(self, username: str, password: str):
        return { "something": "something" }

def test_login():
    body = {
        "username": "Jhon Doe",
        "password": "12345"
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_view = LoginView(mock_controller)

    response = login_view.handle(request)
    
    assert isinstance(response, HttpResponse)
    assert response.body == { "data": { "something": "something" }}
    assert response.status_code == 200

def test_login_with_validation_error():
    body = {
        "password": "12345"
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_view = LoginView(mock_controller)

    with pytest.raises(Exception):
        login_view.handle(request)
