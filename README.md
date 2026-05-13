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
https://phishguard.busade.dev/docs
```

---

## 🖼️ Screenshots

### 📌 Swagger API Interface

![Swagger UI](docs/screenshots/swagger.png)

---

### 📌 Prediction Example

![Prediction Phishing Output](docs/screenshots/prediction-phishing.png)

![Prediction Legitimate Output](docs/screenshots/prediction-legitimate.png)

---

### 📌 Health Check Endpoint

![Health Check](docs/screenshots/health.png)

---

### 📌 Running Docker Image

![Running Docker Image](docs/screenshots/running-docker.png)

---

## 🚀 Overview

### 🛡️ PhishGuard Engine
**Busade PhishGuard Engine** is a high-performance, production-grade microservice dedicated to real-time URL threat intelligence. Moving beyond experimental notebooks, this system implements a complete ML inference pipeline designed for low-latency detection and seamless architectural integration.

#### 🚀 Engineering Highlights
***Production-First Architecture:** Built with FastAPI using the modern lifespan pattern for optimized resource management and startup efficiency.

**High-Speed Inference:** Implements structural feature extraction for ML classification, delivering sub-millisecond threat scoring without the overhead of heavy external dependencies.

**Cloud-Native & DevOps Ready:** Fully containerized with Docker, featuring a specialized Makefile workflow and automated CI/CD deployment pipelines to Render.

**Enterprise Standards:** Features structured logging, comprehensive health monitoring, and an interactive OpenAPI (Swagger) interface for rapid integration testing.

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

## 📂 Dataset

Add:

Due to size constraints, raw datasets are not included in this repository.

To reproduce training:

1. Download phishing dataset from Kaggle  
2. Download PhishTank dataset  
3. Prepare legitimate URL dataset  
4. Run:

```bash
python src/dataset_builder.py
```

---

# 🔥 Senior-Level Touch (Highly Recommended)

Create:

```bash
mkdir data/sample
```

> Add small file:

**data/sample/sample_urls.csv**

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
git clone https://github.com/olubusade/phishguard-engine
cd phishguard-engine

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐳 Docker Deployment

```bash
## 🚀 PhishGuard Engine - Installation & Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.12 (for local venv testing)

### Local Development (Using Docker)
We use a `Makefile` to simplify Docker operations. 

1. **Build the image:**
```bash
   make build
```
2. **Run the engine:**
```bash
make run
```
The API will be available at http://localhost:8000 and Swagger docs at http://localhost:8000/docs.

3. **Stop the engine:**

```bash
make stop
```
4. **View live logs:**

```bash
make logs
```
5. **Quick Refresh (Rebuild & Restart):**

```Bash
make up
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

## 👤 ABOUT THE ENGINEER

**Busade Adedayo**
*Senior Software Engineer / Solution Architect (Healthcare Systems)*

* 10+ years of total experience in full-stack engineering and systems architecture.
* 7+ years specialized in HealthTech, architecting and scaling production-grade Electronic Medical Record (EMR) systems.**Electronic Medical Record (EMR)** systems
Led architecture and development of domain-driven, modular healthcare platforms used in real clinical workflows
Strong focus on:
*✔  Clinical workflow digitization (SOAP notes, vitals, prescriptions)*
*✔ System architecture & scalability (DDD, modular monolith design)*
*✔ Healthcare interoperability (FHIR R4 standards)*
*✔ Security & Compliance: Specialized in RBAC/PBAC, HIPAA-aligned audit logging, and "Break-the-Glass" (BTG) emergency access protocols*
*✔ Experienced in designing enterprise backend systems with observability, logging, and monitoring layers*
*✔ AWS Cloud Practitioner certified | Preparing for AWS Solutions Architect - Associate*
*✔ **Passionate about building global-standard healthcare infrastructure from Africa for global markets*
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
