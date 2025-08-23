import re
import time
from collections import defaultdict, deque

LOG_FILE = "logs/access.log"

# Regex patterns for detecting common web attacks
patterns = {
    "SQLi": re.compile(r"(\%27)|(\')|(\-\-)|(\%3D)|(=)"),
    "XSS": re.compile(r"(<script>|%3Cscript|onerror|%3Cimg)"),
    "Traversal": re.compile(r"\.\./"),
    "Admin Scan": re.compile(r"/admin|/login\.php.*id="),
}

# Store request history for brute force detection
request_history = defaultdict(lambda: deque())

# Thresholds
MAX_REQUESTS = 50
TIME_WINDOW = 20  # seconds

def detect_attack(line: str):
    """Check for malicious patterns inside a log line"""
    for attack_type, pattern in patterns.items():
        if pattern.search(line):
            return attack_type
    return None

def extract_ip(line: str) -> str:
    """Extract the IP from a log line (assuming common access.log format)"""
    parts = line.split()
    return parts[0] if parts else "UNKNOWN"

def brute_force_check(ip: str, timestamp: float):
    """Check if an IP is making too many requests in a short time"""
    requests = request_history[ip]
    requests.append(timestamp)

    # Remove old requests outside time window
    while requests and timestamp - requests[0] > TIME_WINDOW:
        requests.popleft()

    if len(requests) > MAX_REQUESTS:
        return True
    return False

def tail_f(filename):
    """Tail a log file like `tail -f`"""
    with open(filename, "r") as f:
        f.seek(0, 2)  # move to end
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

if __name__ == "__main__":
    print("[*] Real-time WAF Analyzer started...")
    for log_line in tail_f(LOG_FILE):
        ip = extract_ip(log_line)
        now = time.time()

        # Attack pattern detection
        attack = detect_attack(log_line)
        if attack:
            print(f"[ALERT] {attack} detected from {ip} → {log_line}")

        # Brute force detection
        if brute_force_check(ip, now):
            print(f"[ALERT] Possible brute force from {ip} (>{MAX_REQUESTS} reqs/{TIME_WINDOW}s)")
