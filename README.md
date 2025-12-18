AI-Assisted Log Anomaly Detection System

Overview

This project implements a backend service that analyzes system logs and identifies anomalous behavior using machine-learning–based anomaly detection. It is designed to demonstrate how AI can assist security and backend teams in prioritizing suspicious events in large volumes of operational data.
The application exposes secure REST APIs for log analysis, health monitoring, and risk scoring, following production-style backend practices.

✨ Key Features

--> Batch ingestion of system log data via REST API
--> Unsupervised anomaly detection using Isolation Forest
--> Risk score assignment (0–100) to prioritize suspicious events
--> API key–based request authentication
--> Health check endpoint for service monitoring
--> OpenAPI (Swagger) documentation support

🛠 Tech Stack

Language: Python
Backend Framework: FastAPI
Machine Learning: Scikit-learn (Isolation Forest)
Data Processing: Pandas
API Server: Uvicorn

Project Structure
ai-log-anomaly-detection/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── feature_engineering.py
│
├── data/
│   └── logs.csv
│
├── models/
│   └── anomaly_model.pkl
│
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ How It Works

--> Log data is submitted to the API in JSON format
--> Relevant features (CPU and memory usage) are extracted
--> A trained Isolation Forest model evaluates each log entry
--> Anomalies are flagged and assigned a risk score
--> Results are returned via a structured API response

API Endpoints
### Health Check
   bash
    GET /health

🚀 Response:

{ "status": "ok" }

### Analyze Logs
  bash
    POST /analyze

### Headers

x-api-key: secure-api-key-123


Request Body

[
  {
    "process_name": "unknown.exe",
    "cpu_usage": 95,
    "memory_usage": 900
  }
]


Response

{
  "total_logs": 1,
  "anomalies_detected": 1,
  "results": [
    {
      "process_name": "unknown.exe",
      "cpu_usage": 95,
      "memory_usage": 900,
      "anomaly": "Yes",
      "risk_score": 100
    }
  ]
}

🚀 Running the Project Locally
1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Train the model
python train_model.py

4. Start the API server
python -m uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

📌 Use Case

--> This project simulates how backend and security teams can leverage machine learning to assist in:
--> Log monitoring
--> Security event triage
--> Anomaly detection
--> Risk-based alert prioritization

📜 Notes

o This is a proof-of-concept designed for learning and demonstration
o The architecture can be extended with databases, authentication services, and real log sources
o API keys should be stored securely using environment variables in production systems

Author

Developed by a Computer Science postgraduate with a focus on backend systems, security, and applied machine learning.
