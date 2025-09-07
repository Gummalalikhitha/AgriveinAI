import os
import shutil
import random

# Paths
dataset_dir = r"C:\Users\gumma\OneDrive\Desktop\AgriVeinAI\plantvillage_dataset\color"   # Your dataset folder
base_dir = "plantvillage_split"

# Train/Val/Test percentages
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Create folders
for split in ["train", "val", "test"]:
    split_dir = os.path.join(base_dir, split)
    os.makedirs(split_dir, exist_ok=True)

# Split each class folder
for class_name in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_name)
    if not os.path.isdir(class_path):
        continue
    
    images = os.listdir(class_path)
    random.shuffle(images)

    n_total = len(images)
    n_train = int(train_ratio * n_total)
    n_val = int(val_ratio * n_total)

    train_imgs = images[:n_train]
    val_imgs = images[n_train:n_train+n_val]
    test_imgs = images[n_train+n_val:]

    for split, img_list in zip(["train", "val", "test"], [train_imgs, val_imgs, test_imgs]):
        split_class_dir = os.path.join(base_dir, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        for img in img_list:
            src = os.path.join(class_path, img)
            dst = os.path.join(split_class_dir, img)
            shutil.copy(src, dst)

print("✅ Dataset successfully split into train/val/test")
