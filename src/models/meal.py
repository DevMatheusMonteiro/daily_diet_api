from database import db
class Meal(db.Model):
    __tablename__ = "Meals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    datetime = db.Column(db.DateTime, nullable=False)
    isOnDiet = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", back_populates='meal')