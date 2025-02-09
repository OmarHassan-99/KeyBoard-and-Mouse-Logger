# **Key and Mouse Logger (KeyMouseTracker)**  

## **Description**  
KeyMouseTracker is a Python-based keylogger and mouse activity tracker that records keystrokes and mouse interactions with timestamps. The program runs in the background using threading, efficiently logging both keyboard and mouse events concurrently. It writes logs to separate text files for easy analysis.

---

## **Features**  
- Logs all keystrokes with timestamps, including special keys like Enter and Backspace.  
- Records mouse movements, clicks, and scroll events.  
- Writes keyboard logs to `AllLoggedKeys.txt` and `ActualDisplay.txt`.  
- Stores mouse logs in `Mouse_Logs.txt`.  
- Excludes non-relevant keys from being recorded for cleaner logs.  
- Timestamped logs for accurate activity tracking.  
- Multi-threaded implementation to handle keyboard and mouse events simultaneously.

---

## **Files Generated**
1. `AllLoggedKeys.txt`: Complete logs of all keystrokes with timestamps.  
2. `ActualDisplay.txt`: Cleaner logs showing a display-like representation of the typed text.  
3. `Mouse_Logs.txt`: Logs mouse movements, clicks, and scroll events.

---

## **How to Use**  
### **1. Prerequisites**
- Python 3.x installed on your system.
- Install the required dependency by running:
  ```bash
  pip install pynput

### **2. Running the Program**  
#### **On Linux/macOS**  
- Open a terminal and run:
  ```bash
  python3 key_mouse_logger.py
#### **On Windows**  
- Open a command prompt or Powershell and run:
  ```bash
  python key_mouse_logger.py
  
### **3.Stopping the Program**  
Press the Escape (Esc) key to gracefully stop the program and save the logs.

## **Implementation Details**  
- **Keyboard Event Handling:**  
  - Detects and logs key presses and releases.  
  - Special handling for keys like Space, Enter, and Backspace.  
  - Excludes system keys like Ctrl, Alt, and function keys for cleaner logs.  

- **Mouse Event Handling:**  
  - Logs mouse movements, button clicks, and scrolling with timestamps.  

- **Multi-threading:**  
  - Keyboard and mouse listeners run concurrently using Python's threading module.

## **Security and Ethical Disclaimer**  
This program is intended solely for educational and ethical purposes. Unauthorized use of keyloggers is illegal and violates privacy laws. Ensure you have the necessary permissions before using this tool. The author does not condone or support any malicious usage of this program.

