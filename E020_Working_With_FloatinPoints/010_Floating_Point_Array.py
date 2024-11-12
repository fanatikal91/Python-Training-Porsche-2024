import random
import time

# Array-Dimensionen
rows, cols = 1000, 1000

# Erstelle das 2D-Array mit zufälligen Gleitkommazahlen
array = [[random.random() for _ in range(cols)] for _ in range(rows)]

# Total number of replacements to be done
total_replacements = rows * cols

# Liste zur Speicherung der Ersetzungszeiten
replacement_times = []

# Iteriere über Ersetzungen in Schritten von 10000
for i in range(10000, total_replacements + 1, 10000):
    start_time = time.time()
    
    # Ersetze die ersten i Elemente im 2D-Array
    count = 0
    for row in range(rows):
        for col in range(cols):
            if count < i:
                array[row][col] = random.random()  # Neuen zufälligen Wert einsetzen
                count += 1
            else:
                break
        if count >= i:
            break
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    replacement_times.append(elapsed_time)
    print(f"Replacing {i} elements took {elapsed_time:.6f} seconds")
