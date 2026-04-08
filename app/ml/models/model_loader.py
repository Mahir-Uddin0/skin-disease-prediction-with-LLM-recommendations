import torch
import timm

MODEL_PATH = "models/skin_model.pth"

# Update this to your number of classes
NUM_CLASSES = 10  

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model():
    model = timm.create_model("deit3_base_patch16_224", pretrained=False, num_classes=NUM_CLASSES)

    checkpoint = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(checkpoint)

    model.to(device)
    model.eval()

    return model


# Load once (important!)
model = load_model()