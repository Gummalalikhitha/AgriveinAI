import cv2
import numpy as np
import os
import pickle
from sklearn.decomposition import IncrementalPCA

# Function to extract vein features
def extract_vein_features(image_path, size=(128, 128)):
    img = cv2.imread(image_path)
    if img is None:
        return None, None  # skip broken files
    
    # Resize for faster processing
    img = cv2.resize(img, size)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold for veins
    veins = cv2.adaptiveThreshold(blur, 255,
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV, 11, 2)

    # Flatten vein pattern for ML
    features = veins.flatten()

    return features, veins


def preprocess_dataset(dataset_dir, output_file="features.pkl", img_limit=None):
    X, y = [], []
    label_map = {}

    print("🔄 Starting preprocessing...")

    for idx, class_name in enumerate(os.listdir(dataset_dir)):
        class_path = os.path.join(dataset_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        label_map[idx] = class_name
        images = os.listdir(class_path)

        if img_limit:  # debug mode: use only N images per class
            images = images[:img_limit]

        for i, img_name in enumerate(images):
            img_path = os.path.join(class_path, img_name)
            features, _ = extract_vein_features(img_path)

            if features is None:
                continue  # skip bad image

            X.append(features)
            y.append(idx)

            if i % 100 == 0:
                print(f"[{class_name}] Processed {i}/{len(images)} images...")

    X = np.array(X)
    y = np.array(y)

    print(f"✅ Extracted features from {len(X)} images.")

    # Reduce dimensionality (faster for large datasets)
    print("🔄 Running Incremental PCA...")
    ipca = IncrementalPCA(n_components=100, batch_size=200)
    X_reduced = ipca.fit_transform(X)

    with open(output_file, "wb") as f:
        pickle.dump((X_reduced, y, label_map, ipca), f)

    print(f"✅ Features saved to {output_file}")


if __name__ == "__main__":
    # change img_limit to e.g. 200 for quick testing
    preprocess_dataset("plantvillage_split/train", img_limit=None)
