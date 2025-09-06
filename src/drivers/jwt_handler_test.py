from .jwt_handler import JwtHandler

def test_jwt_handle():
    jwt_handler = JwtHandler()
    body = {
        "username": "Jhon Doe"
    }

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]
