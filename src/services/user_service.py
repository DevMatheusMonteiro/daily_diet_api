from repositories.user_repository import UserRepository, User
from dto.input.user_dto_input import UserDTOInput
from utils.app_error import AppError
import bcrypt
class UserService:
    @staticmethod
    def create_user(user_dto_input:UserDTOInput):
        email = user_dto_input.email
        username = user_dto_input.username
        password = user_dto_input.password
        if not email or not username or not password:
            raise AppError("Campos Inválidos.")
        user_by_email = UserRepository.get_user_by_email(email)
        user_by_username = UserRepository.get_user_by_username(username)
        if user_by_email:
            raise AppError("Email já cadastrado.")
        if user_by_username:
            raise AppError("Nome de usuário já cadastrado.")
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt()).decode()
        new_user = User(email=email, username=username, password=hashed_password)
        created_user_id = UserRepository.create_user(new_user)
        return created_user_id
    @staticmethod
    def get_user_by_id(user_id:int):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise AppError("Usuário não encontrado.", 404)
        return user
    @staticmethod
    def search_users(search):
        users = UserRepository.search_users(search)
        if not users:
            raise AppError("Nenhum usuário encontrado.", 404)
        return users
    @staticmethod
    def update_user(user_dto_input:UserDTOInput, current_user_id:int, current_password:str=None):
        user = UserRepository.get_user_by_id(user_dto_input.id)
        if not user or user.id != current_user_id:
            raise AppError("Usuário não encontrado.", 404)
        email = user_dto_input.email
        username = user_dto_input.username
        current_password = current_password
        new_password = user_dto_input.password
        if email and email.strip() != "":
            user_by_email = UserRepository.get_user_by_email(email)
            if user_by_email and user_dto_input.id != user_by_email.id:
                raise AppError("Email já cadastrado.")
        if username and username.strip() != "":
            user_by_username = UserRepository.get_user_by_username(username)
            if user_by_username and user_dto_input.id != user_by_username.id:
                raise AppError("Nome de usuário já cadastrado.")
        if new_password and new_password.strip() != "":
            if not current_password or not current_password.strip():
                raise AppError("Informe a senha atual.")
            if not bcrypt.checkpw(str.encode(current_password), str.encode(user.password)):
                raise AppError("Senha atual inválida.")
            user.password = bcrypt.hashpw(str.encode(new_password), bcrypt.gensalt()).decode()
        user.email = email or user.email
        user.username = username or user.username
        UserRepository.update_user(user)
    @staticmethod
    def delete_user(user_id:int):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise AppError("Usuário não encontrado.", 404)
        UserRepository.delete_user(user)
        return user.id