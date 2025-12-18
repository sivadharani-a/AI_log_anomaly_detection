from fastapi import FastAPI, Header, HTTPException
from typing import Optional, List
import pandas as pd

from app.model import load_model, predict
from app.feature_engineering import extract_features

app = FastAPI(
    title="AI-Assisted Log Anomaly Detection",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


API_KEY = "secure-api-key-123"  


def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


model = load_model()

def calculate_risk(cpu_usage: int, memory_usage: int, is_anomaly: bool) -> int:
    """
    Returns a risk score between 0 and 100
    """
    base_score = min(cpu_usage + (memory_usage // 10), 100)
    return base_score if is_anomaly else base_score // 3


@app.get("/")
def root():
    return {"message": "AI-Assisted Log Anomaly Detection API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_logs(
    logs: List[dict],
    x_api_key: Optional[str] = Header(None)
):
    verify_api_key(x_api_key)

    df = pd.DataFrame(logs)

    required_fields = {"process_name", "cpu_usage", "memory_usage"}
    if not required_fields.issubset(df.columns):
        raise HTTPException(
            status_code=400,
            detail="Missing required log fields"
        )

    features = extract_features(df)

    predictions = predict(model, features)

    results = []
    anomaly_count = 0

    for i, row in df.iterrows():
        is_anomaly = predictions[i] == -1
        if is_anomaly:
            anomaly_count += 1

        risk_score = calculate_risk(
            row["cpu_usage"],
            row["memory_usage"],
            is_anomaly
        )

        results.append({
            "process_name": row["process_name"],
            "cpu_usage": row["cpu_usage"],
            "memory_usage": row["memory_usage"],
            "anomaly": "Yes" if is_anomaly else "No",
            "risk_score": risk_score
        })

    return {
        "total_logs": len(results),
        "anomalies_detected": anomaly_count,
        "results": results
    }
