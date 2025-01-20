from flask_login import current_user
from functools import wraps
from utils.app_error import AppError
class LoginRequiredHandler:
    @staticmethod
    def custom_login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                raise AppError(message="Acesso não autorizado. Por favor, realize o login.", status_code=401)
            return f(*args, **kwargs)
        return decorated_function