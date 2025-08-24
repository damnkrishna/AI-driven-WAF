import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Path to dataset
DATA_PATH = "output/dataset.csv"
MODEL_PATH = "output/model.pkl"

def main():
    # Load dataset
    df = pd.read_csv(DATA_PATH)
    print(f"Dataset loaded with shape: {df.shape}")

    # Ensure 'label' column exists
    if "label" not in df.columns:
        raise ValueError("The dataset must have a 'label' column for training.")

    # Features (all columns except 'label')
    X = df.drop("label", axis=1)
    y = df["label"]

    # Encode categorical features (if not numeric)
    for col in X.columns:
        if X[col].dtype == "object":
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))

    # Encode labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate
    accuracy = clf.score(X_test, y_test)
    print(f"Model trained with accuracy: {accuracy:.2f}")

    # Save model + label encoder
    joblib.dump({"model": clf, "label_encoder": label_encoder}, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
