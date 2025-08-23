# Attack Traffic Generator

This script (`attack_traffic.py`) generates simulated web traffic (both normal and malicious) against a locally running Flask server.  
It is useful for testing and building datasets for Web Application Firewall (WAF) or log analysis projects.

---

## 🚀 Features
- Sends **normal user requests** (search queries, login attempts, etc.).
- Sends **malicious requests** (SQL Injection, XSS, path traversal, bots).
- Uses **multiple threads** to simulate concurrent clients.
- Automatically randomizes **User-Agent headers**.
- Continuously runs and writes all logs to your Flask server's `logs/access.log`.

---

## 📦 Requirements

Make sure your system is up to date and has Python 3 installed:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
````

Then install the required Python libraries:

```bash
pip3 install requests
```

---

## ⚙️ Usage

### 1. Start your Flask server

Run the Flask app (from your `app.py`):

```bash
python3 app.py
```

This will start the server on `http://localhost:8080` and create a `logs/access.log` file.

### 2. Run the traffic generator

In another terminal, run:

```bash
python3 attack_traffic.py
```

This will start sending both normal and malicious requests to the Flask server.

### 3. Watch the logs live

Open another terminal and run:

```bash
tail -f logs/access.log
```

Now you can observe requests being logged in real-time.

<img width="958" height="430" alt="image" src="https://github.com/user-attachments/assets/73a84337-45c7-4d67-9b70-70e222287def" />

---

## 🛑 Notes

* By default, the script targets `http://localhost:8080`. Update the `BASE` variable in `attack_traffic.py` if your server runs on a different host/port.
* The script is **for testing only**. Do not run it against servers you don’t own or have permission to test.

