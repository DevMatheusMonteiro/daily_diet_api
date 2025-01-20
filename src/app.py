from flask import Flask
from config import Config
from database import db
from routes.routes_manager import RoutesManager
from utils.app_response import AppResponse
from handlers.exception_handler import ExceptionHandler
from models.meal import Meal
from models.user import User
app = Flask(__name__)
app.response_class = AppResponse
app.config.from_object(Config)
exception_handler = ExceptionHandler(app)
exception_handler.handle_exceptions()
routes_manager = RoutesManager(app)
routes_manager.register_blueprints()
db.init_app(app)
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)