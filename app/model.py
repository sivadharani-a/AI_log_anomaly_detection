import joblib
from sklearn.ensemble import IsolationForest

MODEL_PATH = "models/anomaly_model.pkl"

def train_model(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    model.fit(X)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, X):
    return model.predict(X)
