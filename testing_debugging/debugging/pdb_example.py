"""
To use pdb, you need to import it and insert a breakpoint in 
your code using pdb.set_trace(). The program will stop executing 
when it reaches this line, allowing you to interact with it via the command line.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract second number from first."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide first number by second."""
    import pdb; pdb.set_trace()  # Insert breakpoint here
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(a, b, operation):
    """Perform a calculation based on the operation."""
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        raise ValueError("Invalid operation")
    
"""
Example Debugging Session:
After running the code, you'll be stopped at pdb.set_trace().
Type n to go to the next line and check if b == 0 is being evaluated.
Use p b to print the value of b. You can see that b is 0, and you can 
understand why the exception is being raised.
If you want to continue running the code after inspecting it, 
you can type c to proceed.
"""
result = calculate(10, 0, "divide")
print(result)