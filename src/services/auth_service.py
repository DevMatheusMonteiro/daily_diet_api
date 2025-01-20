from utils.app_error import AppError
from repositories.user_repository import UserRepository
from flask_login import login_user, logout_user
import bcrypt
class AuthService:
    @staticmethod
    def login(data:dict):
        email = data.get("email")
        password = data.get("password")
        if email and password:
            user = UserRepository.get_user_by_email(email)
            if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
                login_user(user)
                return user
        raise AppError(message="Credenciais inválidas.", status_code=401)
    @staticmethod
    def logout():
        logout_user()