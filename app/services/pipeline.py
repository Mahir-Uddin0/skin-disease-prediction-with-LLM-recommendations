import json
import re
from app.services.inference_service import predict_disease
from app.services.llm_service import generate_recommendation


def extract_json(text: str):
    """
    Extract JSON block safely from LLM output
    """
    try:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass
    return None


def analyze_skin(image_bytes: bytes):
    disease, confidence = predict_disease(image_bytes)
    
    # return {
    #     "disease": disease,
    #     "confidence": confidence
    # }

    llm_raw = generate_recommendation(disease, confidence)

    llm_data = extract_json(llm_raw)

    if not llm_data:
        llm_data = {
            "recommendations": "Use gentle skincare and avoid irritants.",
            "next_steps": "Consult a dermatologist for proper evaluation.",
            "tips": "Keep skin moisturized and avoid scratching."
        }

    return {
        "disease": disease,
        "confidence": confidence,
        "recommendations": llm_data.get("recommendations", ""),
        "next_steps": llm_data.get("next_steps", ""),
        "tips": llm_data.get("tips", "")
    }