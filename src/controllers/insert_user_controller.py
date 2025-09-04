from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.controllers.interfaces.insert_user_controller import InsertUserControllerInterface

class InsertUserController(InsertUserControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface)-> None:
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()
    
    def insert(self, username: str, password: str)->dict:
        hashed_password = self.__create_hash_password(password)
        self.__insert_new_user(username, hashed_password)
        return self.__format_response(username)

    def __create_hash_password(self, password: str):
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password

    def __insert_new_user(self, username: str, hashed_password: str)-> None:
        self.__user_repository.insert_user(username, hashed_password)
    
    def __format_response(self, username: str)-> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username
        }
