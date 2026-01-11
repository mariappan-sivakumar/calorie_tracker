from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from datetime import datetime
from app.db.base import Base


class FoodLog(Base):
    __tablename__ = "food_logs"
    __table_args__ = ({"schema": "calorie_tracker"},)

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    food_name = Column(String)
    quantity = Column(String)

    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)

    micronutrients = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
