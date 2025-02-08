async function predict() {
    let sequence = document.getElementById("sequence").value.trim();
    let resultDiv = document.getElementById("result");
    let timeDiv = document.getElementById("time");

    if (sequence.length < 10 || sequence.length > 100) {
        alert("Sequence length must be between 10 and 100.");
        return;
    }

    // Show loading message
    resultDiv.innerText = "Processing...";
    timeDiv.innerText = "";

    let start = performance.now();

    try {
        let response = await fetch("https://amp-classifier-zc.fly.dev/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sequence })
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.statusText}`);
        }

        let data = await response.json();
        let end = performance.now();

        if (!data.prediction) {
            throw new Error("Invalid response from server");
        }

        // Display results
        resultDiv.innerText = `Prediction: ${data.prediction} (Confidence: ${data.confidence || "N/A"}%)`;
        timeDiv.innerText = `Processing Time: ${(end - start).toFixed(2)} ms`;

    } catch (error) {
        console.error("Prediction error:", error);
        resultDiv.innerText = "Error: Unable to get prediction.";
        timeDiv.innerText = "";
    }
}
