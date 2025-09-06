from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.controllers.insert_user_controller import InsertUserController
from src.views.insert_user_view import InsertUserView

def insert_user_composer():
    model = UserRepository(db_connection_handler)
    controller = InsertUserController(model)
    view = InsertUserView(controller)

    return view
