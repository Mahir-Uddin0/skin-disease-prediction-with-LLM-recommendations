import json
from app.services.inference_service import predict_disease
from app.services.llm_service import generate_recommendation


def analyze_skin(image_bytes: bytes):
    disease, confidence = predict_disease(image_bytes)

    llm_raw = generate_recommendation(disease, confidence)

    try:
        llm_data = json.loads(llm_raw)
    except:
        # fallback if parsing fails
        llm_data = {
            "recommendations": llm_raw,
            "next_steps": "Consult a dermatologist.",
            "tips": "Keep skin clean and avoid irritation."
        }

    return {
        "disease": disease,
        "confidence": confidence,
        "recommendations": llm_data.get("recommendations", ""),
        "next_steps": llm_data.get("next_steps", ""),
        "tips": llm_data.get("tips", "")
    }