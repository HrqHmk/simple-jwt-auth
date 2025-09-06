from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.insert_user_composer import insert_user_composer

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}, 200)

@user_routes_bp.route("/user/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = insert_user_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception:
        return jsonify(http_response.body), http_response.status_code
