import time

# Generate a long string and a substring to search
main_string = "a" * 1000000 + "b"  # Long string ending in a unique 'b' character
substring = "ab"  # Substring we're searching for, near the end

# 1. Naive Search
def naive_search(main, sub):
    for i in range(len(main) - len(sub) + 1):
        if main[i:i+len(sub)] == sub:
            return i
    return -1

# 2. Built-in `in` operator
def builtin_search(main, sub):
    return main.find(sub)

# Measure performance
start_time = time.time()
naive_result = naive_search(main_string, substring)
naive_time = time.time() - start_time
print(f"Naive search took    {naive_time:.6f}  seconds and found at index {naive_result}")

start_time = time.time()
builtin_result = builtin_search(main_string, substring)
builtin_time = time.time() - start_time
print(f"Built-in search took {builtin_time:.6f} seconds and found at index {builtin_result}")
