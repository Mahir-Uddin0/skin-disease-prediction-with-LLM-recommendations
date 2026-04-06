from PIL import Image
import io


def load_image(image_bytes: bytes):
    return Image.open(io.BytesIO(image_bytes))