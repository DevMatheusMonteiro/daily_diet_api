from utils.app_error import AppError
from utils.app_response import AppResponse
from flask_login import login_required
class ExceptionHandler:
    def __init__(self, app):
        self.app = app
    def handle_exceptions(self):
        @self.app.errorhandler(AppError)
        def handle_app_error(error):
            return AppResponse(message=error.message, status="error", status_code=error.status_code)
        @self.app.errorhandler(Exception)
        def handle_general_exception(error):
            return AppResponse(body={"details": str(error)}, message="An unexpected error occurred.",status="error", status_code=500)