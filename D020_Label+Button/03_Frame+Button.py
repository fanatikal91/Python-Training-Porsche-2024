import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("ttk.Frame Example")
root.geometry("400x300")  # Set window size (width x height)

# Create a ttk.Frame with padding and a border
frame = ttk.Frame(root, padding="10 10 20 50", relief="raised", borderwidth=15)
frame.pack(fill="both", expand=True)

# Add a label and button to the frame
label = ttk.Label(frame, text="Hello, ttk.Frame!")
label.pack(pady=10)

close_button = tk.Button(frame, text="Schließen", command=root.quit)
close_button.pack(pady=10)

phone = tk.StringVar()
home = tk.Radiobutton(frame, text='Home', variable=phone, value='home')
home.select()
home.pack()
office = tk.Radiobutton(frame, text='Office', variable=phone, value='office').pack()
cell = tk.Radiobutton(frame, text='Mobile', variable=phone, value='cell').pack()

button = ttk.Button(frame, text="Arbeitsweise auswählen")
button.pack(pady=5)

# Run the application
root.mainloop()
