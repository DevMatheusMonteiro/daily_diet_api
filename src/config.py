from sqlalchemy.engine import URL
import os
class Config:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "instance", "database.db")
    SECRET_KEY = "default"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    