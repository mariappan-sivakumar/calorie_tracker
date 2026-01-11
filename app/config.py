import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

USDA_API_KEY = os.getenv("USDA_API_KEY")
USDA_BASE_URL = "https://api.nal.usda.gov/fdc/v1"

DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
