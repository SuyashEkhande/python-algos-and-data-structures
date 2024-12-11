# Advanced Decorator Use Cases

# Chaining decorators: Applying multiple decorators on a single function
# `uppercase` converts the function's result to uppercase
def uppercase(func):
    def wrapper(*args, **kwargs):
        # Call the original function and transform the result
        result = func(*args, **kwargs)
        return result.upper()  # Convert result to uppercase
    return wrapper

# `add_exclamation` adds an exclamation mark to the function's result
def add_exclamation(func):
    def wrapper(*args, **kwargs):
        # Call the original function and modify the result
        result = func(*args, **kwargs)
        return result + "!"  # Append an exclamation mark
    return wrapper

# Applying both decorators to the function `greet`
@uppercase  # This decorator is applied first
@add_exclamation  # This decorator is applied second (executed first)
def greet(name):
    return f"Hello, {name}"  # Original function result

# When `greet` is called, it will be processed by `add_exclamation` and then `uppercase`
print(greet("Alice"))  # Output: HELLO, ALICE!

# Decorators with arguments: Customizing decorator behavior with parameters
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the original function `n` times and concatenate the results
            result = ""
            for _ in range(n):  # Repeat `n` times
                result += func(*args, **kwargs) + "\n"  # Add a newline after each result
            return result
        return wrapper
    return decorator  # Returns the actual decorator

# Using the `repeat` decorator with argument `3`
@repeat(3)
def say_hello():
    return "Hello!"  # Original function result

# The `repeat` decorator ensures the function result is repeated 3 times
print(say_hello())
# Output:
# Hello!
# Hello!
# Hello!

# Class-based decorators: Creating decorators using a class
# A class decorator must implement the `__call__` method to make instances callable
class TimerDecorator:
    def __init__(self, func):
        self.func = func  # Store the original function

    def __call__(self, *args, **kwargs):
        # Measure execution time of the decorated function
        import time
        start = time.time()  # Start time
        result = self.func(*args, **kwargs)  # Call the original function
        end = time.time()  # End time
        print(f"Execution time: {end - start:.4f} seconds")  # Display elapsed time
        return result  # Return the original function's result

# Applying the class-based decorator to a function
@TimerDecorator
def compute():
    # Compute the sum of numbers from 0 to 999,999
    total = sum(range(10**6))
    return total  # Return the computed sum

# The `TimerDecorator` will display the execution time of `compute`
print(compute())  # Output includes the computed result and execution time
