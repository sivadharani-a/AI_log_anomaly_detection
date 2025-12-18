import pandas as pd

def extract_features(df: pd.DataFrame):
    features = df[['cpu_usage', 'memory_usage']]
    return features
