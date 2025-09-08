from src.controllers.interfaces.create_order_controller import CreateOrderControllerInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class CreateOrderView(ViewInterface):
    def __init__(self, controller:CreateOrderControllerInterface)-> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest)-> HttpResponse:
        user_id = http_request.params.get("user_id")
        header_user_id = http_request.headers.get("uid")
        product = http_request.body.get("product")
        description = http_request.body.get("description")

        self.__validade_inputs(user_id, product, description, header_user_id)
        response = self.__controller.create(product, description, user_id)
        return HttpResponse(body={ "data": response }, status_code=201)

    def __validade_inputs(
            self,
            user_id: any, 
            product: any,
            description: any,
            header_user_id: any
    )-> None:
        if (
            not user_id
            or not product
            or not description
            or not isinstance(product, str)
            or not isinstance(description, str)
            or int(header_user_id) != int(user_id)
        ):
            raise HttpBadRequestError("Invalid input")
