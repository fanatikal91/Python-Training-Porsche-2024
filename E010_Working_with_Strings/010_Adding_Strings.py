import timeit

# Function to concatenate a string n times
def concatenate_string(n):
    s = ""
    for _ in range(n):
        s += "a"  # Concatenation of a single character each time
    return s

# Run the test for exponentially increasing values of n
for i in range(1, 9):
    n = 10**i
    time_taken = timeit.timeit(lambda: concatenate_string(n), number=1)
    if i == 1:
        print(f"Concatenating {n:9d} times took {time_taken:9.6f} seconds")
    else:
        print(f"Concatenating {n:9d} times took {time_taken:9.6f} seconds  -->  {(time_taken / old_time_taken):5.2f} times longer")
    old_time_taken = time_taken
