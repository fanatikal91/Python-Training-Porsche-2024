import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Application")
root.geometry("300x200")  # Set window size (width x height)

# Add a simple label
label = tk.Label(root, text="Welcome to my Tkinter application!")
label.pack(pady=200)  # Place the label with some padding on top and bottom

# Start the main event loop
root.mainloop()