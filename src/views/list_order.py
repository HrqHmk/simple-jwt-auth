from src.controllers.interfaces.list_order_controller import ListOrderControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface

class ListOrderView(ViewInterface):
    def __init__(self, controller: ListOrderControllerInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest)-> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        self.__validate_headers(user_id, header_user_id)

        response = self.__controller.list(user_id)
        return HttpResponse(body={ "data": response }, status_code=201)

    def __validate_headers(self, user_id: any, header_user_id)->None:
        if (
            not user_id
            or int(header_user_id) != int(user_id)
        ):
            raise HttpBadRequestError("Invalid headers")
