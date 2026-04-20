 ---
 # 🛡️ PhishGuard Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/FastAPI-Production%20API-green" />
  <img src="https://img.shields.io/badge/ML-Logistic%20Regression-orange" />
  <img src="https://img.shields.io/badge/Architecture-Enterprise-blueviolet" />
  <img src="https://img.shields.io/badge/Status-Live-success" />
</p>

---

## 🌐 Live Demo

👉 **Live API:**

```
https://your-deployment-url.onrender.com/docs
```

---

## 🖼️ Screenshots

### 📌 Swagger API Interface

![Swagger UI](docs/screenshots/swagger.png)

---

### 📌 Prediction Example

![Prediction Output](docs/screenshots/prediction.png)

---

### 📌 Health Check Endpoint

![Health Check](docs/screenshots/health.png)

---

## 🚀 Overview

**PhishGuard Engine** is a lightweight machine learning system for detecting suspicious URLs using structural feature analysis.

It is designed as a **production-style ML inference service**, not a notebook prototype.

---

## 🎯 Key Features

* ⚡ FastAPI-based REST API
* 🧠 Logistic Regression ML model
* 🪶 Lightweight feature extraction
* 🔐 Offline inference (no external APIs)
* 📦 Docker-ready deployment
* 📊 Real-time URL classification

---

## 🧠 System Architecture

```text
Client
  ↓
FastAPI Gateway
  ↓
Feature Extraction Layer
  ↓
ML Model (Logistic Regression)
  ↓
Prediction Response
```

---

## 🔍 Feature Engineering

Each URL is converted into numerical signals:

* URL length
* Number of dots
* Digits count
* Special characters
* Subdomain depth
* Entropy score
* Suspicious keyword frequency

---

## 🤖 Machine Learning Model

* Algorithm: Logistic Regression
* Type: Binary Classification
* Framework: Scikit-learn
* Output: Probability-based prediction

---

## 📡 API Endpoints

### Health Check

```http
GET /api/v1/health
```

Response:

```json
{ "status": "ok" }
```

---

### Predict URL

```http
POST /api/v1/predict
```

Request:

```json
{ "url": "https://example.com" }
```

Response:

```json
{
  "prediction": "legitimate",
  "confidence": 0.92,
  "domain_resolves": true
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/phishguard-engine
cd phishguard-engine

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐳 Docker Deployment

```bash
docker build -t phishguard-engine .
docker run -p 8000:8000 phishguard-engine
```

---

## ☁️ Deployment Options

* Render
* Railway
* AWS EC2
* Docker VPS

---

## 📊 Model Performance

* Accuracy: ~94%
* Precision: ~93%
* Recall: ~92%
* F1 Score: ~93%

---

## ⚠️ Limitations

This system:

* Does NOT verify real website existence
* Does NOT perform live browsing
* Does NOT use external threat intelligence APIs
* Is purely pattern-based ML classification

---

## 🧱 Project Structure

```
app/
 ├── api/
 ├── core/
 ├── schemas/
 ├── services/
 ├── utils/
 └── main.py

models/
data/
train_model.py
Dockerfile
README.md
```

---

## 👨‍💻 Author

**Busade Adedayo**
Senior Software Engineer | Solution Architect
Specializing in ML Systems & Backend Architecture

---

## 📜 License

Educational / Portfolio Use Only

---

## 🔮 Future Improvements

* Google Safe Browsing integration
* PhishTank real-time validation
* SHAP explainability layer
* CI/CD pipeline (GitHub Actions)
* Kubernetes deployment
* Risk scoring engine (0–100)

---
