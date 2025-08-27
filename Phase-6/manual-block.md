# 🛡️ Phase 6 — Manual IP Blocking (iptables)

## 📌 Overview

This module demonstrates how to **block malicious IPs manually** using Linux `iptables`.
Blocked IPs are **prevented from sending any packets** (HTTP requests, ping, etc.) to your server.

This is a **precursor to automating blocking** in your WAF project.

---

## 🔧 Prerequisites

* Linux system with `iptables` installed
* `sudo` privileges
* Caution: **Do not block your own IP**, especially if using SSH

---

## 📋 Step 1 — Check Current Firewall Rules

```bash
sudo iptables -L INPUT -n --line-numbers
```

* Shows all current rules in the **INPUT chain**
* `num` → rule number
* `target` → action (ACCEPT/DROP)
* `source` → source IP

---

## 📌 Step 2 — Add an IP to Blocklist

Example: block `192.168.1.10`

```bash
sudo iptables -I INPUT 1 -s 192.168.1.10 -j DROP
```

* `-I INPUT 1` → inserts at the top of INPUT chain
* `-s <IP>` → source IP to block
* `-j DROP` → drop all packets from this IP

### ✅ Verify it’s blocked

```bash
sudo iptables -L INPUT -n --line-numbers
```

* You should see the new DROP rule at the top
* Any requests from this IP are now silently discarded

---

## 📌 Step 3 — Remove an IP from Blocklist

Example: unblock `192.168.1.10`

```bash
sudo iptables -D INPUT -s 192.168.1.10 -j DROP
```

### ✅ Verify it’s removed

```bash
sudo iptables -L INPUT -n --line-numbers
```

* The IP should no longer appear in the list
* Requests from this IP will now be accepted normally

---

## 📌 Step 4 — Optional: Make Rules Persistent

```bash
sudo apt-get install -y iptables-persistent
sudo netfilter-persistent save
```

* Ensures your blocked IPs stay blocked **even after a system reboot**

## ⚠️ Notes & Tips

* Only block **attacker IPs**; avoid your own machine IP
* Always check logs first to confirm malicious activity
* This manual method is safe for learning before automating blocking in Phase 6 of your WAF project


