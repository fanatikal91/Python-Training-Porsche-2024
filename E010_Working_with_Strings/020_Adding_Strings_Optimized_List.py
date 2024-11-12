import timeit

# Optimized function to concatenate a string n times
def concatenate_string_optimized(n):
    parts = ["a" for _ in range(n)]  # List of 'a' characters
    return "".join(parts)  # Join all parts into a single string

# Values of n for exponential growth
n_values = [10**i for i in range(1, 9)]

first_line = True
# Measure time taken for each n using the optimized method
for n in n_values:
    time_taken = timeit.timeit(lambda: concatenate_string_optimized(n), number=1)
    if first_line:
        print(f"Concatenating {n:9d} times took {time_taken:9.6f} seconds")
        first_line=False
    else:
        print(f"Concatenating {n:9d} times took {time_taken:9.6f} seconds  -->  {(time_taken / old_time_taken):5.2f} times longer")
    old_time_taken = time_taken
