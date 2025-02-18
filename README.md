# BCBU-ZC AMP Classifier
<img src="image.png" alt="Tool Logo">

This project is a web application for classifying amino acid sequences as either Antimicrobial Peptides (AMPs) or Non-AMPs. It uses a machine learning model served via a Gradio interface.  The application allows users to input sequences either manually or by uploading a FASTA file.


Access the platform from [here](https://nonzeroexitali.github.io/AMP-Classifier-ZC/)  

## Features

*   **Dual Input Methods:**
    *   **Manual Input:** Enter amino acid sequences directly into a text area.
    *   **FASTA File Upload:** Upload standard FASTA files (`.fasta`, `.fa`, `.fna`).  Supports single-sequence FASTA files.
*   **Input Validation:**
    *   **Length Check:**  Ensures sequences are between 10 and 100 amino acids long.
    *   **Character Check:**  Verifies that sequences contain only standard amino acid characters (ACDEFGHIKLMNPQRSTVWY).
    *   **FASTA Format Check:** Validates uploaded files for correct FASTA format (header line starting with `>` and sequence lines).
    *   **File Type Check:** Only allows files with `.fasta`, `.fa`, or `.fna` extensions.
*   **Real-time Feedback:**
    *   **Character Count:** Displays the current sequence length.
    *   **Error Messages:** Provides clear error messages for invalid input.
    *   **Progress Bar:** Shows a progress indicator while the model is classifying.
    *   **Confidence Score:** Displays the model's confidence in its prediction.
*   **User Interface:**
    *   **Tabbed Interface:** Organizes content into "Prediction," "Model," and "About" sections.
    *   **Responsive Design:** Adapts to different screen sizes.
    *   **Tooltips:**  Provides helpful information on input requirements.
*   **Gradio Integration:**  Uses the Gradio library for easy interaction(Backend) with the machine learning model.

## Technologies Used

*   **HTML:**  For the structure of the web page.
*   **CSS:** For styling the user interface (including dark mode).
*   **JavaScript:** For handling user input, FASTA parsing, validation, interacting with the Gradio backend, and managing the UI.
*   **Gradio:**  For serving the machine learning model and providing a Python backend.  *This project assumes you have a Gradio backend already set up.*
* **Font Awesome:** For providing the icons in tabs.

## Prerequisites

*   **A running Gradio backend:** You need a Gradio app serving your AMP classification model.  The JavaScript code connects to this backend.  The provided code here assumes the backend is available at the endpoint specified in the `initClient()` function (currently `"nonzeroexit/AMP-Classifier"`).  You'll need to change this if your Gradio app is deployed elsewhere.  See the "Deployment" section for more details.
*   **A web server:** To serve the HTML, CSS, and JavaScript files.
  
## Setup and Usage

1.  **Clone the repository:**

    ```bash
    git clone <(https://github.com/NonZeroExitAli/AMP-Classifier-ZC/)>
    cd <(https://github.com/NonZeroExitAli)>
    ```

5.  **Use the Application:**
    *   Open the web page in your browser.
    *   **To enter a sequence manually:** Type or paste the amino acid sequence into the text area.
    *   **To upload a FASTA file:** Click the "Browse" button (or the file input area), select your FASTA file, and the sequence will be automatically loaded into the text area.
    *   Click the "Classify Sequence" button to get the prediction.

## File Structure
>Seq1
>
MEKAALIFIGLLLFSTCTQILAQSCNNDSDCTNLKCATKNIKCEQNKCQCLDERYIRAISLNTRSPRCNVQSCIDHCKAIGEVIYVCFTYH


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) <!-- Add a license badge if you have one -->
