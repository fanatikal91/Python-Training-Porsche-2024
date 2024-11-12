import random
import time

# QuickSort function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Array sizes to test
sizes = list(range(0, 100001, 10000))

# Perform QuickSort on arrays of increasing size and time each run
for size in sizes:
    # Generate an array with `size` random integers
    array = [random.randint(0, 1000000) for _ in range(size)]
    
    # Time the QuickSort
    start_time = time.time()
    sorted_array = quicksort(array)
    end_time = time.time()
    
    # Calculate and print the time taken
    elapsed_time = end_time - start_time
    print(f"QuickSort took {elapsed_time:.6f} seconds to sort {size} elements.")
