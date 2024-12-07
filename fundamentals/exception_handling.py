# Python Exception Handling

# Basic Exception Handling
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Handling Multiple Exception
try:
    num = int("Hello") #ValueError
except(ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# Catching Multiple Exceptions with Different Blocks
try:
    num = int("Hello") #ValueError
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# Using Else Block
try:
    a = 10 / 2 #No Error
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {a}")

# Using Finally Block
try:
    a = 10 / 2 #No Error
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print(f"Result: {a}")   

# Raising Exception
try:
    raise ValueError("Custom Error")
except ValueError as e:
    print(f"Error: {e}")

# Custom Exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
try:
    raise CustomError("Custom Error")
except CustomError as e:
    print(f"Error: {e}")

# Catching All Exceptions
try:
    b = "hello" + 10 #TypeError
except Exception as e:
    print(f"Error: {e}")

# Assertions (Debugging Tool to check conditions)
x = 10
try:
    # Below Line makes sure that a certain condition is met
    assert x > 5, "x is not greater than 5" 
    print("Assertion Passed")
except AssertionError as e:
    print(f"Error: {e}")

# Handling Specific Error Type
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print("Invalid input type")
        return None
    else:
        return result
print(divide_numbers(10, 0)) #ZeroDivision Error
print(divide_numbers(10, "hello")) #TypeError
print(divide_numbers(10, 2)) #Valid

# Handling Exception Hierarchy (Parent and Child Exception)
class ParentError(Exception):
    pass

class ChildError(ParentError):
    pass

try:
    raise ChildError("This is a child exception")
except ParentError as e:
    print(f"ParentError: {e}")
except ChildError as e:
    print(f"ChildError: {e}")

# Handling Exceptions in List Comprehensions
numbers = [1, 2, 3, 4, 5]
result = []
for nums in numbers:
    try:
        result.append(10 / nums)
    except ZeroDivisionError as e:
        result.append(None)
    
print(f"Result of Division: {result}")

# Nested Exception Handling
try:
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        raise
except Exception as e:
    print(f"Outer Exception: {e}")

# Exception Handling with user input
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Context Manager and Exception Handling (Using with Statement)
class OpenFile:
    def __enter__(self):
        print("Opening file...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if exc_type is not None:
            print(f"Error occurred: {exc_value}")
        return True  # Suppresses exception

with OpenFile() as file:
    print("Reading file...")
    raise ValueError("Simulated error in file operation.")

# Exception Propagation (Exception passed up to the caller)
def function_a():
    raise ValueError("An error occurred in function_a")

def function_b():
    try:
        function_a()
    except ValueError as e:
        print(f"Handled in function_b: {e}")
        raise  # Propagate the error further

try:
    function_b()
except ValueError as e:
    print(f"Handled in main: {e}")