
# Basic Function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Default Argument
def greeting(name="User"):
    print(f"Hello, {name}!")

greeting()
greeting("Bob")

# Return Multiple Values
def divide_and_remainder(a, b):
    return a // b, a % b

result, remainder = divide_and_remainder(10, 3)
print(f"Result: {result}, Remainder: {remainder}")

# Positional Arguments: Pass n Number of Sequential Data
# Keyword Arguments: Pass n Number of Named Data
def show_items(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_items("Item 1", "Item 2", "Item 3", key1="Value 1", key2="Value 2")

# lambda functions
gradesSum = lambda grades: sum(grades)
grades = [98, 80, 92, 89, 95]
print(f'Grades Sum: {gradesSum(grades)}')

# Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f'Factorial: {factorial(5)}')

# Function Annotations
def multiply(a: int, b: int) -> int:
    return a * b

print(f'Multiply: {multiply(2, 3)}')

# Higher-Order Functions : Accept Functions in arguments/Return functions
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x**2, 5)
print(f'Result: {result}')

# Inner/Nested Functions
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)

print(f'Result from Inner Function: {outer_function(5)}')

# Decorators
# A decorator wraps a function, adding pre/post-execution behavior 
# via a wrapper function. When you call the decorated function, arguments 
# are passed to the wrapper, which then calls the original function and returns its result.
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called...")
        result = func(*args, **kwargs)
        print("Function has been called.")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Suyash")

# Generator Functions
def countdown(n):
    while n > 0:
        yield n
        n = n - 1

for num in countdown(5):
    print(num, end=" ")
print()






