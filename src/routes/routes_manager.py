from .auth_route import AuthRoute
from .user_route import UserRoute
class RoutesManager:
    def __init__(self, app):
        self.app = app
        self.auth_route = AuthRoute(app)
        self.user_route = UserRoute(app)
    def register_blueprints(self):
        self.app.register_blueprint(self.auth_route.auth, url_prefix="/auth")
        self.app.register_blueprint(self.user_route.user, url_prefix="/user")