# Simple Keylogger Program

A lightweight Python keylogger program that records and logs keystrokes to a local text file. This project is built for educational, authorized security testing, and research purposes.

---

## ⚠️ Ethical & Legal Disclaimer
> [!WARNING]
> **Monitoring keystrokes without explicit, written consent from the device owner is illegal and unethical.** This software is developed solely for educational instruction, authorized security audits, and personal research. Use this program responsibly and only on machines you own or have explicit authorization to monitor.

---

## ✨ Features
- **Key Logging**: Captures alphabetic, numeric, and special keys.
- **Readable Log Format**: Special keys like Space, Enter, and Tab are formatted cleanly instead of raw code representations.
- **Inactivity Session Detection**: Automatically starts a new line with a timestamp (e.g., `[2026-08-23 19:54:12]`) if typing is paused for more than 5 seconds.
- **Clean Control Key Representation**: Intercepts and translates shortcuts like `Ctrl+C` or `Ctrl+V` into human-readable strings like `[CTRL+C]`.
- **Session Boundaries**: Logs when a session starts, stops, or is interrupted by a user.
- **Graceful Termination**: Stop monitoring instantly by pressing the `Escape` key.

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
Ensure you have Python installed on your system.

### 2. Dependencies
Install the required keyboard listening library using `pip`:
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Open your terminal in the project directory.
2. Execute the script:
   ```bash
   python keylogger.py
   ```
3. Type in any application. Your keystrokes will be captured and written to `key_log.txt` in the same directory.
4. Press **Escape** (`Esc`) to cleanly exit the logger.
