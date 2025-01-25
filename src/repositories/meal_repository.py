from models.meal import Meal, db
from sqlalchemy import and_
class MealRepository:
    @staticmethod
    def create_meal(meal: Meal):
        db.session.add(meal)
        db.session.commit()
        return meal.id
    @staticmethod
    def get_user_meal_by_id(meal_id:int, user_id:int):
        return Meal.query.filter(
            and_(
                Meal.id == meal_id,
                Meal.user_id == user_id
            )
        ).first()
    @staticmethod
    def search_user_meals(user_id:int, search:str):
        search_pattern = f"%{search}%"
        return Meal.query.filter(
            and_(
                Meal.user_id == user_id,
                Meal.description.like(search_pattern)
            )
        ).all()
    @staticmethod
    def update_meal(meal: Meal):
        db.session.commit()
        return meal.id
    @staticmethod
    def delete_meal(meal: Meal):
        db.session.delete(meal)
        db.session.commit()
        return meal.id