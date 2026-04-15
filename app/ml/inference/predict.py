import torch
from PIL import Image
import io

from app.ml.models.model_loader import model, device
from app.ml.preprocessing.transform import transform
from app.utils.constants import CLASS_NAMES


def predict_image(image_bytes: bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.nn.functional.softmax(outputs, dim=1)

        confidence, pred_class = torch.max(probs, dim=1)

    disease = CLASS_NAMES[(pred_class).item()]
    confidence = confidence.item()

    return disease, confidence