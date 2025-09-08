import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .create_order_view import CreateOrderView

class MockController:
    def create(self, product: str, description: str, user_id: int):
        return { "something": "something" }

def test_handle_create_order():
    body = {
        "product": "Product Test",
        "description": "Test"
    }

    params = {
        "user_id": 1
    }

    headers = {
        "uid": 1
    }

    request = HttpRequest(body=body, params=params, headers=headers)

    mock_controller = MockController()
    view = CreateOrderView(mock_controller)

    response = view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == { "data": { "something": "something" }}
    assert response.status_code == 201
