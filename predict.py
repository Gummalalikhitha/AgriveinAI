import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from severity import estimate_severity
from disease_info import disease_solutions
# -------------------
# Config
# -------------------
IMG_SIZE = 224
MODEL_PATH = "models/effnetb0_vein_color.h5"
DATA_DIR = "plantvillage_split/train"  # for class names

# -------------------
# Load model & classes
# -------------------
print("Loading model...")
model = keras.models.load_model(MODEL_PATH)

class_names = sorted(os.listdir(DATA_DIR))
print(f"Loaded {len(class_names)} classes.")

# -------------------
# Helper: Extract vein pattern
# -------------------
def extract_vein_pattern(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Adaptive thresholding to highlight veins
    veins = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    return veins

# -------------------
# Main Prediction Function
# -------------------
def predict_disease(image_path):
    # Preprocess for model
    img = keras.utils.load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
    x = keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.efficientnet.preprocess_input(x)

    # Predict
    preds = model.predict(x)
    cls = class_names[np.argmax(preds)]
    confidence = float(np.max(preds) * 100)

    # Severity
    severity = estimate_severity(image_path)

    # Vein pattern
    veins = extract_vein_pattern(image_path)
    # after inference
    info = disease_solutions.get(cls, {
    "description": "Information not available.",
    "solution": "No recommendation available."
    })

    return cls, confidence, severity, veins, info
