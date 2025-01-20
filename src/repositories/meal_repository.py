from models.meal import Meal, db
class MealRepository:
    @staticmethod
    def create_meal(meal: Meal):
        db.session.add(meal)
        db.session.commit()
        return meal
    @staticmethod
    def get_all_user_meals(user_id: int):
        return Meal.query.filter_by(user_id=user_id)
    @staticmethod
    def get_meal_by_id(meal_id:int):
        return Meal.query.get(meal_id)
    @staticmethod
    def update_meal(meal_id:int, data:dict):
        meal = Meal.query.get(meal_id)
        if not meal:
            return None
        for key, value in data.items():
            if hasattr(meal, key):
                setattr(meal,key,value)
        db.session.commit()
        return meal
    @staticmethod
    def delete_meal(meal_id:int):
        meal = Meal.query.get(meal_id)
        if not meal:
            return None
        db.session.delete(meal)
        db.session.commit()
        return meal