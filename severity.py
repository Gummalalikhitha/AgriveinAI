# severity.py
import cv2
import numpy as np

def estimate_severity(image_path):
    """
    Estimate severity of disease as % of leaf area affected.
    Uses color thresholding (HSV) for brown/yellow regions.
    """
    img = cv2.imread(image_path)
    if img is None:
        return 0.0  # file not found

    # Resize for speed
    img = cv2.resize(img, (256, 256))

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold for diseased regions (brown/yellow)
    lower_disease = np.array([10, 40, 40])
    upper_disease = np.array([40, 255, 255])
    mask_disease = cv2.inRange(hsv, lower_disease, upper_disease)

    # Threshold for healthy (green) regions
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Count pixels
    diseased_area = np.sum(mask_disease > 0)
    healthy_area = np.sum(mask_green > 0)
    total_area = diseased_area + healthy_area

    if total_area == 0:
        return 0.0

    severity_percent = (diseased_area / total_area) * 100
    return round(severity_percent, 2)
