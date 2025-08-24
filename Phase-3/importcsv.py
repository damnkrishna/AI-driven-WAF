import re
import csv

ACCESS_LOG = "logs/access.log"
OUTPUT_FILE = "dataset.csv"

# Regex for parsing standard access.log lines
log_pattern = re.compile(
    r'(?P<src_ip>\d+\.\d+\.\d+\.\d+).*?'
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>GET|POST) (?P<url>.*?) HTTP/1.[01]" '
    r'(?P<status>\d+) (?P<bytes>\d+) '
    r'"(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
)

# Malicious patterns
patterns = {
    "sqli": re.compile(r"(\%27)|(\')|(\-\-)|(\%23)|(#)|union.*select|select.*from|insert.*into", re.IGNORECASE),
    "xss": re.compile(r"(<script>|%3Cscript|onerror|alert\()", re.IGNORECASE),
    "traversal": re.compile(r"(\.\./|\.\.\\)", re.IGNORECASE),
    "cmd_injection": re.compile(r"(;|\|\||&&|wget|curl)", re.IGNORECASE),
}

def is_malicious(url):
    for name, regex in patterns.items():
        if regex.search(url):
            return True
    return False

with open(ACCESS_LOG, "r") as infile, open(OUTPUT_FILE, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["src_ip","timestamp","method","url","status","bytes","user_agent","label"])

    for line in infile:
        match = log_pattern.search(line)
        if match:
            data = match.groupdict()
            label = "malicious" if is_malicious(data["url"]) else "normal"
            writer.writerow([
                data["src_ip"], data["timestamp"], data["method"], data["url"],
                data["status"], data["bytes"], data["user_agent"], label
            ])

print(f"✅ Clean dataset created: {OUTPUT_FILE}")
