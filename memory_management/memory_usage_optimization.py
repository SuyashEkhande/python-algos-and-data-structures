import sys

# Analyze memory usage of Python objects
int_var = 42
str_var = "hello"
list_var = [1, 2, 3]
dict_var = {"key": "value"}

print(f"Memory usage of int: {sys.getsizeof(int_var)} bytes")
print(f"Memory usage of str: {sys.getsizeof(str_var)} bytes")
print(f"Memory usage of list: {sys.getsizeof(list_var)} bytes")
print(f"Memory usage of dict: {sys.getsizeof(dict_var)} bytes")

# Memory optimization: Using generator expressions
large_list = [x for x in range(10**6)]  # List comprehension (large memory usage)
large_gen = (x for x in range(10**6))  # Generator expression (low memory usage)

print(f"Memory usage of list [x for x in range(10**6)]: {sys.getsizeof(large_list)} bytes")
print(f"Memory usage of generator (x for x in range(10**6): {sys.getsizeof(large_gen)} bytes")  # Only the generator object itself

# Efficient data structures: Use `__slots__` to reduce memory overhead
class OptimizedClass:
    __slots__ = ["attr1", "attr2"]  # Limit attributes to save memory
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

optimized_obj = OptimizedClass(10, 20)
print(f"Memory usage of optimized object: {sys.getsizeof(optimized_obj)} bytes")
