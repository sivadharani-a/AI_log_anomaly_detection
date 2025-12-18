import pandas as pd
from app.feature_engineering import extract_features
from app.model import train_model

df = pd.read_csv("data/logs.csv")
X = extract_features(df)
train_model(X)

print("Model trained and saved successfully.")
