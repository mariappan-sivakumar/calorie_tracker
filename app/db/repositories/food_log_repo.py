from sqlalchemy.orm import Session
from app.models.food_log import FoodLog


def create_food_log(
        db: Session,
        *,
        food_name: str,
        quantity: str,
        calories: float,
        protein: float,
        carbs: float,
        fat: float,
        micronutrients: dict
) -> FoodLog:
    food_log = FoodLog(
        food_name=food_name,
        quantity=quantity,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fat=fat,
        micronutrients=micronutrients
    )

    db.add(food_log)
    db.commit()
    db.refresh(food_log)

    return food_log
