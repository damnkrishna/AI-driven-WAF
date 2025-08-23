from flask import Flask, request, jsonify
import logging, os, time

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)

class CombinedLogFormatter(logging.Formatter):
    def format(self, record):
        # Fields we want to log
        ip = request.headers.get("X-Forwarded-For", request.remote_addr or "-")
        user_ident = "-"
        user_auth = "-"
        time_local = time.strftime("%d/%b/%Y:%H:%M:%S %z")
        method = request.method
        path = request.full_path[:-1] if request.full_path.endswith('?') else request.full_path
        proto = request.environ.get("SERVER_PROTOCOL", "HTTP/1.1")
        status = record.status if hasattr(record, "status") else 200
        size = record.size if hasattr(record, "size") else "-"
        referer = request.headers.get("Referer", "-")
        ua = request.headers.get("User-Agent", "-")

        return f'{ip} {user_ident} {user_auth} [{time_local}] "{method} {path} {proto}" {status} {size} "{referer}" "{ua}" "-"'

# Access logger
access_logger = logging.getLogger("access")
access_logger.setLevel(logging.INFO)
fh = logging.FileHandler("logs/access.log", encoding="utf-8")
fh.setFormatter(CombinedLogFormatter())
access_logger.addHandler(fh)

@app.after_request
def after(resp):
    rec = logging.LogRecord("access", logging.INFO, "", 0, "", (), None)
    rec.status = resp.status_code
    rec.size = resp.calculate_content_length() or 0
    access_logger.handle(rec)
    return resp

@app.route("/")
def home():
    return "OK"

@app.route("/login.php")
def login():
    # echo back params (just for variety)
    return jsonify({"msg": "login", "args": request.args})

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return jsonify({"results": [], "q": q})

@app.route("/admin")
def admin():
    return ("forbidden", 403)

if __name__ == "__main__":
    app.run(port=8080, debug=False)
