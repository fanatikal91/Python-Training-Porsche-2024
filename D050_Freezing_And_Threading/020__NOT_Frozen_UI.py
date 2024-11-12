import tkinter as tk
import threading
import time
from tkinter import messagebox

def long_running_task():
    time.sleep(10)  # Simulate a long task
    print("Task completed")


root = tk.Tk()
root.title("Non-Freezing Tkinter UI")

def show_message_box():
    messagebox.showinfo("Message", "Important information!")

def start_task():
    # Run the task in a separate thread
    threading.Thread(target=long_running_task).start()

# Button to start the long-running task
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack(pady=20)

message_button = tk.Button(root, text="Start Task", command=show_message_box)
message_button.pack(pady=20)

root.mainloop()
