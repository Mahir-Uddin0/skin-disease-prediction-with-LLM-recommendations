from app.services.llm_service import generate_recommendation, parse_llm_output

def analyze_skin(image_bytes: bytes):
    disease, confidence = predict_disease(image_bytes)

    llm_raw = generate_recommendation(disease, confidence)
    llm_data = parse_llm_output(llm_raw)

    return {
        "disease": disease,
        "confidence": confidence,
        **llm_data
    }