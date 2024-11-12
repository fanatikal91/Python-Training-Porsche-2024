import numpy as np
import time

# Array-Dimensionen
rows, cols = 1000, 1000

# Erstelle ein 2D-Array mit zufälligen Gleitkommazahlen
array = np.random.rand(rows, cols)

# Total number of replacements to be done
total_replacements = rows * cols

# Liste zur Speicherung der Ersetzungszeiten
replacement_times = []

# Iteriere über Ersetzungen in Schritten von 10000
for i in range(10000, total_replacements + 1, 10000):
    start_time = time.time()
    
    # Ersetze die ersten i Elemente im Array (linearer Zugriff)
    array.flat[:i] = np.random.rand(i)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    replacement_times.append(elapsed_time)
    print(f"Replacing {i} elements took {elapsed_time:.6f} seconds")
