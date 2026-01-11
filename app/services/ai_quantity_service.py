from fastapi import UploadFile

from app.ai.gemini_quantity import convert_to_grams
from app.ai.gemini_vision import detect_food_from_image
from app.services.nutrition_service import get_nutrition_data
from sqlalchemy.orm import Session


def process_food_input(user_input: str, db: Session):
    ai_result = convert_to_grams(user_input)

    if "error" in ai_result:
        return ai_result

    if ai_result["confidence"] < 0.6:
        return {"error": "Low confidence in quantity conversion"}

    grams = ai_result["quantity_grams"]
    food_name = ai_result["food_name"]

    nutrients = get_nutrition_data(food_name, grams, db)
    return {
        "input": user_input,
        "confidence": ai_result["confidence"],
        **nutrients
    }


async def food_from_image(
        image: UploadFile,
        quantity: str,
        db: Session
):
    image_bytes = await image.read()

    # 1️⃣ Detect food name
    food_result = detect_food_from_image(image_bytes)

    if food_result["confidence"] < 0.6:
        return {"error": "Low confidence food detection"}

    food_name = food_result["food_name"]

    # 2️⃣ Convert quantity → grams
    quantity_result = convert_to_grams(quantity)

    if "error" in quantity_result:
        return quantity_result

    grams = quantity_result["quantity_grams"]

    # 3️⃣ USDA nutrition + scaling
    nutrition = get_nutrition_data(food_name, grams, db)

    return {
        "input": quantity,
        "quantity_grams": grams,
        "food_name_confidence": food_result["confidence"],
        "quantity_confidence": quantity_result["confidence"],
        "nutrition": nutrition
    }
