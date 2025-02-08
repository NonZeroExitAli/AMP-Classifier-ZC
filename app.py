from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get("sequence", "")

    if not sequence or len(sequence) < 10 or len(sequence) > 100:
        return jsonify({"error": "Sequence length must be between 10 and 100."}), 400

    # Dummy model logic (Replace with your actual ML model)
    prediction = "AMP" if "A" in sequence else "non-AMP"
    confidence = 85.5  # Replace with actual confidence score

    return jsonify({"prediction": prediction, "confidence": confidence})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
