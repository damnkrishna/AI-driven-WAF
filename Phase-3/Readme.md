# 🚀 Phase 3 – Machine Learning for Anomaly Detection in Web Logs

This phase focuses on **training a Machine Learning (ML) model on historical web server logs** to detect malicious traffic (SQLi, XSS, directory traversal, etc.) in **real-time incoming logs**.

---

## 📌 Project Overview

1. **Data Sources**

   * `malicious_logs.txt` → IDS-style dataset containing only malicious requests.
   * `all_logs.txt` → Full web access logs containing both normal and malicious traffic.

2. **Goal**

   * Convert raw logs into a **structured CSV dataset**.
   * Train ML models to **differentiate normal vs. malicious requests**.
   * Deploy a pipeline that can process **new real-time logs** and flag anomalies.

---

## 🛠️ Steps Implemented

### 1. Data Preprocessing

* Extract structured fields from raw log lines:

  * `src_ip`, `dst_ip`, `timestamp`, `method`, `url`, `status`, `bytes`, `user_agent`, `label`
* Label requests:

  * `normal` = benign requests
  * `malicious` = attack requests (from malicious dataset or pattern detection)
* Remove duplicates and clean noise (crawler/bot traffic if irrelevant).

### 2. Dataset Generation

* Merge `malicious_logs.txt` and `all_logs.txt`.
* Save final dataset as `dataset.csv`.
* Example row:

| src\_ip         | dst\_ip         | timestamp            | method | url                   | status | bytes | user\_agent       | label     |
| --------------- | --------------- | -------------------- | ------ | --------------------- | ------ | ----- | ----------------- | --------- |
| 138.176.237.216 | 138.176.237.216 | 23/Aug/2025:22:27:08 | GET    | /login.php?user=alice | 200    | 40    | Mozilla/5.0 (bot) | malicious |

### 3. Model Training

* Use the structured dataset to train ML models (e.g., **Random Forest, XGBoost, Logistic Regression**).
* Features extracted:

  * Request method (GET/POST)
  * URL/query length
  * Special characters in URL (e.g., `'`, `<script>`, `../`)
  * Response status code
  * Bytes transferred
  * User-Agent keywords

### 4. Real-Time Detection

* New logs are parsed in the same way.
* Trained model predicts if each request is **normal** or **malicious**.
* Can be integrated with streaming tools (Kafka, RabbitMQ) or log forwarders (Filebeat, Fluentd).

---

## ▶️ How to Run

### 1. Preprocess Logs

```bash
python3 log_to_csv.py
```

* Input: `malicious_logs.txt`, `all_logs.txt`
* Output: `dataset.csv`

### 2. Train Model

```bash
python3 train_model.py
```

* Loads `dataset.csv`
* Trains & saves ML model as `model.pkl`

### 3. Real-Time Detection

```bash
python3 detect_realtime.py new_logs.txt
```

* Input: New log file (`new_logs.txt`)
* Output: Predictions (Normal/Malicious) printed or saved as CSV

---

## 📊 Future Improvements

* Expand features with **NLP (TF-IDF, embeddings)** on request URLs.
* Build a **streaming pipeline** for real-time classification.
* Add **attack categories** (SQLi, XSS, Path Traversal) instead of just `malicious`.
* Integrate with **SIEM dashboards** for visualization.

---


✅ With this phase, you now have an ML pipeline that learns from past log patterns and detects anomalies in real-time.


