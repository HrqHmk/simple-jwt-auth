from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.user import UserTable
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection)-> None:
        self.__db_connection = db_connection
    
    def insert_user(self, username: str, password: str)-> None:
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

    def get_user_by_username(self, username: str)->  UserTable:
        with self.__db_connection as database:
            try:
                user = (
                    database.session
                        .query(UserTable)
                        .filter(UserTable.username == username)
                        .first()
                )

                return user
            except NoResultFound:
                return None
