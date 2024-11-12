import random
import time

# Bubble sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, array is already sorted
        if not swapped:
            break

# Array sizes to test
sizes = list(range(0, 30001, 10000))

# Perform bubble sort on arrays of increasing size and time each run
for size in sizes:
    # Generate an array with `size` random integers
    array = [random.randint(0, 1000000) for _ in range(size)]
    
    # Time the bubble sort
    start_time = time.time()
    bubble_sort(array)
    end_time = time.time()
    
    # Calculate and print the time taken
    elapsed_time = end_time - start_time
    print(f"Bubble sort took {elapsed_time:.6f} seconds to sort {size} elements.")
