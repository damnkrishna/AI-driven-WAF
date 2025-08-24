# 🛡️ Phase 6 — Real-Time IP Blocking (Linux, iptables)

## 📌 Overview

This module extends the Phase 2 WAF analyzer to **automatically block malicious IPs** in real time.

* Uses `alerts.jsonl` to block known malicious IPs.
* Monitors `access.log` for new suspicious activity.
* Maintains a `blocklist.jsonl` to track blocked IPs.
* Uses **iptables** to drop traffic from malicious IPs.

---

## 🔧 Prerequisites

1. Linux system with `iptables` installed
2. `sudo` privileges
3. Phase 2 WAF analyzer running with `alerts.jsonl` and `access.log`
4. Optional: `out/` folder for storing `blocklist.jsonl`

```bash
mkdir -p out
touch out/blocklist.jsonl
```

---

## 📋 Step 1 — Understand Manual Blocking

Practice blocking a test IP manually before automating:

```bash
# Block IP
sudo iptables -I INPUT 1 -s <IP_ADDRESS> -j DROP

# Verify
sudo iptables -L INPUT -n --line-numbers

# Unblock IP
sudo iptables -D INPUT -s <IP_ADDRESS> -j DROP
```

⚠️ **Warning:** Do not block your own IP (especially if using SSH).

---

## 📋 Step 2 — Maintain a Blocklist

* `blocklist.jsonl` stores blocked IPs with timestamp and reason:

```json
{"ip": "192.168.1.10", "reason": "SQLi", "time": "2025-08-24 15:30:22"}
```

* Keeps track of which IPs are already blocked
* Ensures persistence across script restarts

---

## 📋 Step 3 — Block Existing Alerts

* Read `alerts.jsonl` on startup
* For each malicious IP, check if it’s already in blocklist
* If not, add to `blocklist.jsonl` and block via iptables

---

## 📋 Step 4 — Real-Time Monitoring

* Tail `access.log` in real time

* For each new request:

  1. Extract IP
  2. If IP is in blocklist → ignore/drop request
  3. If log matches suspicious patterns →

     * Raise alert
     * Add IP to `blocklist.jsonl`
     * Block it via iptables immediately

* Example suspicious patterns:

  * SQL Injection (`select ... from`, `union select`)
  * Cross-Site Scripting (`<script>`)
  * Path Traversal (`../`)

---

## 📋 Step 5 — Verify Blocked IPs

```bash
sudo iptables -L INPUT -n --line-numbers
```

* Check that malicious IPs are listed and are dropped
* Test by sending requests from blocked IPs → requests should fail

---

## 📋 Step 6 — Unblocking IPs

To remove an IP from the firewall manually:

```bash
sudo iptables -D INPUT -s <IP_ADDRESS> -j DROP
```

* Optionally remove from `blocklist.jsonl` if you want it to be tracked as unblocked

---

## 📋 Step 7 — Persistence

* By default, iptables rules are **temporary** and reset on reboot
* To make persistent (Debian/Ubuntu):

```bash
sudo apt-get install -y iptables-persistent
sudo netfilter-persistent save
```

* On other distros, save rules with:

```bash
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

---

## 📋 Step 8 — Testing & Safety

1. Start your mini web server + traffic generator
2. Confirm existing malicious IPs from `alerts.jsonl` are blocked
3. Generate new suspicious requests → they should get blocked in real time
4. Normal traffic should pass normally
5. Always test on **non-critical IPs first**

---

## 📋 Step 9 — Future Enhancements

* Add **auto-unblock** after a set time
* Include **GeoIP info** in alerts
* Build a **dashboard** for live blocked IPs and reasons
* Later, integrate ML predictions for early blocking (Phase 5)

---
