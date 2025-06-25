
---

# 🧠 MNIST Digit Classifier API

This is a simple Flask API for digit recognition using a pre-trained Keras model on the MNIST dataset. You can send an image of a digit (28x28 grayscale) and get back the predicted digit.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**Required Python packages (in `requirements.txt`):**

```
flask
tensorflow
pillow
numpy
```

---

## 🚀 Running the App

Make sure you're in the project folder (where `app.py` and `mnist_digit_model.keras` are located), then run:

```bash
python app.py
```

Flask will start a local development server at:

```
http://127.0.0.1:5000
```

---

## 📤 How to Use the API

Use `curl` or Postman to send a **POST** request with an image file.

### 🧪 Example Using curl:

```bash
curl -X POST -F "file=@digit.png" http://127.0.0.1:5000/predict
```

> Replace `digit.png` with the path to your 28x28 grayscale image of a digit (ideally white digit on black background).

### ✅ Expected Response

```json
{
  "digit": 7
}
```

---

## 🖼️ Image Format

* **Input:** PNG, JPG, or any format supported by Pillow
* **Color:** Grayscale (will be converted automatically)
* **Size:** 28x28 pixels (resized if needed)

> The image is inverted automatically (black background → white digit) to match MNIST style.

---

## 🧠 Model

* Pretrained Keras models: `mnist_digit_model.keras && mnist_digit_model.h5`
* Model expects flattened 28x28 input (shape: `(1, 784)`)

If you train a new model, make sure:

* Output layer uses `softmax`
* Input is flattened or reshaped to 784
* Model is saved using:

```python
model.save("mnist_digit_model.keras or mnist_digit_model.h5)
```

---

## 🔧 File Structure

```
mnist_test/
├── app.py
├── models/
|-----
├── requirements.txt
└── digit.png  # example image
```

---

## 📬 Notes

* The server runs in debug mode by default.
* This is for development/testing. For production, use a proper WSGI server (e.g., gunicorn) and add input validation/auth.

---
