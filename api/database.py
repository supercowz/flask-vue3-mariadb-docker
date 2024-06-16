from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, Text, LargeBinary as Binary

db = SQLAlchemy()

class UserModel(db.Model):
  __tablename__ = "users"
  id = db.Column(Integer, primary_key=True)
  # email = db.Column(String(255), unique=True, nullable=False)
  username = db.Column(String(255), unique=True, nullable=False)
  password = db.Column(Binary(100), nullable=False)
  created_at = db.Column(DateTime, nullable=False)