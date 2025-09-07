from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.main.server.routes.user_routes import user_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_routes_bp)
