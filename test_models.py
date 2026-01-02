import tensorflow as tf
from ultralytics import YOLO

print("Loading vegetation model...")
veg_model = tf.keras.models.load_model("models/vegetation_saved_model")

print("Loading soil model...")
soil_model = YOLO("models/soil_best.pt")

print("✅ Both models loaded successfully")
