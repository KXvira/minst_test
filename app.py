from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model("./model/mnist_digit_model.keras")

def prepare_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert("L")
    img = img.resize((28, 28))
    img_array = np.array(img)
    img_array = 255 - img_array
    img_array = img_array / 255.0
    img_array = img_array.reshape(1, 784)
    return img_array

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    image = prepare_image(file.read())
    prediction = model.predict(image)
    predicted_digit = int(np.argmax(prediction))
    return jsonify({"digit": predicted_digit})

if __name__ == "__main__":
    app.run(debug=True)
