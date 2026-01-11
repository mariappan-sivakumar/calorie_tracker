from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.db.session import get_db
from app.models.food_log import FoodLog
from app.schemas.food import FoodHistoryResponse

router = APIRouter(tags=["History"])


@router.get("/", response_model=List[FoodHistoryResponse])
def get_food_history(
        db: Session = Depends(get_db),
        limit: int = Query(20, ge=1, le=100),
        food_date: Optional[date] = Query(None)
):
    """
    Fetch food intake history.

    - Default: latest 20 records
    - Optional filter by date (YYYY-MM-DD)
    """

    query = db.query(FoodLog)

    if food_date:
        query = query.filter(FoodLog.created_at.cast(date) == food_date)

    history = (
        query
        .order_by(FoodLog.created_at.desc())
        .limit(limit)
        .all()
    )

    return history
