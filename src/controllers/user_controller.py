from services.user_service import UserService
from dto.input.user_dto_input import UserDTOInput
from dto.output.user_dto_output import UserDTOOutput
from utils.app_response import AppResponse
from flask import request
from flask_login import current_user
class UserController:
    @staticmethod
    def create_user():
        data = request.json
        # data = {"email": "matheus@email.com", "username": "matheus", "password":"123"}
        user_dto_input = UserDTOInput()
        user_dto_input.map_object(data)
        created_user_id = UserService.create_user(user_dto_input)
        return AppResponse(message="Usuário adicionado com sucesso.", status_code=201, body={"user_id": created_user_id})
    @staticmethod
    def get_user_by_id():
        user = UserService.get_user_by_id(current_user.id)
        user_dto_output = UserDTOOutput()
        user_dto_output.map_object(user.to_dict())
        return user_dto_output.model_dump()
    @staticmethod
    def get_user_by_email():
        pass