🌿 AgriVeinAI
---
AgriVeinAI is an AI-powered web application designed to detect plant leaf diseases from images, analyze their severity, and provide actionable solutions for farmers and agricultural researchers. By leveraging deep learning and leaf vein extraction techniques, the project enhances disease classification accuracy and supports sustainable agriculture.

🚀 Live Demo
---
👉 Try AgriVeinAI on Hugging Face Spaces

📖 Project Overview
---
This project was built to address the real-world challenge of early plant disease detection. Using the PlantVillage dataset, I trained a deep learning model based on the EfficientNet-B0 architecture, achieving 98% accuracy in classifying 38 different plant disease classes.

The system extracts vein patterns from plant leaves before prediction, ensuring higher accuracy and robustness against noise in the input images. The web app allows users to upload a leaf image and instantly receive:

✅ Disease name

✅ Severity level (mild, moderate, severe)

✅ Actionable solutions to control the disease

✨ Features
---
38 Plant Disease Classes: Covers a wide range of crops and diseases from the PlantVillage dataset.

Leaf Vein Extraction: Enhances prediction reliability by focusing on biological vein structures.

High Accuracy (98%): Trained on EfficientNet-B0 deep learning model.

Severity Analysis: Provides an estimate of how infected the plant is.

Actionable Solutions: Practical remedies and eco-friendly farming practices.

User-Friendly Web App: Upload leaf image → Get prediction & solutions.

🛠️ Tech Stack
---
Frontend: HTML, CSS (Responsive pages for Home, About, Contact, Predict)

Backend: Flask (Python)

Deep Learning Model: EfficientNet-B0 (TensorFlow/Keras)

Dataset: PlantVillage Dataset

Deployment: Hugging Face Spaces (Gradio + Flask integration)

📂 Project Structure
---
AgriVeinAI/
│
├── app.py                 # Flask main app file
├── predict.py             # Prediction logic (load model, preprocess, predict, severity, solutions)
├── static/                # CSS, JS, and local images
├── templates/             # HTML templates (Home, About, Contact, Predict)
├── model/                 # Trained EfficientNet-B0 model (.h5 or .pkl)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

📊 Model Training
---
Dataset: PlantVillage (38 classes of healthy and diseased plant leaves)

Preprocessing: Image resizing, normalization, and augmentation.

Model: EfficientNet-B0

Accuracy: 98% on test dataset.

Extra Step: Leaf vein extraction for improved prediction quality.

📌 How It Works
---
User uploads a leaf image.

System extracts vein pattern from the leaf.

Preprocessed image is passed into the EfficientNet-B0 model.

Model predicts the disease class.

Severity is analyzed.

The app returns: disease name + severity + recommended solutions.

📬 Contact
---

👩‍💻 Created by Gummala Likhitha
📧 [Your Email Here]
🌐 [Your LinkedIn/GitHub Profile]

✨ If you like this project, don’t forget to ⭐ star the repo and try it on Hugging Face
!
