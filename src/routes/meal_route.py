from flask import Blueprint
from controllers.meal_controller import MealController
from handlers.login_required_handler import LoginRequiredHandler
class MealRoute:
    def __init__(self, app):
        self.app = app
        self.meal = Blueprint("meal", __name__)
        self.setup_routes()
    def setup_routes(self):
        @self.meal.route("/", methods=["POST"])
        @LoginRequiredHandler.custom_login_required
        def create_meal():
            return MealController.create_meal()
        @self.meal.route("/<int:id>",methods=["GET"])
        @LoginRequiredHandler.custom_login_required
        def get_user_meal_by_id(id):
            return MealController.get_user_meal_by_id(id)
        @self.meal.route("/search_user_meals", methods=["GET"])
        @LoginRequiredHandler.custom_login_required
        def search_user_meals():
            return MealController.search_user_meals()
        @self.meal.route("/<int:id>", methods=["PUT"])
        @LoginRequiredHandler.custom_login_required
        def update_meal(id:int):
            return MealController.update_meal(id)
        @self.meal.route("/<int:id>", methods=["DELETE"])
        @LoginRequiredHandler.custom_login_required
        def delete_meal(id):
            return MealController.delete_meal(id)