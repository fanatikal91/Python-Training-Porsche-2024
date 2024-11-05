import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("300x500")  # Set window size

# Create a label and place it in the first row, first column
label = tk.Label(root, text="Name:")
label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field and place it in the first row, second column
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Treeview-Widget (Tabelle) erstellen und in Grid platzieren
tree = ttk.Treeview(root, columns=("entry"), show="headings", height=8)
tree.heading("entry", text="Eingabe")
tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Funktion zum Hinzufügen eines neuen Eintrags zur Tabelle
def submit_entry():
    # Text aus dem Entry-Feld holen
    entry_text = entry.get()
    if entry_text:  # Überprüfen, ob das Entry-Feld nicht leer ist
        tree.insert("", "end", values=(entry_text,))  # Zeile zur Tabelle hinzufügen
        entry.delete(0, tk.END)  # Entry-Feld nach Einfügen leeren

# Create a button and place it in the second row, spanning two columns
submit_button = tk.Button(root, text="Submit", command=submit_entry)
submit_button.grid(row=1, column=0, columnspan=2, pady=20)


# Start the main event loop
root.mainloop()