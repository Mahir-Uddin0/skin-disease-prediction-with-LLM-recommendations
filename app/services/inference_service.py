from app.ml.inference.predict import predict_image


def predict_disease(image_bytes: bytes):
    return predict_image(image_bytes)