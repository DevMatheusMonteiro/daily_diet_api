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
        user_dto_input = UserDTOInput()
        user_dto_input.map_object(data)
        created_user_id = UserService.create_user(user_dto_input)
        return AppResponse(message="Usuário adicionado com sucesso.", status_code=201, body={"user_id": created_user_id})
    @staticmethod
    def get_user_by_id(id:int):
        user = UserService.get_user_by_id(id)
        user_dto_output = UserDTOOutput()
        user_dto_output.map_object(user.to_dict())
        return AppResponse(body={"user": user_dto_output.model_dump()})
    @staticmethod
    def search_users():
        data = request.args
        search = data.get("search")
        users = UserService.search_users(search)
        user_dto_output = UserDTOOutput()
        return AppResponse(body={"users": [user_dto_output.map_object(user.to_dict()).model_dump() for user in users]})
    @staticmethod
    def update_user(id:int):
        data = request.json
        user_dto_input = UserDTOInput()
        user_dto_input.map_object(data)
        user_dto_input.id = id
        UserService.update_user(user_dto_input, current_user.id, data.get("current_password"))
        return AppResponse(message="Usuário atualizado com sucesso.")
    @staticmethod
    def delete_user(id:int):
        UserService.delete_user(id)
        return AppResponse(message="Usuário deletado com sucesso.")