from flask import Blueprint
from controllers.user_controller import UserController
from handlers.login_required_handler import LoginRequiredHandler
class UserRoute:
    def __init__(self, app):
        self.app = app
        self.user = Blueprint("user", __name__)
        self.setup_routes()
    def setup_routes(self):
        @self.user.route("/create_user", methods=["POST"])
        def create_user():
            return UserController.create_user()
        @self.user.route("/<int:id>",methods=["GET"])
        @LoginRequiredHandler.custom_login_required
        def get_user_by_id(id):
            return UserController.get_user_by_id(id)