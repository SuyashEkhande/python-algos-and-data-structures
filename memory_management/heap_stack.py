""" 
Python Memory Model consists of the heap and stack:

 - Heap: Stores dynamically allocated objects (e.g., lists, dictionaries, custom objects).
 - Stack: Stores function calls and local variables during execution.
"""


# Global variables are stored in the heap.
global_var = "I live in the heap"

def function_scope():
    # Local variable are stored in the stack.
    local_var = "I live in the stack"
    print(f"Local variable: {local_var}")
     # Accessible only during the function calllocal_var) # Accessible only during the function call

function_scope()

# Objects, even inside functions, are allocated on the heap.
def create_object():
    obj = {"key": "value"} # The dictionary itself is in the heap
    print(f"Object in heap: {obj}")
    

create_object()

# Python’s memory model ensures that objects are shared across references.
a = [1, 2, 3]  # The list is in the heap
b = a  # `b` points to the same object in the heap
b.append(4)
print(a)  # Output: [1, 2, 3, 4] (both `a` and `b` share the same memory location)

