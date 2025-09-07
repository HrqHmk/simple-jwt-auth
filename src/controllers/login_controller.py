from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface
from src.models.sqlite.entities.user import UserTable
from src.errors.types.http_unauthorized import HttpUnauthorizedError
from .interfaces.login_controller import LoginControllerInterface

class LoginController(LoginControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface)->None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()
    
    def login(self, username: str, password: str)->dict:
        user = self.__verify_credentials(username, password)
        token = self.__create_jwt_token(user.id)
        return self.__format_response(user.username, token)

    def __verify_credentials(self, username: str, password: str)-> UserTable:
        user = self.__find_user(username)
        hased_password = user.password
        self.__verify_correct_password(password, hased_password)
        return user
    
    def __find_user(self, username: str)-> UserTable:
        user = self.__user_repository.get_user_by_username(username)
        if not user:
            raise HttpUnauthorizedError("Invalid Credentials")

        return user

    def __verify_correct_password(self, password: str, hashed_password: str)-> None:
        is_password_correct = self.__password_handler.check_password(password, hashed_password)
        if not is_password_correct:
            raise HttpUnauthorizedError("Invalid Credentials")

    def __create_jwt_token(self, user_id: int)-> str:
        payload = { "user_id": user_id}
        token = self.__jwt_handler.create_jwt_token(payload)
        return token

    def __format_response(self, username: str, token: str)-> dict:
        return {
            "access": True,
            "username": username,
            "token": token
        }
