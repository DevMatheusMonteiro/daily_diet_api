from services.meal_service import MealService
from dto.input.meal_dto_input import MealDTOInput
from dto.output.meal_dto_output import MealDTOOutput
from utils.app_response import AppResponse
from flask import request
from flask_login import current_user
class MealController:
    @staticmethod
    def create_meal():
        data = request.json
        meal_dto_input = MealDTOInput()
        meal_dto_input.map_object(data)
        meal_dto_input.user_id = current_user.id
        created_meal_id = MealService.create_meal(meal_dto_input)
        return AppResponse(message="Refeição adicionada com sucesso.", status_code=201, body={"meal_id": created_meal_id})
    @staticmethod
    def get_user_meal_by_id(meal_id:int):
        meal = MealService.get_user_meal_by_id(meal_id, current_user.id)
        meal_dto_output = MealDTOOutput()
        meal_dto_output.map_object(meal.to_dict())
        return AppResponse(body={"meal": meal_dto_output.model_dump()})
    @staticmethod
    def search_user_meals():
        data = request.args
        search = data.get("search")
        meals = MealService.search_user_meals(current_user.id, search)
        meal_dto_output = MealDTOOutput()
        return AppResponse(body={"meals": [meal_dto_output.map_object(meal.to_dict()).model_dump() for meal in meals]})
    @staticmethod
    def update_meal(meal_id:int):
        data = request.json
        meal_dto_input = MealDTOInput()
        meal_dto_input.map_object(data)
        meal_dto_input.id = meal_id
        meal_dto_input.user_id = current_user.id
        MealService.update_meal(meal_dto_input)
        return AppResponse(message="Refeição atualizada com sucesso.")
    @staticmethod
    def delete_meal(meal_id:int):
        MealService.delete_meal(meal_id, current_user.id)
        return AppResponse(message="Refeição deletada com sucesso.")