import json
import subprocess
import time
from datetime import datetime

ALERTS_FILE = "out/alerts.jsonl"
BLOCKLIST_FILE = "out/blocklist.jsonl"
ACCESS_LOG = "logs/access.log"

# Load blocked IPs from blocklist
def load_blocklist():
    blocked = set()
    try:
        with open(BLOCKLIST_FILE) as f:
            for line in f:
                blocked.add(json.loads(line)["ip"])
    except FileNotFoundError:
        pass
    return blocked

# Add new IP to blocklist file
def add_to_blocklist(ip, reason):
    blocked = load_blocklist()
    if ip not in blocked:
        entry = {"ip": ip, "reason": reason, "time": str(datetime.now())}
        with open(BLOCKLIST_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return True
    return False

# Block IP using iptables
def block_ip(ip):
    try:
        subprocess.run(["sudo", "iptables", "-I", "INPUT", "1", "-s", ip, "-j", "DROP"], check=True)
        print(f"[BLOCKED] {ip}")
    except Exception as e:
        print(f"[ERROR] Could not block {ip}: {e}")

# Tail the access log in real-time
def tail_log(filename):
    with open(filename) as f:
        f.seek(0, 2)  # move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

# Simple function to extract IP (assuming first field in log)
def extract_ip(line):
    return line.split()[0]

# Placeholder: your existing detection logic
def looks_suspicious(line):
    patterns = ["../", "<script>", "union select", "select .* from"]
    for p in patterns:
        if p in line.lower():
            return True
    return False

# Get reason for alert
def get_reason(line):
    if "../" in line:
        return "Path Traversal"
    elif "<script>" in line.lower():
        return "XSS"
    elif "union select" in line.lower() or "select " in line.lower():
        return "SQLi"
    return "Unknown"

# Main loop
def main():
    blocked_ips = load_blocklist()

    # Block all existing alerts first
    try:
        with open(ALERTS_FILE) as f:
            for line in f:
                alert = json.loads(line)
                ip = alert["ip"]
                reason = alert["type"]
                if add_to_blocklist(ip, reason):
                    block_ip(ip)
    except FileNotFoundError:
        pass

    # Monitor new requests
    for line in tail_log(ACCESS_LOG):
        ip = extract_ip(line)
        if ip in blocked_ips:
            continue  # ignore blocked IP
        if looks_suspicious(line):
            reason = get_reason(line)
            if add_to_blocklist(ip, reason):
                block_ip(ip)
                print(f"[ALERT] {ip} triggered {reason}")

if __name__ == "__main__":
    main()
