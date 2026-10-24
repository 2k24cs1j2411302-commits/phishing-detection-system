# 🔐 Phishing URL Detection System

A Machine Learning-based web application that analyzes URLs and identifies potentially phishing links. Built using Python and Streamlit, this project uses a trained machine learning model to classify a URL as **Phishing** or **Secure** based on its characteristics.

## 🚀 Features

- **URL Analysis:** Accepts a URL as input for analysis.
- **Machine Learning Prediction:** Uses a pre-trained model to classify URLs.
- **Feature Extraction:** Analyzes URL length, number of dots, digits, special characters, HTTPS usage, presence of `@`, and IP address patterns.
- **Interactive Web Interface:** Provides a simple interface using Streamlit.
- **Instant Results:** Displays a warning for potentially phishing URLs or a success message for URLs classified as secure.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-learn-compatible model
- **Model Serialization:** Joblib
- **Data Processing:** Regular Expressions (Regex)

## 📂 Project Structure

```text
phishing-detection-system/
│
├── app.py                    # Streamlit application
├── phishing_model.pkl        # Trained ML model
├── phishing_url_dataset.csv  # URL dataset
├── Untitled.ipynb            # Jupyter Notebook
├── requirements.txt          # Project dependencies
├── .gitignore                # Ignored files
└── README.md                 # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd phishing-detection-system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit joblib scikit-learn
```

If your notebook uses additional libraries, install those as well.

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🧠 How It Works

1. The user enters a URL into the Streamlit application.
2. The application extracts seven URL characteristics:
   - URL length
   - Number of dots
   - Number of digits
   - Presence of the `@` symbol
   - Whether the URL starts with `https`
   - Count of selected special characters
   - Presence of an IPv4-style address pattern
3. These features are passed to the pre-trained machine learning model.
4. The model predicts the URL's class.
5. The application displays either **PHISHING DETECTED** or **SECURE**.

## 💻 Example

**Input URL:**

```text
http://example.com/login
```

**Output:** The application displays a prediction based on the trained model.

*Note: The actual prediction depends on the model and its training data.*

## 📊 Dataset

The project includes `phishing_url_dataset.csv`, which can be used to explore URL data and support the model-training workflow.

The dataset's exact size, feature schema, and class distribution should be documented after inspecting the CSV file.

## 🔮 Future Improvements

- Improve feature extraction with additional URL and domain characteristics.
- Evaluate the model using accuracy, precision, recall, F1-score, and a confusion matrix.
- Add confidence scores and clearer prediction explanations.
- Develop a more advanced user interface.
- Deploy the application online.
- Add tests for URL parsing and prediction behavior.

## ⚠️ Limitations

- Predictions depend on the quality and scope of the training data.
- A URL classified as secure is not guaranteed to be safe.
- The application analyzes URL characteristics and
