from app.services.inference_service import predict_disease


def analyze_skin(image_bytes: bytes):
    disease, confidence = predict_disease(image_bytes)

    return {
        "disease": disease,
        "confidence": confidence
    }