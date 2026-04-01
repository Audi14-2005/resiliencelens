import pandas as pd
from sklearn.ensemble import IsolationForest

def train_anomaly_model():
    df = pd.read_csv("data/simulated_data.csv")

    df["latency"] = df["latency"]

    model = IsolationForest(contamination=0.1)
    model.fit(df[["latency"]])

    return model


def detect_anomaly(model, event):
    value = [[event["latency"]]]
    result = model.predict(value)

    return result[0] == -1  # -1 means anomaly