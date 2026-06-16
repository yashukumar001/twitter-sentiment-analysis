# 🚀 Twitter Sentiment Analysis Web Application

A modern web-based Sentiment Analysis application built using **Python**, **Flask**, and **Deep Learning concepts** to classify user-entered text as **Positive** or **Negative** sentiment.

The project demonstrates the complete Machine Learning workflow, including text preprocessing, sentiment classification, model training, inference, and web deployment through an interactive user interface.

---

# 📌 Project Overview

Sentiment Analysis is a Natural Language Processing (NLP) task that identifies emotional tone within textual data.

This application allows users to enter tweets, comments, reviews, or any text input and receive an instant sentiment prediction through a user-friendly web interface.

The project was designed to explore:

* Natural Language Processing (NLP)
* Sentiment Classification
* Text Preprocessing
* Deep Learning Architectures
* Flask Web Development
* Model Deployment Concepts

---

# 🎯 Key Features

✅ Real-Time Sentiment Prediction

✅ Interactive Web Interface

✅ Text Preprocessing Pipeline

✅ Sentiment Classification Engine

✅ Flask-Based Backend

✅ Modern Responsive UI

✅ Machine Learning Workflow Integration

✅ End-to-End Project Deployment Structure

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Machine Learning & NLP

* PyTorch
* NLTK
* Scikit-Learn
* Pandas
* NumPy

## Web Development

* Flask
* HTML5
* CSS3

## Development Tools

* Git
* GitHub
* VS Code

---

# 🧠 Machine Learning Workflow

The project follows a complete NLP pipeline:

```text
User Input
     ↓
Text Cleaning
     ↓
Tokenization
     ↓
Vocabulary Mapping
     ↓
Feature Representation
     ↓
Sentiment Prediction
     ↓
Result Display
```

---

# ⚙️ Project Architecture

```text
┌────────────────────┐
│ User Input Text    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Text Preprocessing │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Sentiment Model    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Prediction Engine  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Flask Web App      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Browser Output     │
└────────────────────┘
```

---

# 📂 Project Structure

```text
twitter-sentiment-analysis/

│
├── app.py
├── model.py
├── train.py
├── predict.py
├── check_dataset.py
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
```

---

# 🔍 Text Preprocessing

The application performs multiple preprocessing operations:

* Lowercasing
* URL Removal
* Punctuation Removal
* Tokenization
* Vocabulary Creation
* Sequence Encoding

These steps help convert raw text into a machine-readable format suitable for sentiment classification.

---

# 🌐 Web Application Interface

The application provides a clean and responsive interface where users can:

1. Enter text
2. Click Analyze Sentiment
3. Receive instant sentiment prediction

Example:

```text
Input:
I absolutely love this product.

Output:
Positive 😊
```

```text
Input:
This is the worst service ever.

Output:
Negative 😞
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start Flask server:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 📈 Future Enhancements

Planned improvements include:

* LSTM Integration
* Confidence Score Display
* Sentiment Probability Graphs
* User History Tracking
* Dark/Light Theme Toggle
* Cloud Deployment
* API Endpoints
* Multi-Class Sentiment Analysis

---

# 💡 Learning Outcomes

Through this project, the following concepts were explored:

* Natural Language Processing
* Sentiment Analysis
* Flask Web Development
* Deep Learning Fundamentals
* Model Training & Evaluation
* Git & GitHub Workflow
* Project Deployment Concepts

---

# 📸 Screenshots

Add screenshots of:

* Home Page
* Positive Prediction
* Negative Prediction

inside a `screenshots/` folder.

Example:

```text
screenshots/
├── homepage.png
├── positive_prediction.png
└── negative_prediction.png
```

---

# 👨‍💻 Author

**Yashu Kumar**

Computer Science Engineering Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Natural Language Processing
* Software Development

---

# ⭐ Acknowledgements

This project was developed for learning and portfolio purposes to gain hands-on experience in Machine Learning, Natural Language Processing, and Full-Stack Application Development.
