from models.user import User, db
from sqlalchemy import and_, or_
class UserRepository:
    @staticmethod
    def create_user(user:User):
        db.session.add(user)
        db.session.commit()
        return user.id
    @staticmethod
    def get_user_by_id(user_id:int):
        return User.query.get(user_id)
    @staticmethod
    def get_user_by_email(email:str):
        return User.query.filter_by(email=email).first()
    @staticmethod
    def get_user_by_username(username:str):
        return User.query.filter_by(username=username).first()
    @staticmethod
    def search_users(search):
        search_pattern = f"%{search}%"
        return User.query.filter(
            or_(
                User.email.like(search_pattern), 
                User.username.like(search_pattern)
            )
        ).all()
    @staticmethod
    def update_user(user:User):
        db.session.commit()
        return user.id
    @staticmethod
    def delete_user(user: User):
        db.session.delete(user)
        db.session.commit()
        return user.id