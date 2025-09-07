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






# 🌿 AgriVeinAI – Plant Leaf Disease Detection  

[![Live Demo](https://img.shields.io/badge/HuggingFace-Live%20Demo-yellow)](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  
[![GitHub](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/yourusername/AgriVeinAI)  

AgriVeinAI is a deep learning–powered application that helps identify **plant leaf diseases** with high accuracy.  
It uses the **PlantVillage dataset** and the **EfficientNetB0 model**, achieving **98% accuracy**.  

The app extracts **leaf vein patterns**, classifies the disease, estimates its **severity**, and provides **actionable solutions** for farmers and researchers.  

---

## 🚀 Features  

- ✅ Upload a plant leaf image for real-time disease detection  
- ✅ **Vein pattern extraction** for improved classification  
- ✅ Predicts across **38 disease classes** from PlantVillage dataset  
- ✅ Provides **severity analysis** of the infection  
- ✅ Suggests **practical remedies** and actionable solutions  
- ✅ User-friendly web interface deployed on Hugging Face Spaces  

---

## 📂 Project Structure  

AgriVeinAI/
│
├── app.py # Flask backend for handling routes and predictions
├── predict.py # Prediction pipeline and severity analysis
├── static/ # CSS, JS, and static assets
│ ├── style.css
│ └── images/
├── templates/ # HTML templates (Home, About, Contact, Predict)
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ └── predict.html
├── models/ # Trained EfficientNetB0 model (.h5 or .keras)
├── requirements.txt # Dependencies (Flask, TensorFlow, OpenCV, etc.)
└── README.md # Project Documentation

yaml
Copy code

---

## 📊 Dataset  

This project uses the **PlantVillage Dataset** (38 classes of plant leaf diseases).  
📥 Download here: [PlantVillage Dataset (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease)  

---

## 🧠 Model  

- Architecture: **EfficientNetB0**  
- Training Accuracy: **98%**  
- Dataset: **PlantVillage (38 classes)**  
- Improvements:  
  - Leaf vein extraction for better predictions  
  - Severity analysis integrated into pipeline  

---

## 🌐 Live Demo  

👉 [Click here to try AgriVeinAI on Hugging Face Spaces](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  

---

## 🛠️ Installation & Usage  

Clone the repository:  

```bash
git clone https://github.com/yourusername/AgriVeinAI.git
cd AgriVeinAI
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run locally:

bash
Copy code
python app.py
The app will run on: http://127.0.0.1:5000/

👩‍💻 Contributor
Gummala Likhitha – Hugging Face Profile

📸 Showcase
🌱 Upload Image → Vein Extraction → Disease Prediction → Severity → Solution


📌 Future Improvements
Add multilingual farmer support

Deploy on cloud servers for scalability

Mobile app integration

📜 License
This project is licensed under the MIT License – feel free to use and modify.
