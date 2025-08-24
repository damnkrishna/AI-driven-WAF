# 🚀 Model Training & Prediction Guide

This guide explains how to train a Machine Learning model using `dataset.csv`, save it, and then use it for predictions.

---

## 📂 Files

* `dataset.csv` → Your labeled dataset (contains request data + labels).
* `train_model.py` → Script to train and save the ML model.
* `predict.py` → Script to load the saved model and make predictions.

---

## 🏋️ Training the Model

1. Make sure `dataset.csv` exists in your project folder.

2. Run the training script:

   ```bash
   python3 train_model.py
   ```

3. This will:

   * Load `dataset.csv`
   * Train a machine learning classifier
   * Save the model as `model.pkl`

---

## 🔍 Using the Model for Predictions

1. Once the model is saved (`model.pkl`), you can make predictions with:

   ```bash
   python3 predict.py "GET /index.php?id=1 UNION SELECT password FROM users"
   ```

2. Output will show whether the request is:

   * `Normal`
   * or `Malicious` (with predicted attack type, if included)

---

## ⚡ Workflow Summary

1. Update/clean `dataset.csv`
2. Train the model → `python3 train_model.py`
3. Predict with saved model → `python3 predict.py "<log/request>"`

