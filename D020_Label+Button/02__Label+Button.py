import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Application")
root.geometry("400x300")  # Set window size (width x height)

# Add a simple label
label = tk.Label(root, text="Welcome to my Tkinter application!")
label.pack(pady=20)  # Place the label with some padding on top and bottom

# A button to close the window
close_button = tk.Button(root, text="Schließen", command=root.quit)
close_button.pack(pady=70)

# Add second label
adwise = tk.Label(root, text="Hier kann experimentiert werden" )
adwise.pack(padx=20)

frame = ttk.Frame(root, padding="5 5 5 5", relief="raised", borderwidth=5)
frame.pack(fill="both", expand=False)


# Start the main event loop
root.mainloop()