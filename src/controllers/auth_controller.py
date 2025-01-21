from flask import request
from services.auth_service import AuthService
from utils.app_response import AppResponse
class AuthController:
    @staticmethod
    def login():
        data = request.json
        AuthService.login(data)
        return AppResponse(message="Autenticação realizada com sucesso.")
    @staticmethod
    def logout():
        AuthService.logout()
        return AppResponse(message="Logout realizado com sucesso.")