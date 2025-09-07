# 🌿 AgriVeinAI – Plant Leaf Disease Detection  

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green?logo=flask)](https://flask.palletsprojects.com/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)](https://www.tensorflow.org/)  
[![HuggingFace](https://img.shields.io/badge/Deployed-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  

🚀 **Live Demo**: [AgriVeinAI on Hugging Face Spaces](https://huggingface.co/spaces/gummalalikhitha/AgriVeinAI)  
📂 **GitHub Repo**: [AgriVeinAI](https://github.com/gummalalikhitha/AgriVeinAI)  

---

## 📖 Overview  

**AgriVeinAI** is an **AI-powered deep learning application** for detecting **plant leaf diseases** with high accuracy.  
It uses **leaf vein extraction** to improve predictions, classifies diseases, estimates severity, and provides **actionable solutions** for farmers.  

- ✅ **Dataset:** [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)  
- ✅ **Model:** EfficientNetB0 (98% accuracy)  
- ✅ **Deployed on:** Hugging Face Spaces  

---

## ✨ Features  

| Feature | Description |
|---------|-------------|
| 🌱 **Disease Detection** | Upload a leaf image → Predict disease instantly |
| 🔍 **Vein Extraction** | Uses vein pattern analysis for robust classification |
| 📊 **Severity Analysis** | Estimates how severe the infection is |
| 💡 **Solutions** | Provides remedies and preventive practices |
| 🖼 **Supports 38 Classes** | Covers multiple crops & diseases |
| 🌐 **Deployed App** | Accessible to anyone, anywhere |

---

## 🧠 Model  

- **Architecture:** EfficientNetB0 (Transfer Learning)  
- **Accuracy:** 98% on test set  
- **Training Dataset:** PlantVillage (38 disease classes, 54,000+ images)  
- **Enhancements:**  
  - ✅ Leaf vein pattern analysis  
  - ✅ Severity classification  
  - ✅ Optimized preprocessing pipeline  

---

## 📊 Dataset  

📥 Download dataset here: [PlantVillage (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease)  

| Dataset Details | Value |
|-----------------|-------|
| Classes | 38 |
| Images | ~54,000 |
| Type | RGB leaf images |
| Labels | Healthy / Diseased (multiple crops) |

---

## 📂 Project Structure  

```bash
AgriVeinAI/
│
├── app.py             # Flask backend server
├── predict.py         # Core prediction logic
├── model/             # Trained EfficientNetB0 model
├── templates/         # HTML pages (Home, About, Contact, Predict)
├── static/            # CSS, JS, images
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
⚙️ Installation & Usage
Clone the repository and run locally:

bash
Copy code
# Clone repo
git clone https://github.com/gummalalikhitha/AgriVeinAI.git
cd AgriVeinAI

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
Open 👉 http://127.0.0.1:5000/ in your browser.

🌐 Live Demo
👉 Try AgriVeinAI on Hugging Face Spaces

📸 Workflow Showcase
🌱 Upload Image

🔍 Vein Extraction

🧠 Disease Prediction

📊 Severity Estimation

💡 Solution Recommendation

👩‍💻 Contributor
Gummala Likhitha

GitHub

Hugging Face Profile

🚀 Future Improvements
📱 Mobile app integration

🌍 Multilingual farmer support

☁️ Cloud-based scalable deployment

🤖 IoT integration for real-time field monitoring

📜 License
This project is licensed under the MIT License – free to use and modify.

⭐ If you found this project helpful, don’t forget to star the repo! 🌟
