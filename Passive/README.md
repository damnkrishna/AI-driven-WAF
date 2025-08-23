# Web Log Analyzer

A Python project to analyze web server access logs, summarize requests by IP, HTTP status codes, and detect suspicious requests.  
Generates a clean, structured report in `output/report.txt`.

---

## 📂 Project Structure

```
web-log-analyzer/
├── sample_data/
│   ├── access.log
│   └── client_hostname.csv
├── output/
│   └── report.txt
├── log_analyzer.py
├── setup.sh
├── download_data.sh
└── requirements.txt
```

- `sample_data/` → Contains the web server logs and client hostnames.  
- `output/` → Stores the generated analysis report.  
- `log_analyzer.py` → Python script to parse logs and generate the report.  
- `setup.sh` → Sets up virtual environment and installs dependencies.  
- `download_data.sh` → Downloads and extracts dataset from Kaggle.  
- `requirements.txt` → Lists all Python packages required for the project.

---
<img width="1536" height="200" alt="image" src="https://github.com/user-attachments/assets/1de07b2c-3548-46dc-a45b-d9dd2957825f" />


## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd web-log-analyzer
```

### 2. Run Setup Script  
This will create a virtual environment and install all required Python packages:
```
bash setup.sh
```

### 3. Download Dataset  
Download and extract the dataset automatically:
```
bash download_data.sh
```

This will create the `sample_data/` folder and add:  
- `access.log`  
- `client_hostname.csv`  

### 4. Run the Log Analyzer  
```
python3 log_analyzer.py
```

This generates a clean report in `output/report.txt`.

The report includes:  
- Total unique IPs  
- Top 5 IP addresses by request count  
- HTTP status code summary  
- Suspicious requests detected  

---

## 📊 Sample Output

```
=== Web Log Analysis Report ===

📊 Total Unique IPs: 258606

🔝 Top 5 IPs
----------------------------------------
IP Address           Requests
66.249.66.194       353483
66.249.66.91        314522
151.239.241.163      92475
66.249.66.92         88332
91.99.30.32          45979

📈 Status Codes
----------------------------------------
Status       Count
200         9579824
404          105011
302          199835
...

⚠️ Suspicious Requests Detected: 2707
```

---

## 💻 Notes

Make sure you always activate the virtual environment before running the script:  
```
source ~/myenv/bin/activate
```

The project is designed to be self-contained; anyone can set it up by following these instructions.

---

## 📚 Dependencies
All Python dependencies are listed in `requirements.txt`:
- pandas  
- numpy  
- matplotlib  
- seaborn  

---
