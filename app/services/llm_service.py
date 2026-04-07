import json


def generate_recommendation(disease: str, confidence: float) -> dict:
    # This function would call the LLM (like OpenAI's GPT) to get recommendations based on the disease and confidence.
    # For demonstration, we'll return a mock response.
    return {
        "recommendation": f"Based on the diagnosis of {disease} with a confidence of {confidence:.2f}, it is recommended to consult a dermatologist for further evaluation and treatment options.",
        "precautions": "Avoid sun exposure, keep the affected area clean, and do not self-medicate."
    }
    

def parse_llm_output(text: str):
    try:
        return json.loads(text)
    except:
        return {
            "recommendations": "Unable to parse recommendations.",
            "next_steps": "Consult a medical professional.",
            "tips": "Keep skin clean and moisturized."
        }