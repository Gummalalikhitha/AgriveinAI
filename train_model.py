# train_supervised.py
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB0
import math

# -------------------
# Config
# -------------------
DATA_DIR = "plantvillage_split"   # contains train/, val/, test/
BATCH_SIZE = 32
IMG_SIZE = 224                    # change to 260/300 if you have VRAM
EPOCHS = 10
MODEL_OUT = "models/effnetb0_vein_color.h5"
NUM_WORKERS = 4
PATIENCE = 5

# -------------------
# Datasets (tf.data)
# -------------------
AUTOTUNE = tf.data.AUTOTUNE

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    os.path.join(DATA_DIR, "train"),
    label_mode="categorical",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=True,
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    os.path.join(DATA_DIR, "val"),
    label_mode="categorical",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=False,
)

class_names = train_ds.class_names
num_classes = len(class_names)
print("classes:", num_classes, class_names)

# Prefetch
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# -------------------
# Advanced Augmentation (in-tf)
# -------------------
data_augmentation = keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.15),
    layers.RandomZoom(0.15),
    layers.RandomTranslation(0.08, 0.08),
    layers.RandomContrast(0.15),
], name="augment")

# If you want Albumentations offline augmentation pipeline, you can use image preprocessing step that saves to disk,
# but the above TF pipeline is fast and GPU-friendly.

# -------------------
# Build model (transfer learning)
# -------------------
def build_model(img_size=IMG_SIZE, num_classes=num_classes):
    inputs = keras.Input(shape=(img_size, img_size, 3))
    x = data_augmentation(inputs)
    # Optionally: add custom preprocessing (clahe, or merge vein map) BEFORE feeding here by creating preprocessed PNGs.
    # Use EfficientNet preprocessing:
    x = tf.keras.applications.efficientnet.preprocess_input(x)
    base = EfficientNetB0(include_top=False, input_tensor=x, weights="imagenet")
    base.trainable = False   # warmup training

    x = layers.GlobalAveragePooling2D()(base.output)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)
    model = keras.Model(inputs, outputs)
    return model, base

model, base = build_model()

# compile (warmup)
optimizer = tf.keras.optimizers.Adam(learning_rate=3e-4)
model.compile(optimizer=optimizer,
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# -------------------
# Callbacks
# -------------------
os.makedirs("models", exist_ok=True)
checkpoint = keras.callbacks.ModelCheckpoint(
    MODEL_OUT, monitor="val_accuracy", save_best_only=True, verbose=1
)
early = keras.callbacks.EarlyStopping(monitor="val_accuracy", patience=PATIENCE, restore_best_weights=True)
reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=3, verbose=1)

# -------------------
# Class weights (optional - handle imbalance)
# -------------------
# compute class weights
import numpy as np
from collections import Counter
labels = []
for batch_images, batch_labels in train_ds.unbatch().batch(1):
    labels.append(int(tf.argmax(batch_labels[0]).numpy()))
counts = Counter(labels)
total = sum(counts.values())
class_weights = {i: total/(len(counts)*counts[i]) for i in counts}
print("class_weights:", class_weights)

# -------------------
# Warmup training
# -------------------
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5,
    callbacks=[checkpoint, early, reduce_lr],
    class_weight=class_weights
)

# -------------------
# Fine-tune: unfreeze some layers
# -------------------
base.trainable = True
# Freeze first N layers (tune this)
fine_tune_at = int(len(base.layers) * 0.6)
for layer in base.layers[:fine_tune_at]:
    layer.trainable = False
for layer in base.layers[fine_tune_at:]:
    layer.trainable = True

# lower LR for fine-tune
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# continue training
history_ft = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS,
    callbacks=[checkpoint, early, reduce_lr],
    class_weight=class_weights
)

# Save final model
model.save(MODEL_OUT)
print("Saved model to", MODEL_OUT)

# -------------------
# Evaluate on test set
# -------------------
test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    os.path.join(DATA_DIR, "test"),
    label_mode="categorical",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=False,
)
test_ds = test_ds.prefetch(AUTOTUNE)

loss, acc = model.evaluate(test_ds)
print(f"Test accuracy: {acc:.4f}")
