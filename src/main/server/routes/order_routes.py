from flask import Blueprint, request, jsonify
from src.main.composer.create_order_composer import create_order_composer
from src.main.composer.list_order_composer import list_order_composer
from src.views.http_types.http_request import HttpRequest
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.errors.error_handler import handle_errors

order_routes_bp = Blueprint("order_routes", __name__)

@order_routes_bp.route("/orders/<user_id>", methods=["POST"])
def create_order(user_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={ "user_id": user_id },
            tokens_infos=token_information,
            headers=request.headers
        )
        http_response = create_order_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@order_routes_bp.route("/orders/<user_id>", methods=["GET"])
def list_order(user_id):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            params={ "user_id": user_id },
            tokens_infos=token_information,
            headers=request.headers
        )
        http_response = list_order_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
