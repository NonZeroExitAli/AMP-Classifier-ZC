from flask import Flask, request, jsonify
import joblib
import time

app = Flask(__name__)

# 🔹 Load the trained model
model = joblib.load("model.joblib")  # Ensure this file is in the correct directory

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get("sequence", "")

    # 🔸 Validate input
    if not sequence or len(sequence) < 10 or len(sequence) > 100:
        return jsonify({"error": "Sequence length must be between 10 and 100."}), 400

    # 🔹 Measure processing time
    start_time = time.time()

    # 🔹 Predict using the loaded model
    prediction = model.predict([sequence])[0]  # Assuming the model accepts a list
    confidence = 85.5  # If your model provides confidence, replace this

    processing_time = round((time.time() - start_time) * 1000, 2)  # In milliseconds

    return jsonify({
        "prediction": "AMP" if prediction == 1 else "non-AMP",
        "confidence": confidence,
        "processing_time": processing_time
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
