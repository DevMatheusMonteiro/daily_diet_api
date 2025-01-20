from database import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    meal = db.relationship("Meal", uselist=False, back_populates="user", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {"id": self.id, "email": self.email, "username": self.username, "password": self.password}