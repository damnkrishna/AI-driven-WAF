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
<img width="466" height="298" alt="image" src="https://github.com/user-attachments/assets/b2af0a3f-0b1e-4fa0-addb-c31ea1a35ed1" />



NOTE:
-remeber to run this script in one terminal 
-also remeber to start this from starting in a virtual environment to keep the python and other stuff isolated from whole system 
