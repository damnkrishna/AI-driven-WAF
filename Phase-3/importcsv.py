import re
import csv
import os

LOG_FILE = "logs/access.log"
CSV_FILE = "output/dataset.csv"
PRETTY_FILE = "output/dataset_pretty.txt"

# Suspicious patterns with attack type labels
SUSPICIOUS_PATTERNS = {
    r"\.\./": "Directory Traversal",
    r"select.+from": "SQL Injection",
    r"union.+select": "SQL Injection",
    r"<script>": "XSS",
    r"\.php\?": "PHP Injection",
    r"/etc/passwd": "Local File Inclusion",
}

# Regex for parsing Apache logs
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\S+)'
)

def parse_log_line(line):
    """Parse one line from access.log"""
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None

def detect_attack(url):
    """Detect attack type based on URL patterns"""
    for pattern, attack_type in SUSPICIOUS_PATTERNS.items():
        if re.search(pattern, url, re.IGNORECASE):
            return attack_type
    return ""

def main():
    if not os.path.exists(LOG_FILE):
        print(f"❌ Log file not found: {LOG_FILE}")
        return

    entries = []

    # Step 1: Parse logs
    with open(LOG_FILE, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                attack_type = detect_attack(parsed["url"])
                label = "malicious" if attack_type else "normal"
                entries.append([
                    parsed["ip"],
                    parsed["time"],
                    parsed["method"],
                    parsed["url"],
                    parsed["status"],
                    parsed["size"],
                    label,
                    attack_type
                ])

    # Step 2: Write CSV
    os.makedirs("output", exist_ok=True)
    headers = ["src_ip", "timestamp", "method", "url", "status", "size", "label", "attack_type"]
    with open(CSV_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(entries)

    # Step 3: Write Pretty File (aligned columns)
    col_widths = [len(h) for h in headers]
    for row in entries:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(col)))

    with open(PRETTY_FILE, "w") as f:
        # Header
        header_row = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        f.write(header_row + "\n")
        f.write("-" * len(header_row) + "\n")

        # Data rows
        for row in entries:
            formatted = "  ".join(str(col).ljust(col_widths[i]) for i, col in enumerate(row))
            f.write(formatted + "\n")

    print(f"✅ Dataset saved as {CSV_FILE}")
    print(f"✅ Pretty formatted dataset saved as {PRETTY_FILE}")

if __name__ == "__main__":
    main()
