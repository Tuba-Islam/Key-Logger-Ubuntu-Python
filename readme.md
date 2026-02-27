

# 📌 CyberSecurity – Keylogger Simulation

## 📖 Project Overview

This project simulates a **basic keylogger in a controlled and authorized environment** to demonstrate how keystroke logging attacks work and the associated cybersecurity risks.

⚠ **Important:**
This project is strictly for educational purposes and must only be executed on systems where you have explicit authorization.

---

# 🎯 Objectives

* Understand how keystroke logging works technically.
* Capture system-wide keystrokes in a controlled environment.
* Store logs in structured format (JSON).
* Demonstrate encryption of captured logs.
* Perform basic log analysis.
* Analyze security risks associated with keylogging attacks.

---

# 🛠 Technologies Used

* **Python 3**
* `pynput` (keyboard event capturing)
* `cryptography` (log encryption)
* `json` (structured logging)
* `signal` (safe termination handling)
* `collections` (frequency analysis)

---

# 🖥 Environment

* OS: Ubuntu Linux
* Course: CyberSecurity
* Execution Mode: Authorized lab testing only

---

# 📦 Installation

## 1️⃣ Install Dependencies

```bash
sudo apt update
pip3 install pynput cryptography
```

---

# ▶ Running the Program

```bash
sudo python3 keylogger.py
```

> `sudo` is required to capture system-wide keystrokes on Ubuntu.

---

# ⏹ Stopping the Program

Press:

```
CTRL + C
```

This will:

* Save logs to JSON file
* Encrypt the log file
* Perform automatic analysis
* Exit safely

---

# 📁 Output Files

After stopping the program:

| File                      | Description                       |
| ------------------------- | --------------------------------- |
| `keystroke_log.json`      | Structured readable keystroke log |
| `keystroke_log.encrypted` | Encrypted version of log          |

---

# 📂 Log Format (JSON Structure)

Example:

```json
[
    {
        "timestamp": "2026-03-01 10:21:44",
        "key": "a"
    },
    {
        "timestamp": "2026-03-01 10:21:45",
        "key": "[ENTER]"
    }
]
```

---

# 🔍 Features Demonstration Guide (For Professor Testing)

## ✅ Feature 1: Real-Time Keystroke Capture

* Run the program
* Type in terminal or browser
* Observe printed keystrokes with timestamps

---

## ✅ Feature 2: Special Key Detection

Test:

* ENTER
* SHIFT
* CTRL
* BACKSPACE
* TAB

They will appear as:

```
[ENTER]
[SHIFT]
[CTRL]
```

---

## ✅ Feature 3: Structured Logging

After stopping:

```bash
cat keystroke_log.json
```

Shows organized timestamped entries.

---

## ✅ Feature 4: Log Encryption

Verify encrypted file:

```bash
cat keystroke_log.encrypted
```

It will appear unreadable (encrypted binary).

---

## ✅ Feature 5: Log Analysis

When program stops, it automatically:

* Displays most frequent keys
* Detects numeric sequences (possible password patterns)
* Shows statistical summary

---

# 🧠 Concepts Applied

## 1️⃣ Event-Driven Programming

Uses keyboard listener callbacks:

```python
on_press(key)
```

---

## 2️⃣ System-Wide Input Hooking

The program uses `pynput` to register a low-level keyboard listener.

Concept: Input event interception.

---

## 3️⃣ Structured Data Logging

Logs stored in JSON format:

* Easy parsing
* Readable
* Forensic-friendly

---

## 4️⃣ Signal Handling

Uses:

```python
signal.signal(signal.SIGINT, signal_handler)
```

Ensures:

* Safe termination
* No data loss

---

## 5️⃣ Cryptographic Protection

Uses:

```python
Fernet (symmetric encryption)
```

Concept demonstrated:

* Attackers may encrypt stolen logs to evade detection.
* Defensive side: encrypted data storage for secure logging.

---

## 6️⃣ Frequency Analysis

Uses:

```python
collections.Counter
```

Demonstrates:

* Behavioral analysis
* Pattern recognition
* Password guessing potential

---

# ⚠ Security Risks Demonstrated

Keyloggers can lead to:

* Credential theft
* Banking fraud
* Identity theft
* Corporate espionage
* Capture of OTP / 2FA codes
* Privacy invasion

---

# 🛡 Defensive Countermeasures

To protect against keyloggers:

* Anti-malware software
* Endpoint Detection & Response (EDR)
* OS permission restrictions
* Two-factor authentication (2FA)
* Encrypted input fields
* Behavioral monitoring systems

---

# 🧪 Testing Scenario for Evaluation

Professor can test by:

1. Running the script
2. Typing:

   * A sample password (e.g., 123456)
   * Random text
3. Stopping program
4. Observing:

   * JSON log file
   * Encrypted file
   * Analysis output

---

# 📚 Academic Learning Outcomes

After completing this project, students understand:

* How keyloggers technically operate
* Why they are dangerous
* How logs are structured and analyzed
* How encryption can be used offensively or defensively
* Importance of cybersecurity countermeasures

---

# ⚖ Legal & Ethical Notice

This software is developed strictly for:

* Educational use
* Controlled lab environments
* Authorized systems only

Unauthorized deployment may violate cybersecurity laws and privacy regulations.

---

# 👩‍💻 Author: Tuba Islam

Semester Project – CyberSecurity Lab
Python Implementation on Ubuntu

---

---
