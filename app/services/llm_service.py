import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_recommendation(disease: str, confidence: float):
    """
    Generate structured medical advice using Gemini.
    """

    prompt = f"""
You are a medical assistant AI.

A skin disease classification model predicted:
- Disease: {disease}
- Confidence: {confidence:.2f}

Provide the response in JSON format with the following fields:
- recommendations
- next_steps
- tips

Guidelines:
- Keep explanations simple and safe
- Do NOT provide diagnosis claims
- Include a disclaimer to consult a doctor
- Keep each field concise (2–3 sentences max)
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text

