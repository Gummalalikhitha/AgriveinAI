import os
import cv2
import base64
from flask import Flask, render_template, request
from predict import predict_disease

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Convert image to base64 for HTML
def to_base64(img):
    if img is None:
        return None
    _, buffer = cv2.imencode(".png", img)
    return base64.b64encode(buffer).decode("utf-8")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "No file uploaded", 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Run prediction
        prediction, confidence, severity, veins,info = predict_disease(filepath)

        # Convert vein image to base64
        veins_b64 = to_base64(veins)

        return render_template(
            "result.html",
            prediction=prediction,
            confidence=round(confidence, 2),
            severity=severity,
            info=info,
            image_path=filepath,
            vein_img=veins_b64
        )

    return render_template("predict.html")

@app.route("/result")
def result():
    return render_template("result.html")
if __name__ == "__main__":
    app.run(debug=False)
