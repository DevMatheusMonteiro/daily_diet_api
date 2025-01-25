from .auth_route import AuthRoute
from .user_route import UserRoute
from .meal_route import MealRoute
class RoutesManager:
    def __init__(self, app):
        self.app = app
        self.auth_route = AuthRoute(app)
        self.user_route = UserRoute(app)
        self.meal_route = MealRoute(app)
    def register_blueprints(self):
        self.app.register_blueprint(self.auth_route.auth, url_prefix="/auth")
        self.app.register_blueprint(self.user_route.user, url_prefix="/user")
        self.app.register_blueprint(self.meal_route.meal, url_prefix="/meal")