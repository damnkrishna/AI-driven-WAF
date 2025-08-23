import re
import pandas as pd
from tabulate import tabulate  # pip install tabulate

# Regex for Apache Combined Log Format
log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<time>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) (?P<protocol>\S+)" '
    r'(?P<status>\d+) (?P<size>\d+) '
    r'"(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

# Read your access.log file
with open("access.log", "r", encoding="utf-8") as f:
    logs = f.readlines()

data = []
for line in logs:
    match = log_pattern.match(line)
    if match:
        data.append(match.groupdict())

# Convert to DataFrame
df = pd.DataFrame(data)

# Print clean readable table
print("\n📊 Parsed Access Logs:\n")
print(tabulate(df.head(20), headers="keys", tablefmt="fancy_grid", showindex=False))  # show first 20 rows

# Save to CSV for analysis
df.to_csv("cleaned_access_logs.csv", index=False)

# Save to TXT with pretty table
with open("cleaned_access_logs.txt", "w", encoding="utf-8") as f:
    f.write(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

print("\n✅ Logs cleaned and saved as cleaned_access_logs.csv & cleaned_access_logs.txt")
