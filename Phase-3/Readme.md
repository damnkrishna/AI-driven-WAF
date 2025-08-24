# 🚀 Phase 3 – Dataset conversion to train ML model

This phase focuses on **training a Machine Learning (ML) model on historical web server logs** to detect malicious traffic (SQLi, XSS, directory traversal, etc.) in **real-time incoming logs**.

---

This project focuses on analyzing and labeling web server logs to identify suspicious or malicious requests (e.g., SQL Injection, XSS, Directory Traversal).  
It organizes log data into a **human-readable format** as well as a **structured CSV dataset** suitable for training machine learning models in later phases.

---

## Features Implemented So Far
1. **Log Parsing (`label.py`)**  
   - Reads raw web server logs (`logs/access.log`).  
   - Detects suspicious patterns (SQL injection, XSS, directory traversal, etc.).  
   - Labels each log entry as either **Normal** or **Malicious**.  
   - Assigns an **attack type** if malicious (otherwise left blank).  

2. **Prettified Dataset (`output/dataset_pretty.txt`)**  
   - Nicely formatted logs with aligned columns.  
   - Automatically adjusts column spacing based on the longest entry in each column.  
   - Easy to read for humans when analyzing raw requests.  

3. **CSV Dataset for ML (`output/dataset.csv`)**  
   - Stores logs in structured format:
     ```
     src_ip,timestamp,method,url,status,attack_type,label
     ```
   - `label`: `Normal` or `Malicious`.  
   - `attack_type`: Specific attack (e.g., SQLi, XSS, Directory Traversal) or blank for normal requests.  
   - This CSV will later be used to train ML models for log classification.  

---

## Project Phase Progress
- **Phase 0**: Project setup (directory structure, basic file handling). ✅  
- **Phase 1**: Parsing raw access logs. ✅  
- **Phase 2**: Detecting suspicious patterns and labeling. ✅  
- **Phase 3**: Generating datasets for ML training. ✅  

Currently, the project outputs:
- `dataset_pretty.txt` → Human-readable aligned dataset.  
- `dataset.csv` → ML training dataset.  

---

## Next Steps
- **Phase 4**: Train a machine learning model (e.g., Logistic Regression, Random Forest, or an LSTM for sequences) on `dataset.csv`.  
- **Phase 5**: Implement real-time log analysis (streaming detection).  
- **Phase 6**: Build a small dashboard or CLI tool to visualize suspicious activity.  

---

## Running the Project

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd web-log-analyzer
````

### 2. Run the Script

```bash
python3 label.py
```

* The script will read `logs/access.log`.
* Output will be stored inside the `output/` folder.

---

## Example Output

### dataset\_pretty.txt

```
IP              Timestamp           Method   URL                           Status   Attack_Type         Label
192.168.1.10    [24/Aug/2025:11:32] GET      /index.html                   200      -                  Normal
192.168.1.15    [24/Aug/2025:11:33] GET      /index.php?id=1 UNION SELECT  500      SQL Injection      Malicious
```

### dataset.csv

```
src_ip,timestamp,method,url,status,attack_type,label
192.168.1.10,[24/Aug/2025:11:32],GET,/index.html,200,,Normal
192.168.1.15,[24/Aug/2025:11:33],GET,/index.php?id=1 UNION SELECT,500,SQL Injection,Malicious
```

---

## Tech Stack

* **Python 3**
* **Regex** for suspicious pattern detection
* **CSV module** for dataset generation

---

✅ With this phase, you now have an ML pipeline that learns from past log patterns and detects anomalies in real-time.


