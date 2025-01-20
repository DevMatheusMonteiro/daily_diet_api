from flask import Blueprint
from flask_login import LoginManager
from controllers.auth_controller import AuthController
from handlers.login_required_handler import LoginRequiredHandler
from repositories.user_repository import UserRepository
class AuthRoute:
    def __init__(self, app):
        self.app = app
        self.auth = Blueprint("auth", __name__)
        self.login_manager = LoginManager()  
        self.login_manager.init_app(app)
        self.login_manager.login_view = "auth.login"
        @self.login_manager.user_loader
        def load_user(user_id):
            return UserRepository.get_user_by_id(user_id)
        self.setup_routes()
    
    def setup_routes(self):
        @self.auth.route("/login", methods=["POST"])
        def login():
            return AuthController.login()
        @self.auth.route("/logout",methods=["GET"])
        @LoginRequiredHandler.custom_login_required
        def logout():
            return AuthController.logout()