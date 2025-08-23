import re
from collections import Counter

# Input and Output paths
LOG_FILE = "sample_data/access.log"
REPORT_FILE = "output/report.txt"

# Suspicious patterns to flag
SUSPICIOUS_PATTERNS = [
    r"\.\./",              # directory traversal
    r"select.+from",       # SQL injection
    r"union.+select",      # SQL injection
    r"<script>",           # XSS
    r"\.php",              # suspicious PHP access
    r"/etc/passwd",        # passwd file
]

def parse_logs():
    ip_counter = Counter()
    status_counter = Counter()
    suspicious_requests = []

    with open(LOG_FILE, "r", errors="ignore") as f:
        for line in f:
            # Example log line contains: IP - - [date] "METHOD URL HTTP/1.1" status size
            parts = line.split()
            if len(parts) < 9:
                continue

            ip = parts[0]
            method = parts[5].strip('"')
            url = parts[6]
            status = parts[8]

            ip_counter[ip] += 1
            status_counter[status] += 1

            for pattern in SUSPICIOUS_PATTERNS:
                if re.search(pattern, url, re.IGNORECASE):
                    suspicious_requests.append(line.strip())
                    break

    return ip_counter, status_counter, suspicious_requests

def generate_report():
    ip_counter, status_counter, suspicious = parse_logs()

    with open(REPORT_FILE, "w") as f:
        f.write("=== Web Log Analysis Report ===\n\n")
        f.write(f"Total unique IPs: {len(ip_counter)}\n")
        f.write("Top 5 IPs:\n")
        for ip, count in ip_counter.most_common(5):
            f.write(f"  {ip}: {count} requests\n")

        f.write("\nStatus Codes:\n")
        for status, count in status_counter.items():
            f.write(f"  {status}: {count}\n")

        f.write(f"\nSuspicious Requests Detected: {len(suspicious)}\n")
        for req in suspicious[:10]:  # only show first 10
            f.write(f"  {req}\n")

    print(f"✅ Report generated: {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()
