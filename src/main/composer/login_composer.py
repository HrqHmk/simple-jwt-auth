from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.controllers.login_controller import LoginController
from src.views.login_view import LoginView

def login_composer():
    model = UserRepository(db_connection_handler)
    controller = LoginController(model)
    view = LoginView(controller)

    return view

