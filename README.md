# 🛡️ Social Media Threat Analyzer

An AI-powered web application that analyzes social media profile screenshots to identify potentially fake profiles and bot accounts using Optical Character Recognition (OCR), Machine Learning, and Cybersecurity concepts.

---

## 📌 Overview

The rapid growth of social media platforms has also increased the number of fake profiles, bot accounts, impersonation attempts, and online scams. Many users struggle to determine whether a profile is genuine or suspicious.

The **Social Media Threat Analyzer** is designed to assist users by analyzing screenshots of social media profiles. The system extracts publicly visible information from the uploaded screenshot, processes the extracted data, and predicts whether the profile resembles a genuine or fake account using a Machine Learning model.

Instead of relying on social media APIs, the project performs screenshot-based analysis, making it simple, accessible, and platform-independent.

---

## ✨ Features

- 📷 Upload social media profile screenshots
- 🔍 OCR-based text extraction using Tesseract OCR
- 🤖 AI-powered fake profile detection
- 📊 Machine Learning prediction using Random Forest
- 🛡️ Trust Score calculation
- ⚠️ Bot Probability estimation
- 👤 Username Risk Analysis
- 📝 Bio Scam Keyword Detection
- 📈 Analytics Dashboard
- 📜 Scan History
- 💡 Cybersecurity Recommendations
- 🎨 Responsive and user-friendly interface

---

# 🏗️ System Workflow

```text
User Uploads Screenshot
          │
          ▼
Image Preprocessing (OpenCV)
          │
          ▼
OCR Extraction (Tesseract)
          │
          ▼
Text Processing (SpaCy)
          │
          ▼
Feature Extraction
          │
          ▼
Random Forest Classifier
          │
          ▼
Risk Assessment
          │
          ▼
Security Report
```

---

# 🧠 Technologies Used

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- Random Forest Classifier

## Computer Vision

- OpenCV

## OCR

- Tesseract OCR
- PyTesseract

## Natural Language Processing

- SpaCy

## Database

- SQLite

## Data Processing

- Pandas
- NumPy

## Model Persistence

- Joblib

---

# 📂 Project Structure

```
Social-Media-Threat-Analyzer
│
├── dataset
│   └── instagram.csv
│
├── model
│   └── fake_profile_model.pkl
│
├── static
│   ├── uploads
│   ├── css
│   └── images
│
├── templates
│   ├── index.html
│   ├── result.html
│   ├── analytics.html
│   └── history.html
│
├── app.py
├── train_model.py
├── database.db
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/hitheshsjecmca/Social-Media-Threat-Analyzer.git
```

Move into the project directory.

```bash
cd Social-Media-Threat-Analyzer
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Install Tesseract OCR

Download and install **Tesseract OCR**.

Windows users should update the path inside **app.py**.

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## Train the Machine Learning Model

```bash
python train_model.py
```

This generates:

```
fake_profile_model.pkl
```

---

## Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📊 Machine Learning

The application uses a **Random Forest Classifier**, a supervised machine learning algorithm trained on an Instagram Fake Account Dataset.

The model learns patterns from profile characteristics such as:

- Username Pattern
- Profile Picture Availability
- Full Name Information
- Bio Length
- External URL
- Account Privacy
- Number of Posts
- Followers
- Following

Output:

```
0 → Genuine Profile

1 → Fake Profile
```

---

# 🔍 OCR Pipeline

The uploaded screenshot passes through the following stages:

```
Screenshot
      │
      ▼
OpenCV
(Image Enhancement)
      │
      ▼
Tesseract OCR
(Text Extraction)
      │
      ▼
SpaCy
(Text Processing)
      │
      ▼
Feature Extraction
```

Extracted Information includes:

- Username
- Followers
- Following
- Posts
- Biography
- External Links

---

# 📈 Security Metrics

The application generates several indicators to assist users.

### ✔ Prediction

- Genuine Profile
- Fake Profile

### ✔ Confidence Score

Shows how confident the machine learning model is in its prediction.

### ✔ Trust Score

Calculated using profile characteristics including:

- Number of Posts
- Followers
- Following Ratio
- Account Privacy

### ✔ Bot Probability

Estimates the likelihood that the account behaves like an automated bot.

### ✔ Username Risk

Detects suspicious username patterns.

### ✔ Bio Risk

Identifies scam-related keywords present in profile biographies.

---

# 📸 Application Screens

- Home Page
- Upload Screenshot
- Profile Analysis
- Analytics Dashboard
- Scan History

*(You can add screenshots here after uploading them.)*

---

# 🚀 Future Enhancements

- Multi-platform support (Facebook, LinkedIn, X, Telegram)
- Deep Learning integration
- Reverse Image Search
- Real-time Profile Analysis
- Social Media API Integration
- Mobile Application
- Explainable AI Dashboard
- Advanced Phishing Detection

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning
- Random Forest Classification
- Optical Character Recognition
- Computer Vision
- Natural Language Processing
- Flask Web Development
- Cybersecurity Concepts
- Image Processing
- SQLite Database Management
- Git & GitHub

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is developed for educational and academic purposes.

---

# 👨‍💻 Author

**Hithesh**

MCA Student | AI & Cybersecurity Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star!
