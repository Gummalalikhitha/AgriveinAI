# 🌿 AgriVeinAI – Plant Leaf Disease Detection 

AgriVeinAI is an AI-powered web application designed to detect plant leaf diseases from images, analyze their severity, and provide actionable solutions for farmers and agricultural researchers. By leveraging deep learning and leaf vein extraction techniques, the project enhances disease classification accuracy and supports sustainable agriculture.

[![Live Demo](https://img.shields.io/badge/HuggingFace-Live%20Demo-yellow)](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  
[![GitHub](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/gummalalikhitha/AgriVeinAI)  

## 📖 Project Overview 

AgriVeinAI is a deep learning–powered application that helps identify **plant leaf diseases** with high accuracy.  
It uses the **PlantVillage dataset** and the **EfficientNetB0 model**, achieving **98% accuracy**.  

The app extracts **leaf vein patterns**, classifies the disease, estimates its **severity**, and provides **actionable solutions** for farmers and researchers.  

---

## 🚀 Features   

- 🌱 **Leaf Disease Detection**: Upload a plant leaf image and get instant prediction of the disease.  
- 🔍 **Vein Pattern Extraction**: Uses vein analysis to enhance disease classification.  
- 📊 **Severity Analysis**: Estimates how severe the infection is.  
- 💡 **Actionable Solutions**: Provides practical remedies and best practices for farmers.  
- 🖼 **Supports 38 Classes**: Covers a wide range of plant species and disease categories.  
- 🌐 **Deployed on Hugging Face Spaces** for free access worldwide.  

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
---

🧑‍💻 Tech Stack
---

**Backend:** Flask (Python)

**Frontend:** HTML, CSS, JavaScript

**Model:** EfficientNetB0 (Keras / TensorFlow)

**Dataset:** PlantVillage (public dataset for plant disease detection)

**Deployment:** Hugging Face Spaces

## 📊 Dataset
--- 

This project uses the **PlantVillage Dataset** (38 classes of plant leaf diseases).  
📥 Download here: [PlantVillage Dataset (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease)  


## 🧠 Model  
---
- Architecture: **EfficientNetB0**  
- Training Accuracy: **98%**  
- Dataset: **PlantVillage (38 classes)**  
- Improvements:  
  - Leaf vein extraction for better predictions  
  - Severity analysis integrated into pipeline  

---

## 🌐 Live Demo  
---
👉 [Click here to try AgriVeinAI on Hugging Face Spaces](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  

---

## 🛠️ Installation & Usage  
---
Clone the repository:  
---
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
---
Gummala Likhitha – Hugging Face Profile

📸 Showcase
🌱 Upload Image → Vein Extraction → Disease Prediction → Severity → Solution


📌 Future Improvements
---
Add multilingual farmer support

Deploy on cloud servers for scalability

Mobile app integration

📜 License
This project is licensed under the MIT License – feel free to use and modify.
