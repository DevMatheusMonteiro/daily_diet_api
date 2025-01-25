from database import db
from datetime import datetime
from sqlalchemy.sql import func
class Meal(db.Model):
    __tablename__ = "Meals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    meal_datetime = db.Column(
            db.DateTime(timezone=True), # Habilita suporte ao timezone
            nullable=False,
            server_default=func.now() # Garante que o valor no banco seja UTC
        )
    isOnDiet = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", back_populates='meal')
    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description, "meal_datetime": self.meal_datetime, "isOnDiet": self.isOnDiet, "user_id": self.user_id}