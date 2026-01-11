import json
import google.genai as genai
from app.config import GEMINI_API_KEY
from app.ai.prompts import FOOD_IMAGE_SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)


def detect_food_from_image(image_bytes: bytes) -> dict:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=[
            {
                "role": "user",
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_bytes
                        }
                    },
                    {
                        "text": "Identify the food in this image."
                    }
                ]
            }
        ],
        config={
            "system_instruction": FOOD_IMAGE_SYSTEM_PROMPT,
            "temperature": 0.2,
            "max_output_tokens": 128
        }
    )

    raw = response.candidates[0].content.parts[0].text
    raw = raw.replace("```json", "").replace("```", "").strip()

    return json.loads(raw)
