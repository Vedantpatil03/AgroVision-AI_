from ultralytics import YOLO
import numpy as np
from PIL import Image

def load_soil_model():
    return YOLO("models/soil_best.pt")

def predict_soil(model, image: Image.Image):
    """
    Returns:
    annotated_image (RGB numpy array),
    soil_name (str),
    confidence (float),
    regions_detected (int),
    soil_coverage (float)
    """

    # 🔥 EXACT SAME inference style as Colab
    results = model(
        source=image,
        conf=0.10,
        iou=0.45,
        imgsz=640,
        device="cpu",
        verbose=False
    )[0]

    # No detection case
    if results.boxes is None or len(results.boxes) == 0:
        return None, "No soil detected", 0.0, 0, 0.0

    boxes = results.boxes
    classes = boxes.cls.cpu().numpy().astype(int)
    confidences = boxes.conf.cpu().numpy()

    # ✅ Dominant soil = highest confidence
    idx = np.argmax(confidences)
    dominant_class = classes[idx]
    dominant_conf = confidences[idx]

    # ✅ Coverage calculation
    h, w = results.orig_shape
    total_area = h * w
    detected_area = 0

    for box in boxes.xyxy:
        x1, y1, x2, y2 = box.cpu().numpy()
        detected_area += max(0, x2 - x1) * max(0, y2 - y1)

    coverage = (detected_area / total_area) * 100

    soil_name = results.names[dominant_class]

    # 🔥 Annotated image (same as Colab)
    annotated_img = results.plot()      # BGR
    annotated_img = annotated_img[..., ::-1]  # BGR → RGB

    return (
        annotated_img,
        soil_name,
        round(float(dominant_conf), 2),
        len(boxes),
        round(coverage, 2)
    )
