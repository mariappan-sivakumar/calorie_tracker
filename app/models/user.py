from sqlalchemy import Column, Integer, String
from app.db.base import Base
from dataclasses import dataclass


@dataclass
class User(Base):
    __tablename__ = "users"
    __table_args__ = ({"schema": "calorie_tracker"},)

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
