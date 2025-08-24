import pandas as pd
import joblib
import os

# Paths
DATA_PATH = "output/dataset.csv"
MODEL_PATH = "output/model.pkl"

def main():
    # Load dataset
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)

    if "label" not in df.columns:
        raise ValueError("Dataset must contain a 'label' column")

    # Features (everything except label)
    X = df.drop("label", axis=1)
    y = df["label"]

    # Encode categorical features
    for col in X.columns:
        if X[col].dtype == "object":
            X[col] = X[col].astype("category").cat.codes

    # Load model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}. Run train_model.py first.")
    saved = joblib.load(MODEL_PATH)
    clf = saved["model"]
    label_encoder = saved["label_encoder"]

    # Encode labels to compare correctly
    y_encoded = label_encoder.transform(y)

    # Predict
    preds = clf.predict(X)

    # Decode predictions
    decoded_preds = label_encoder.inverse_transform(preds)

    # Show comparison
    results = pd.DataFrame({
        "Actual": y.values,
        "Predicted": decoded_preds
    })

    print("\n=== Predictions on Full Dataset ===")
    print(results.head(20))  # show first 20 rows
    acc = (results["Actual"] == results["Predicted"]).mean()
    print(f"\nOverall Accuracy on full dataset: {acc:.2f}")

if __name__ == "__main__":
    main()
