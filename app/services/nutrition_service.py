import requests
from app.config import USDA_API_KEY, USDA_BASE_URL
import logging
from sqlalchemy.orm import Session

from app.db.repositories.food_log_repo import create_food_log

# IMPORTANT: attach handlers to the logger manually
logger = logging.getLogger(__name__)
# if not logger.hasHandlers():
#     # Attach handler in case it was imported before setup
#     import sys
#     handler = logging.StreamHandler(sys.stdout)
#     formatter = logging.Formatter(
#         "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
#     )
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)
#     logger.setLevel(logging.INFO)


def search_food(food_name: str):
    url = f"{USDA_BASE_URL}/foods/search?api_key={USDA_API_KEY}"

    payload = {
        "query": food_name,
        "pageSize": 1
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if "foods" not in data or len(data["foods"]) == 0:
        return None

    return data["foods"][0]["fdcId"]


def get_food_details(fdc_id: int):
    url = f"{USDA_BASE_URL}/food/{fdc_id}?api_key={USDA_API_KEY}"
    response = requests.get(url)
    return response.json()


def parse_nutrients(food_data):
    nutrients = food_data.get("foodNutrients", [])

    result = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "micronutrients": {}
    }

    for n in nutrients:
        nutrient_id = n["nutrient"]["id"]
        value = n.get("amount", 0)

        if nutrient_id == 1008:
            result["calories"] = value
        elif nutrient_id == 1003:
            result["protein"] = value
        elif nutrient_id == 1005:
            result["carbs"] = value
        elif nutrient_id == 1004:
            result["fat"] = value
        else:
            name = n["nutrient"]["name"]
            result["micronutrients"][name] = value

    return result


def get_nutrition_data(food_name: str, quantity: int, db: Session):
    fdc_id = search_food(food_name)
    if not fdc_id:
        logger.error("Food not found: %s", food_name)
        return {"error": "Food not found"}

    food_data = get_food_details(fdc_id)

    logger.info("USDA raw response: %s", food_data)

    nutrients = parse_nutrients(food_data)
    scaled = scale_nutrients(nutrients, quantity)

    # 🔹 Store in DB
    food_log = create_food_log(
        db=db,
        food_name=food_name,
        quantity=f"{quantity}g",
        calories=scaled["calories"],
        protein=scaled["protein"],
        carbs=scaled["carbs"],
        fat=scaled["fat"],
        micronutrients=scaled["micronutrients"]
    )

    return {
        "id": food_log.id,
        "food": food_name,
        "quantity_grams": quantity,
        "nutrients": scaled
    }


def scale_nutrients(nutrients: dict, quantity_grams: int) -> dict:
    factor = quantity_grams / 100.0

    scaled = {
        "calories": round(nutrients["calories"] * factor, 2),
        "protein": round(nutrients["protein"] * factor, 2),
        "carbs": round(nutrients["carbs"] * factor, 2),
        "fat": round(nutrients["fat"] * factor, 2),
        "micronutrients": {}
    }

    for name, value in nutrients["micronutrients"].items():
        scaled["micronutrients"][name] = round(value * factor, 2)

    return scaled
