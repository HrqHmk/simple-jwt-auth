from src.models.sqlite.entities.user import UserTable
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection)-> None:
        self.__db_connection = db_connection
    
    def insert_user(self, username: str, password: str):
        with self.__db_connection as database:
            try:
                user_data = UserTable(
                    username=username,
                    password=password
                )

                database.session.add(user_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
