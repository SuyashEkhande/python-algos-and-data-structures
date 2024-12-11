import timeit

# Code to measure execution time
def test_code():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

# Using timeit to measure execution time
"""
timeit.timeit(): Measures how long the test_code function takes to execute.
globals=globals(): This allows you to pass the test_code function to timeit 
                   in the current global scope.
number=10: Executes the code 10 times to get an average execution time.
"""
execution_time = timeit.timeit('test_code()', globals=globals(), number=10)
print(f'Execution time: {execution_time:.6f} seconds')
