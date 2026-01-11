from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any


class FoodTextRequest(BaseModel):
    food_name: str
    quantity: int


class FoodHistoryResponse(BaseModel):
    id: int
    food_name: str
    quantity: str
    calories: float
    protein: float
    carbs: float
    fat: float
    micronutrients: Dict[str, Any]
    created_at: datetime

    class Config:
        from_attributes = True


class AITextRequest(BaseModel):
    prompt: str
