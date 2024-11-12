import tkinter as tk

# Function to handle the button click
def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Hello {name}.")  # Update the greeting text
    greeting_label.grid(row=3, column=0, columnspan=2, pady=10)  # Show the greeting text

# Function to enable/disable the button and hide the greeting text
def on_entry_change(*args):
    # Enable button only if there is text in the entry
    if name_var.get():
        greet_button.config(state="normal")
    else:
        greet_button.config(state="disabled")
    # Hide the greeting text when entry is modified
    greeting_label.grid_remove()

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x150")  # Set window size

# Variable to hold the entry text
name_var = tk.StringVar()
name_var.trace_add("write", on_entry_change)  # Track changes to the entry

# Label for name prompt
name_label = tk.Label(root, text="Enter your Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Entry field for name input
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Greet button
greet_button = tk.Button(root, text="Greet me", command=greet, state="disabled")
greet_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label for the greeting message
greeting_label = tk.Label(root, text="", font=("Arial", 10))
greeting_label.grid(row=3, column=0, columnspan=2, pady=10)
greeting_label.grid_remove()  # Hide the greeting label initially

# Start the main event loop
root.mainloop()