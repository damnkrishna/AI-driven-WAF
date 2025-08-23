# Flask Logging Demo App

A simple Flask web app that logs all incoming requests in Apache-style format.  
Useful for testing requests and generating log data.

## 🚀 Setup & Run

1. Save the script as `app.py`.
2. Install Flask:
   ```bash
   pip install flask
    ```

3. Run the app:

   ```bash
   python3 app.py
   ```
4. Access it at:

   ```
   http://127.0.0.1:8080
   ```

## 📌 Endpoints

* `/` → returns **OK**
* `/login.php?user=test` → echoes query params in JSON
* `/search?q=test` → echoes search query in JSON
* `/admin` → returns **403 Forbidden**

## 📂 Logs

All requests are saved in:

```
logs/access.log
```

Example:

```
127.0.0.1 - - [23/Aug/2025:20:25:01 +0530] "GET /search?q=test HTTP/1.1" 200 25 "-" "curl/7.81.0" "-"
```
