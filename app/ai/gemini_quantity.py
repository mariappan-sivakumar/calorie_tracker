import json
import google.genai as genai
from app.config import GEMINI_API_KEY
from app.ai.prompts import FOOD_QUANTITY_SYSTEM_PROMPT
import re
import json

client = genai.Client(api_key=GEMINI_API_KEY)


def convert_to_grams(user_input: str) -> dict:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",

        contents=[
            {
                "role": "user",
                "parts": [{
                    "text": f"""
Convert the following food quantity into grams.

Food description:
"{user_input}"

Return only JSON using the specified output format.
"""
                }]
            }
        ],
        config={
            "system_instruction": FOOD_QUANTITY_SYSTEM_PROMPT,
            "temperature": 0.1,
            "max_output_tokens": 256
        }
    )

    raw_text = response.candidates[0].content.parts[0].text

    try:
        return extract_json(raw_text)
    except Exception:
        return {
            "error": "Invalid AI response",
            "raw": raw_text
        }


def extract_json(text: str) -> dict:
    # Remove markdown code fences
    cleaned = re.sub(r"```(?:json)?", "", text)
    cleaned = cleaned.replace("```", "").strip()
    return json.loads(cleaned)
