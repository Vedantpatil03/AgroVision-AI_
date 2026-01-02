import numpy as np
import tensorflow as tf
from PIL import Image

def preprocess_image(image: Image.Image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image.astype("float32")

def vegetation_percentage(model, image: Image.Image):
    img = preprocess_image(image)

    # ✅ Use SavedModel serving signature
    infer = model.signatures["serving_default"]
    outputs = infer(tf.constant(img))

    # Get output tensor (first key)
    mask = list(outputs.values())[0].numpy()[0]

    binary_mask = (mask > 0.5).astype(np.uint8)

    vegetation = np.sum(binary_mask)
    total = binary_mask.size

    veg_pct = (vegetation / total) * 100
    non_veg_pct = 100 - veg_pct

    return round(veg_pct, 2), round(non_veg_pct, 2), binary_mask
