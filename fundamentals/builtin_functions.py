"""
Python Built-in Functions - Comprehensive Overview with Examples and Comments
Python has over 70 built-in functions, but here we'll focus on the most essential ones categorized by their use cases.
"""

# 1. Input/Output Functions
# - Used for interacting with the user or the console
print("=== Input/Output Functions ===")

# print(): Outputs data to the console
print("Hello, world!")  # Output: Hello, world!

# input(): Takes user input as a string
# Uncomment the line below to test
# name = input("Enter your name: ")  # User enters "Alice"
# print(f"Hello, {name}!")  # Output: Hello, Alice!

# 2. Type Conversion Functions
# - Used to convert between data types
print("\n=== Type Conversion Functions ===")

# int(): Converts to an integer
print(int("123"))  # Output: 123

# float(): Converts to a floating-point number
print(float("123.45"))  # Output: 123.45

# str(): Converts to a string
print(str(123))  # Output: "123"

# list(), tuple(), set(): Converts to respective collection types
print(list("abc"))  # Output: ['a', 'b', 'c']
print(tuple("abc"))  # Output: ('a', 'b', 'c')
print(set("abc"))  # Output: {'a', 'b', 'c'}

# 3. Numeric Functions
# - Perform operations on numbers
print("\n=== Numeric Functions ===")

# abs(): Returns the absolute value of a number
print(abs(-42))  # Output: 42

# round(): Rounds a number to a specified number of decimals
print(round(3.14159, 2))  # Output: 3.14

# pow(): Raises a number to a power
print(pow(2, 3))  # Output: 8

# 4. Iteration and Sequence Functions
# - Used for working with iterable objects
print("\n=== Iteration and Sequence Functions ===")

# len(): Returns the length of an iterable
print(len("hello"))  # Output: 5

# range(): Generates a range of numbers
for i in range(1, 5):
    print(i, end=" ")  # Output: 1 2 3 4
print()

# enumerate(): Returns index-value pairs for an iterable
for index, value in enumerate("abc"):
    print(index, value)  # Output: 0 a, 1 b, 2 c

# zip(): Combines multiple iterables into tuples
for pair in zip([1, 2, 3], ['a', 'b', 'c']):
    print(pair)  # Output: (1, 'a'), (2, 'b'), (3, 'c')

# 5. String Functions
# - Operate on string objects
print("\n=== String Functions ===")

# chr(): Converts an integer to its Unicode character
print(chr(65))  # Output: A

# ord(): Converts a character to its Unicode integer
print(ord('A'))  # Output: 65

# 6. File Handling Functions
# - Used for file operations
print("\n=== File Handling Functions ===")

# open(): Opens a file (read/write)
# with open("example.txt", "w") as file:
#     file.write("Hello, file!")
# # Uncomment the above lines to create a file and write to it

# 7. Utility Functions
# - Miscellaneous utility functions
print("\n=== Utility Functions ===")

# id(): Returns the memory address of an object
x = 42
print(id(x))  # Output: (varies)

# type(): Returns the type of an object
print(type(x))  # Output: <class 'int'>

# isinstance(): Checks if an object is an instance of a class/type
print(isinstance(x, int))  # Output: True

# dir(): Lists attributes and methods of an object
print(dir([]))  # Output: Methods and attributes of a list

# help(): Displays the help documentation for an object
# Uncomment the line below to test
# help(print)

# 8. Aggregation Functions
# - Perform calculations on collections
print("\n=== Aggregation Functions ===")

# sum(): Calculates the sum of elements in an iterable
print(sum([1, 2, 3]))  # Output: 6

# min(): Returns the smallest element
print(min([1, 2, 3]))  # Output: 1

# max(): Returns the largest element
print(max([1, 2, 3]))  # Output: 3

# 9. Functional Programming Helpers
# - Support higher-order functions
print("\n=== Functional Programming Helpers ===")

# map(): Applies a function to each element in an iterable
print(list(map(str.upper, ["a", "b", "c"])))  # Output: ['A', 'B', 'C']

# filter(): Filters elements based on a condition
print(list(filter(lambda x: x > 1, [1, 2, 3])))  # Output: [2, 3]

# 10. Advanced Functions
# - Used for introspection or special use cases
print("\n=== Advanced Functions ===")

# eval(): Evaluates a string as Python code
print(eval("2 + 2"))  # Output: 4

# sorted(): Returns a sorted list
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# any(): Returns True if any element is True
print(any([False, True, False]))  # Output: True

# all(): Returns True if all elements are True
print(all([True, True, True]))  # Output: True

# Thank you for exploring Python's built-in functions!
