import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("300x150")  # Set window size

# Create a label and place it in the first row, first column
label = tk.Label(root, text="Name:")
label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field and place it in the first row, second column
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button and place it in the second row, spanning two columns
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the main event loop
root.mainloop()