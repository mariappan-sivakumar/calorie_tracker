from app.logger_config import setup_logging
setup_logging()  # MUST run BEFORE importing services


from fastapi import FastAPI
from app.api import food, history

app = FastAPI(title="AI Calorie Tracker")

app.include_router(food.router, prefix="/api/food")
app.include_router(history.router, prefix="/api/history")

# main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
