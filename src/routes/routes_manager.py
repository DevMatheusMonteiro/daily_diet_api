from flask import Blueprint
from .auth_route import AuthRoute
class RoutesManager:
    def __init__(self, app):
        self.app = app
        self.auth_route = AuthRoute(app)
    def register_blueprints(self):
        self.app.register_blueprint(self.auth_route.auth, url_prefix="/auth")