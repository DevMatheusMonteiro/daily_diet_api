from repositories.meal_repository import MealRepository, Meal
from dto.input.meal_dto_input import MealDTOInput
from utils.app_error import AppError
class MealService:
    @staticmethod
    def create_meal(meal_dto_input: MealDTOInput):
        name = meal_dto_input.name
        description = meal_dto_input.description
        meal_datetime = meal_dto_input.meal_datetime
        isOnDiet = meal_dto_input.isOnDiet
        user_id = meal_dto_input.user_id
        if not name or not isOnDiet:
            raise AppError("Campos inválidos.")
        new_meal = Meal(name=name, description=description, meal_datetime=meal_datetime, isOnDiet=isOnDiet, user_id=user_id)
        created_meal_id = MealRepository.create_meal(new_meal)
        return created_meal_id
    @staticmethod
    def get_user_meal_by_id(meal_id: int, current_user_id:int):
        meal = MealRepository.get_user_meal_by_id(meal_id, current_user_id)
        if not meal:
            raise AppError("Refeição não encontrada", 404)
        return meal
    @staticmethod
    def search_user_meals(current_user_id:int, search:str):
        meals = MealRepository.search_user_meals(current_user_id, search)
        if not meals:
            raise AppError("Nenhuma refeição encontrada.", 404)
        return meals
    @staticmethod
    def update_meal(meal_dto_input: MealDTOInput):
        meal = MealRepository.get_user_meal_by_id(meal_dto_input.id, meal_dto_input.user_id)
        if not meal:
            raise AppError("Refeição não encontrada.", 404)
        name = meal_dto_input.name
        description = meal_dto_input.description
        meal_datetime = meal_dto_input.meal_datetime
        isOnDiet = meal_dto_input.isOnDiet
        if (name and name.strip() == ""):
            raise AppError("Campos inválidos.")
        meal.name = name or meal.name
        meal.description = description or meal.description
        meal.meal_datetime = meal_datetime or meal.meal_datetime
        print(isOnDiet)
        meal.isOnDiet = isOnDiet if isOnDiet != None else meal.isOnDiet
        updated_meal_id = MealRepository.update_meal(meal)
        return updated_meal_id
    @staticmethod
    def delete_meal(meal_id, current_user_id):
        meal = MealRepository.get_user_meal_by_id(meal_id=meal_id, user_id=current_user_id)      
        if not meal:
            raise AppError("Refeição não encontrada.", 404)
        deleted_meal = MealRepository.delete_meal(meal)
        return deleted_meal

        
