# IP Tracker V.3

CLI tool for fast IP intelligence lookup with Discord webhook logging.

Clean. Simple. Efficient.

---

## Features

* IP geolocation lookup via **ip-api.com**
* Discord webhook integration (embeds)
* Local history logging
* Google Maps auto-link
* Cross-platform (Windows / Linux / macOS)
* Minimal CLI, no noise

---

## Requirements

* Python **3.9+**
* Internet access

### Python dependencies

```bash
pip install requests colorama
```

---

## Setup

### 1. Clone

```bash
git clone https://github.com/Taro002/orbit-ip-tracker.git
cd orbit-ip-tracker
```

### 2. Discord Webhook (recommended)

Set your webhook as an environment variable:

**Windows (PowerShell)**

```powershell
setx DISCORD_WEBHOOK_URL "https://discord.com/api/webhooks/..."
```

**Linux / macOS**

```bash
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
```

> No webhook = no Discord logging. Tool still works.

---

## Usage

```bash
python main.py
```

### Menu

```
[1] Lookup IP
[2] History
[0] Exit
```

### Output

* Country
* Region
* City
* ZIP
* Latitude / Longitude
* ISP
* Google Maps link

---

## Files

* `main.py` → application logic
* `history.txt` → local lookup history (auto-generated)
* `README.md` → documentation

---

## Notes

* Accuracy depends on **ip-api.com**
* VPN / Proxy IPs may return limited data
* No rate-limit handling (intentional minimalism)

---

## Disclaimer

This tool is for **educational and informational purposes only**.

You are responsible for how you use it.

---

## 📄 License

Copyright © 2025 Taro

Free for personal and educational use.

You are free to modify, improve, and redistribute this project.


<img width="921" height="375" alt="image" src="https://github.com/user-attachments/assets/b95df703-9aea-4b07-9a0c-06636ae88a55" />

