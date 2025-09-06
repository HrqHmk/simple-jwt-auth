import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .insert_user_view import InsertUserView

class MockController:
    def insert(self, username: str, password: str):
        return { "something": "something" }

def test_handle_user_register():
    body = {
        "username": "Jhon Doe",
        "password": "12345"
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    view = InsertUserView(mock_controller)

    response = view.handle(request)
    
    assert isinstance(response, HttpResponse)
    assert response.body == { "data": { "something": "something" }}
    assert response.status_code == 201

def test_handle_user_register_with_validation_error():
    body = {
        "password": "12345"
    }

    request = HttpRequest(body=body)

    mock_controller = MockController()
    view = InsertUserView(mock_controller)

    with pytest.raises(Exception):
        view.handle(request)
