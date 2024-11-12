import tkinter as tk
from tkinter import messagebox

# Function to show the checkbox status
def on_checkbox_toggle():
    # checkbox.config(text="EMPTY")
    if checkbox_var.get():
        messagebox.showinfo("Checkbox Status", "The checkbox is checked!")
    else:
        messagebox.showinfo("Checkbox Status", "The checkbox is unchecked!")

# Create the main window
root = tk.Tk()
root.title("Checkbox Example")
root.geometry("200x100")  # Set window size

# Variable to store the checkbox state
checkbox_var = tk.BooleanVar()

# Create the checkbox and link it to the variable
checkbox = tk.Checkbutton(root, text="Check me", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack(pady=20)  # Center the checkbox with padding

# Start the main event loop
root.mainloop()