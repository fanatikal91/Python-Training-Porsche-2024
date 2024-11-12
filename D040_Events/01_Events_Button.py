import tkinter as tk
from tkinter import messagebox

# Function to show the message box
def on_button_click():
    messagebox.showinfo("Message", "Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Click Example")
root.geometry("200x100")  # Set window size

# Create the button and place it in the center
click_button = tk.Button(root, text="Click me", command=on_button_click)
click_button.pack(pady=30)  # Center the button with padding

# Start the main event loop
root.mainloop()