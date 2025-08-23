# 🛡️ AI-Driven WAF — Phase 2 (Analyzer)

## 📌 Overview

This project is part of a **local Web Application Firewall (WAF) system** that simulates:

1. **Mini Web Server** — runs locally (logs all requests in Apache-style format).
2. **Traffic Generator** — simulates both normal and malicious traffic.
3. **WAF Analyzer (this module)** — tails the access logs in real time, scans for anomalies, and raises alerts.

The analyzer detects **common web attacks** (SQL Injection, XSS, Path Traversal, Admin scans) and monitors **request rates per IP** to flag **brute force attempts**.

---

## ⚡ Features

* 🔍 **Real-time request analysis** (live `tail -f` on `logs/access.log`)
* 🚨 **Regex-based detection** for:

  * SQL Injection (SQLi)
  * Cross-Site Scripting (XSS)
  * Path Traversal (`../`)
  * Admin/Login probes
* 🔒 **Brute force monitoring**

  * Flags IPs sending >50 requests within 20 seconds
* 📡 **Dual alerting**

  * **Live alerts on terminal** with IP, request, and type of anomaly
  * **Persistent alert storage** in `out/alerts.jsonl` for later analysis

---

## 🔧 Setup

### 1️⃣ Create and activate virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 2️⃣ Install dependencies

```bash
pip install flask requests
```

---

## ▶️ Usage

### Step 1: Start the mini web server

```bash
python3 app.py
```

* Runs Flask server at `http://localhost:8080`
* Writes logs to `logs/access.log`

---

### Step 2: Run the traffic generator

```bash
python3 attack_traffic.py
```

* Sends **normal + malicious requests** to the server
* Populates `logs/access.log` in real time

---

### Step 3: Run the WAF Analyzer

```bash
python3 waf_analyzer.py
```

* Continuously tails `logs/access.log`
* Prints alerts in **terminal**
* Saves alerts in **`out/alerts.jsonl`** for later analysis

---

## 🖥️ Example Output

### Live Terminal

```
[*] Real-time WAF Analyzer started...
[ALERT] SQLi detected from 192.168.1.10 → "GET /login.php?id=1' OR '1'='1 HTTP/1.1"
[ALERT] Possible brute force from 10.0.0.15 (>50 reqs/20s)
[ALERT] XSS detected from 123.45.67.89 → "GET /search?q=<script>alert(1)</script> HTTP/1.1"
```

### Stored Alerts (`out/alerts.jsonl`)

```json
{"type": "SQLi", "ip": "192.168.1.10", "log": "GET /login.php?id=1' OR '1'='1 HTTP/1.1", "time": "2025-08-23 19:30:02"}
{"type": "Brute Force", "ip": "10.0.0.15", "log": "N/A", "time": "2025-08-23 19:30:10"}
{"type": "XSS", "ip": "123.45.67.89", "log": "GET /search?q=<script>alert(1)</script> HTTP/1.1", "time": "2025-08-23 19:30:22"}
```

---

## 🚀 Future Enhancements

* Assign **severity scores** per signature
* Maintain an in-memory **blocklist of malicious IPs**
* Add **GeoIP enrichment** (country/city info)
* Build a **live dashboard** for stats and alerts

---
👉 Next natural steps for Phase 3 could be:

Blocking/mitigation logic (instead of just alerting, actually block bad IPs in real-time — e.g., update firewall rules or maintain an in-memory blocklist).

Alert enrichment (add request method, endpoint, user-agent, maybe GeoIP lookup).

Dashboard/visualization (web-based live monitoring of attacks instead of just terminal).

Configurable detection rules (let users update regex/patterns via a JSON/YAML rules file).
