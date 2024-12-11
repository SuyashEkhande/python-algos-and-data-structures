import cProfile

def slow_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

def fast_function():
    return sum(range(1, 1000000))

def main():
    slow_function()
    fast_function()

# Profiling the main function
cProfile.run('main()')
