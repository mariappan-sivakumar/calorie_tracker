import logging

from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.schemas.food import FoodTextRequest, AITextRequest
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services import ai_quantity_service
from app.services.nutrition_service import get_nutrition_data


router = APIRouter()


@router.post("/manual_input")
def analyze_food_text(data: FoodTextRequest, db: Session = Depends(get_db)):
    logging.info("enter into manual_input")
    nutrition = get_nutrition_data(
        data.food_name,
        data.quantity,
        db
    )

    return nutrition


@router.post("/ai_input")
def analyze_food_ai(data: AITextRequest, db: Session = Depends(get_db)):
    logging.info("enter into ai_input analyze_food_ai")
    nutrition = ai_quantity_service.process_food_input(data.prompt, db)

    return nutrition


@router.post("/from-image")
async def food_from_image(
        image: UploadFile = File(...),
        quantity: str = Form("1 serving"),
        db: Session = Depends(get_db)
):
    logging.info("enter into from-image food_from_image")
    nutrition = await ai_quantity_service.food_from_image(image, quantity, db)

    return nutrition
