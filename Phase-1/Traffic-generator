import random, time, threading, urllib.parse, requests

BASE = "http://localhost:8080"

NORMAL_PATHS = [
    "/", "/search?q=toaster", "/search?q=hairdryer",
    "/login.php?id=2", "/login.php?user=alice"
]

MALICIOUS = [
    "/login.php?id=1' OR '1'='1",
    "/search?q=<script>alert('xss')</script>",
    "/../../etc/passwd",
    "/admin",  # forbidden endpoint
    "/search?q=%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E",
]

UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "curl/8.1.0",
    "sqlmap/1.7",
    "Mozilla/5.0 (compatible; AhrefsBot/6.1)",
    "Mozilla/5.0 (compatible; bingbot/2.0)",
]

def hit(path, ua):
    url = BASE + path
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=3)
        return r.status_code
    except Exception:
        return None

def worker(malicious_ratio=0.3, rps=5):
    while True:
        ua = random.choice(UAS)
        path = random.choice(MALICIOUS if random.random() < malicious_ratio else NORMAL_PATHS)
        # Ensure proper encoding of query if needed
        if " " in path:
            p, *rest = path.split(" ", 1)
            path = p + urllib.parse.quote(" " + rest[0])
        hit(path, ua)
        time.sleep(1.0 / max(1, rps))

if __name__ == "__main__":
    # 3 threads to simulate multiple clients
    for _ in range(3):
        threading.Thread(target=worker, kwargs={"malicious_ratio":0.4, "rps":4}, daemon=True).start()
    while True:
        time.sleep(10)
