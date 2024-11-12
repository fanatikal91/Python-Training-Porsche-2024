import tkinter as tk
import random
import time

# Hauptfenster erstellen
root = tk.Tk()
root.title("Messwerte Diagramm")
root.geometry("600x400")

# Canvas erstellen
canvas = tk.Canvas(root, width=580, height=350, bg="white")
canvas.pack(pady=20)

# Achsen zeichnen
canvas.create_line(50, 300, 550, 300, arrow=tk.LAST)  # x-Achse (Zeitachse)
canvas.create_line(50, 300, 50, 50, arrow=tk.LAST)    # y-Achse (Werteachse)

# Beschriftung der Achsen
canvas.create_text(300, 320, text="Zeit")
canvas.create_text(20, 150, text="Werte", angle=90)

# Beispiel-Messwerte generieren
# Messwerte = [(zeitpunkt, wert), ...]
messwerte = [(i, random.randint(50, 250)) for i in range(10)]

# Diagramm zeichnen
def draw_diagram():
    prev_x, prev_y = None, None
    for i, (zeit, wert) in enumerate(messwerte):
        # Koordinaten für das Diagramm berechnen
        x = 50 + (zeit * 50)  # Zeit auf der x-Achse (skalieren)
        y = 300 - wert  # Werte auf der y-Achse (invertieren und skalieren)
        
        # Punkt auf der Achse zeichnen
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="blue")
        
        # Linien zwischen den Punkten zeichnen (falls vorheriger Punkt existiert)
        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, x, y, fill="red", width=2)
        
        # Speichern der aktuellen Koordinaten als vorherige
        prev_x, prev_y = x, y

# Diagramm zeichnen, wenn die Anwendung gestartet wird
draw_diagram()

# Tkinter-Hauptschleife starten
root.mainloop()
