import tkinter as tk
import threading
import time

def long_running_task(status, counter):
    for i in range(1,11):
        time.sleep(1)  # Simulate a long task
        root.after(0, update_counter, counter, i)

    result = "Task Completed"
    
    # Schedule an update to the UI
    root.after(0, update_ui, status, result)
    root.after(2000, update_counter, counter, -1)
    root.after(2000, update_ui, status, "Click 'Start Task' to begin")

def update_ui(var, result):
    var.set(result)

def update_counter(var, count):
    if count == -1:
        var.set(" ")
    else:
        var.set("Counter: " + str(count))
        

def start_task():
    # Start a new thread with the long-running task
    threading.Thread(target=long_running_task, args=(status_var,count_secs_var)).start()

root = tk.Tk()
root.title("Non-Freezing Tkinter UI")

# Variable to store status
status_var = tk.StringVar(value="Click 'Start Task' to begin")

count_secs_var = tk.StringVar(value=" ")

# Label to display task status
status_label = tk.Label(root, textvariable=status_var)
status_label.pack(pady=10)

count_secs_label = tk.Label(root, textvariable=count_secs_var)
count_secs_label.pack(pady=10)

# Button to start the long-running task
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack(pady=20)

root.mainloop()
