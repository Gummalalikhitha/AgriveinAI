# preprocess_plantvillage.py

import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#from keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm

# ----------------------------
# CONFIGURATIONS
# ----------------------------
DATASET_DIR = r"C:\AgriVeinAI\plantvillage_dataset\color"   # Path to PlantVillage dataset
IMG_SIZE = 224                 # Resize all images to 224x224
SAVE_X = "X.npy"               # File to save processed images
SAVE_Y = "y.npy"               # File to save labels

# ----------------------------
# STEP 1: LOAD DATASET
# ----------------------------
def load_dataset(dataset_dir, img_size):
    images = []
    labels = []
    
    print("Loading dataset...")
    for label in tqdm(os.listdir(dataset_dir)):  
        label_path = os.path.join(dataset_dir, label)
        if not os.path.isdir(label_path):
            continue

        for file in os.listdir(label_path):
            file_path = os.path.join(label_path, file)
            
            try:
                # Read image
                img = cv2.imread(file_path)
                if img is None:
                    continue

                # Resize
                img = cv2.resize(img, (img_size, img_size))

                # Convert to grayscale (optional: keep RGB if needed)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Normalize (0-1)
                gray = gray.astype("float32") / 255.0

                # Expand dims for grayscale (H, W, 1)
                gray = np.expand_dims(gray, axis=-1)

                images.append(gray)
                labels.append(label)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue

    return np.array(images), np.array(labels)

# ----------------------------
# STEP 2: DATA AUGMENTATION
# ----------------------------
def augment_data(X, y):
    print("Applying augmentation...")
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest"
    )
    
    augmented_images = []
    augmented_labels = []

    for i in tqdm(range(len(X))):
        img = np.expand_dims(X[i], 0)  # Add batch dim
        it = datagen.flow(img, batch_size=1)
        
        for _ in range(2):  # Generate 2 augmented images per original
            # batch = it.next()
            batch = next(it)
            augmented_images.append(batch[0])
            augmented_labels.append(y[i])
    
    return np.array(augmented_images), np.array(augmented_labels)

# ----------------------------
# MAIN PIPELINE
# ----------------------------
if __name__ == "__main__":
    # Step 1: Load dataset
    X, y = load_dataset(DATASET_DIR, IMG_SIZE)
    print("Original dataset shape:", X.shape, y.shape)

    # Step 2: Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Step 3: Augment dataset
    X_aug, y_aug = augment_data(X, y_encoded)

    # Step 4: Combine original + augmented
    X_final = np.concatenate([X, X_aug], axis=0)
    y_final = np.concatenate([y_encoded, y_aug], axis=0)

    print("Final dataset shape:", X_final.shape, y_final.shape)

    # # Step 5: Save preprocessed dataset
    # np.save(SAVE_X, X_final)
    # np.save(SAVE_Y, y_final)
    # print(f"Saved preprocessed data -> {SAVE_X}, {SAVE_Y}")
    # Instead of augment_data() and concatenating, just save original dataset
    np.save(SAVE_X, X)
    np.save(SAVE_Y, y_encoded)
    print("Saved original dataset only -> X.npy, y.npy")
