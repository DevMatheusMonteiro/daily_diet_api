from repositories.meal_repository import MealRepository, Meal
from models.user import User
from utils.app_error import AppError
class MealService:
    @staticmethod
    def create_meal(data:dict):
        name = data.get()
        description = db.Column(db.String(255), nullable=False)
        datetime = db.Column(db.Datetime, nullable=False)
        isOnDiet = db.Column(db.Boolean, nullable=False)
        user_id = data.get("user_id")
        if not name or not datetime or not isOnDiet or not user_id:
            raise AppError("Campos inválidos.")
        user = User.query.get(user_id)
        if not user:
            raise AppError("Usuário não encontrado.", 404)
            