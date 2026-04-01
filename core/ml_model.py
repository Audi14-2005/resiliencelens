import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model():
    df = pd.read_csv("data/simulated_data.csv")

    # Encode categorical data
    le = LabelEncoder()
    for col in ["service", "cloud", "region", "asn", "cloud_status", "network_status"]:
        df[col] = le.fit_transform(df[col])

    X = df.drop(["timestamp", "failure"], axis=1)
    y = df["failure"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    print(f"Model Accuracy: {accuracy:.2f}")

    return model