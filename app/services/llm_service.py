from google import genai
from app.core.config import GEMINI_API_KEY

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_recommendation(disease: str, confidence: float):
    """
    Generate structured medical advice using Gemini (new SDK).
    """

    prompt = f"""
You are a medical assistant AI.

A skin disease classification model predicted:
- Disease: {disease}
- Confidence: {confidence:.2f}

Provide the response STRICTLY in JSON format:
{{
  "recommendations": "...",
  "next_steps": "...",
  "tips": "..."
}}

Guidelines:
- Keep explanations simple
- Do NOT provide definitive diagnosis
- Include suggestion to consult a doctor
- Keep each field concise (2–3 sentences)
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text