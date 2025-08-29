# LogShield-ML🔒

This project focuses on building an intelligent security layer for web applications by analyzing server logs and access patterns. It detects anomalies, unusual behaviors, and potential malicious activity in real time, then responds with automated actions such as alerts or blocking suspicious IPs. By integrating AI/ML, the system continuously learns normal traffic behavior and adapts to evolving attack patterns, offering smarter and more proactive protection than traditional rule-based defenses.


### 1. **Core Concept**

* Your tool will:

  * **Ingest logs** (web server logs, application logs, access logs).
  * **Detect anomalies or malicious behavior** (SQLi attempts, XSS payloads, brute-force login attempts, unusual request rates).
  * **Take action** → either alert, block the request, or ban the IP temporarily.

This is basically an **ML-driven anomaly detection & response system** for web apps.

---

### 2. **Key Features to Build**

1. **Log Collector**

   * Pull Apache/Nginx logs, app logs, or reverse proxy logs.
   * Parse into structured format (e.g., JSON with IP, endpoint, user-agent, status code, request body).

2. **Rule-based Detection (baseline)**

   * Add static signatures (e.g., `SELECT * FROM`, `<script>`, `../../../etc/passwd`).
   * Track request rates (too many failed logins in X seconds → flag as brute-force).

3. **Anomaly Detection (AI/ML layer)**

   * Train a model on “normal traffic” (IP request frequency, URL paths, request size, status code patterns).
   * Use unsupervised ML (Isolation Forest, One-Class SVM, Autoencoders) to detect “weird” behavior.
   * Example: User normally requests `/home` and `/profile`, but suddenly starts blasting `/admin/login` with payloads.

4. **Response Engine**

   * When suspicious activity is found:

     * **Log-only** (for analysis).
     * **Alert** (send Slack/email alert).
     * **Block** (auto-update firewall rules / `.htaccess` / nginx `deny`).
     * **Kill session** (if integrated with app auth).

---

### 3. **Automation & Self-Learning**

* Feed flagged requests into your ML pipeline → system continuously “learns” what is normal vs abnormal.
* Add feedback loop → security analyst (you) can mark true/false positives.
* Over time, model improves detection accuracy.

---

### 4. **Tech Stack Ideas**

* **Log ingestion**: Python (log parsing), ELK stack (Elasticsearch, Logstash, Kibana) if you want visualization.
* **Detection**: Scikit-learn (Isolation Forest, SVM), PyTorch/TF (Autoencoder).
* **Action**: Python script to update `iptables` / `ufw` / `nginx` rules.
* **Bonus**: Expose as an API or dashboard → “AI-Powered WAF” look.

---

### 5. **How to Showcase It**

* Start small:

  * Rule-based log analyzer that alerts on anomalies.
* Then add ML:

  * Train on real Apache/Nginx logs (use public datasets if you don’t have your own).
* Finally:

  * Demo it in a Dockerized lab → attack your own web app with SQLi/XSS tools (sqlmap, wfuzz, Burp) and show your system catching/blocking.

---

## 📌 Project Roadmap (Phased Development)

### **Phase 0 → Passive Analysis**

* Performed passive **web log analysis** using a Kaggle dataset.
* Extracted insights: request distributions, anomalies, common endpoints.
* Built foundation for feature engineering and log parsing.

---

### **Phase 1 → Mini Web Server Setup**

* Built a **mini web server** running on `localhost:8080`.
* Stored all incoming requests in `access.log`.
* Automated a traffic generator script to continuously send requests.
* Observed logs in real-time using `tail -f access.log`.

---

### **Phase 2 → Real-Time Monitoring & Alerts**

* Created a real-time **log analyzer** that:

  * Reads `access.log` continuously.
  * Matches suspicious patterns (SQLi, XSS, Directory Traversal, Brute Force).
  * Displays alerts in terminal.
  * Stores alerts in a structured file `alerts.jsonl`.

---

### **Phase 3 → Dataset Creation**

* Converted raw logs into a **pretty formatted table** (`dataset_pretty.txt`) for human readability.
* Built a structured **CSV dataset (`output/dataset.csv`)** with:

  * Columns: `src_ip`, `timestamp`, `method`, `request`, `status`, `size`, `user_agent`, `attack_type`, `label`
  * Labels: `normal` / `malicious`
* Dataset now usable for ML training.

---

### **Phase 4 → Machine Learning Model**

* Trained a **RandomForest ML model** on `dataset.csv`.
* Used **80% training / 20% testing split**.
* Saved trained model as `output/model.pkl`.
* Achieved **74% accuracy** on test data.
* Scripts:

  * `train_model.py` → trains and saves the model.
  * `predict.py` → loads model, predicts malicious vs normal.

---

### **Phase 5 → Predict New Logs**

* Extended the system to:

  * Take **new/unseen logs** as input.
  * Predict whether they are `normal` or `malicious`.
  * Output results in structured format.
* Moves detection from “offline dataset analysis” → **real-time prediction**.

---

### **Phase 6 → Automated Blocklist & IP Blocking**

* Maintains a **list of malicious IPs**:

  * Can integrate with **threat intelligence feeds**.
  * Learns malicious IPs from predictions + rule detections.
* Response engine:

  * **Alert-only mode** → log the incident.
  * **Block mode** → auto-update firewall rules (`iptables` / `ufw`) or `nginx` deny rules.
* ML model + blocklist = **AI-driven Intrusion Prevention System**.

---

## 📊 Planned Enhancements

* Visualization of traffic & attack stats using **matplotlib/seaborn**.
* Dashboard integration (Flask + Chart.js, or ELK stack).
* Feedback loop to retrain ML model using analyst-labeled data.
* Dockerized deployment for lab simulation.
* adding more iot devices their data set and stuff

---

## 🎯 Final Outcome

By the end of Phase 6, you will have a **multi-layered AI-WAF prototype**:

* Parses & monitors logs in real-time.
* Detects anomalies via **rules + ML model**.
* **Alerts & auto-blocks** malicious traffic.
* Continuously learns & adapts to new threats.

This project evolves from a **basic log analyzer** → to an **AI-powered intrusion detection system (IDS)** → to a **self-learning WAF**.

---

✨ **Tags**: Cybersecurity, Machine Learning, Intrusion Detection, Log Analysis, AI-WAF

---
