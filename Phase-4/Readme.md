# 🚀 Model Training & Prediction Guide

This guide explains how to train a Machine Learning model using `dataset.csv`, save it, and then use it for predictions.
It includes scripts for **training a model** and **making predictions** with accuracy evaluation.  


---

## 📂 Files

* `dataset.csv` → Your labeled dataset (contains request data + labels).
* `train_model.py` → Script to train and save the ML model.
* `predict.py` → Script to load the saved model and make predictions.

---
# Requirements

This project needs the following Python libraries:

- **pandas** → for loading and handling `dataset.csv`  
- **scikit-learn** → for training and prediction (ML models)  
- **joblib** → for saving and loading the trained model  

## Installation

You can install all requirements with:

```bash
pip install -r requirements.txt
```

## 🏋️ Training the Model

1. Make sure `dataset.csv` exists in your project folder.

2. Run the training script:

   ```bash
   python3 train_model.py
   ```

3. This will:

   * This will read `output/dataset.csv`
   * Train a machine learning model on the data
   * Save the trained model to:

  ```
  output/model.pkl
  ```

---


## Make Predictions

Run the prediction script to test the trained model:

```bash
python3 predict.py
```

* This will:

  * Load `output/dataset.csv`
  * Load `output/model.pkl`
  * Run predictions
  * Print accuracy on the dataset

---

## ✅ Example Workflow

```bash
# Train model
python3 train_model.py

# Run predictions and check accuracy
python3 predict.py
```

## ⚡ Workflow Summary

1. Update/clean `dataset.csv`
2. Train the model → `python3 train_model.py`
3. Predict with saved model → `python3 predict.py `




---

## 🔮 Next Steps (Optional Enhancements)

* Accept **new unseen data** for predictions instead of reusing dataset.csv
* Add **visualizations** (confusion matrix, feature importance, etc.)
* Experiment with different ML algorithms

