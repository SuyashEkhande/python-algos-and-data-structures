from functools import lru_cache

"""
For functions that are repeatedly called with the same arguments 
(e.g., recursive functions), consider using the functools.lru_cache decorator 
to cache results and avoid redundant calculations.

The lru_cache stores the results of previous calls, 
making future calls with the same arguments faster.
"""

@lru_cache(maxsize=None)  # Cache results of the function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(10))