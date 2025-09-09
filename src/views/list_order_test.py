from unittest.mock import MagicMock
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .list_order import ListOrderView

class MockController:
    def list(self, user_id: int):
        return { "something": "something" }

def test_handle_list_order():
    params = {
        "user_id": 1
    }

    headers = {
        "uid": 1
    }

    request = HttpRequest(headers=headers, params=params)
    mock_controller = MockController()
    view = ListOrderView(mock_controller)

    response = view.handle(request)
    assert isinstance(response, HttpResponse)
    assert response.body == { "data": { "something": "something" }}
    assert response.status_code == 201


def test_handle_calls_controller_with_correct_user_id():
    request = HttpRequest(headers={"uid": 42}, params={"user_id": 42})
    mock_controller = MagicMock()
    mock_controller.list.return_value = {"ok": True}

    view = ListOrderView(mock_controller)
    view.handle(request)

    mock_controller.list.assert_called_once_with(42)
