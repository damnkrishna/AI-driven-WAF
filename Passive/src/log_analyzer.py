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

    report_lines = []
    report_lines.append("=== Web Log Analysis Report ===\n")

    # Total unique IPs
    report_lines.append(f"📊 Total Unique IPs: {len(ip_counter)}\n")

    # Top 5 IPs
    report_lines.append("🔝 Top 5 IPs")
    report_lines.append("-" * 40)
    report_lines.append(f"{'IP Address':<20} {'Requests':>10}")
    for ip, count in ip_counter.most_common(5):
        report_lines.append(f"{ip:<20} {count:>10}")
    report_lines.append("")

    # Status codes
    report_lines.append("📈 Status Codes")
    report_lines.append("-" * 40)
    report_lines.append(f"{'Status':<10} {'Count':>10}")
    for status, count in status_counter.most_common():
        report_lines.append(f"{status:<10} {count:>10}")
    report_lines.append("")

    # Suspicious requests
    report_lines.append(f"⚠️  Suspicious Requests Detected: {len(suspicious)}")
    report_lines.append("-" * 40)
    for req in suspicious[:10]:  # Show only first 10 for brevity
        report_lines.append(req)
    if len(suspicious) > 10:
        report_lines.append(f"...and {len(suspicious)-10} more\n")

    # Write to file
    with open("output/report.txt", "w") as f:
        f.write("\n".join(report_lines))

    print("✅ Report generated: output/report.txt")


if __name__ == "__main__":
    generate_report()
