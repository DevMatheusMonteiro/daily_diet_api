from database import db
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.Datetime, nullable=False)
    isOnDiet = db.Column(db.Boolean, nullable=False)