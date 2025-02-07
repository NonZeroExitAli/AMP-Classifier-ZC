async function predict() {
    let sequence = document.getElementById("sequence").value;
    if (sequence.length < 10 || sequence.length > 100) {
        alert("Sequence length must be between 10 and 100.");
        return;
    }

    let start = performance.now();
    let response = await fetch("https://your-backend-url.onrender.com/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sequence })
    });

    let data = await response.json();
    let end = performance.now();

    document.getElementById("result").innerText = `Prediction: ${data.prediction}`;
    document.getElementById("time").innerText = `Processing Time: ${(end - start).toFixed(2)} ms`;
}
