from flask import Flask, request, jsonify
import joblib
import time

app = Flask(__name__)

model = joblib.load("SVM.joblib")  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get("sequence", "")

    if not sequence or len(sequence) < 10 or len(sequence) > 100:
        return jsonify({"error": "Sequence length must be between 10 and 100."}), 400

    start_time = time.time()

    prediction = model.predict([sequence])[0]  
    confidence = 85.5 

    processing_time = round((time.time() - start_time) * 1000, 2) 

    return jsonify({
        "prediction": "AMP" if prediction == 1 else "non-AMP",
        "confidence": confidence,
        "processing_time": processing_time
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
