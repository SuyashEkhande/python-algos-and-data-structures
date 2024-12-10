# Math module: Provides mathematical functions and constants.
# Common operations like factorials, square roots,
# logarithms, trigonometry functions (sin, cos), and more.
import math

print("\nMath module:")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")
print(f"sin(30 degrees in radians): {math.sin(math.radians(30))}")
print(f"cos(30 degrees in radians): {math.cos(math.radians(30))}")
print(f"Log of 100 with base 10: {math.log10(100)}")
print(f"Log of 8 with base 2: {math.log(8, 2)}")


# Random module: Used for generating random numbers,
# making random selections from sequences, and shuffling.
import random

print("\nRandom module:")
print(f"Random float (0-1): {random.random()}")
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random float (1, 10): {random.uniform(1, 10)}")
print(f"Random choice from list [10, 20, 30]: {random.choice([10, 20, 30])}")
print(f"Random sample (3 items) from list: {random.sample([10, 20, 30, 40, 50], 3)}")
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(f"Shuffled list: {data}")


# Datetime module: Handles date and time operations,
# such as getting current time, adding/subtracting days,
# and formatting dates in various ways.
import datetime

now = datetime.datetime.now()
print("\nDatetime module:")
print(f"Current datetime: {now}")
print(f"5 days later: {now + datetime.timedelta(days=5)}")
print(f"Formatted date (YYYY-MM-DD): {now.strftime('%Y-%m-%d')}")
print(f"Creating custom date: {datetime.datetime(2023, 12, 25)}")
print(f"Difference between now and 5 days ago: {now - (now - datetime.timedelta(days=5))}")


# OS module: Provides functions to interact with the operating
# system, such as manipulating files, directories, and environment.
import os

print("\nOS module:")
print(f"Current directory: {os.getcwd()}")
print(f"List of files: {os.listdir()}")
print(f"Environment PATH: {os.environ.get('PATH')}")
print(f"Renaming a file: {os.rename('old_file.txt', 'new_file.txt')}")
print(f"Removing a file: {os.remove('new_file.txt')}")
print(f"Traversing directory with os.walk(): {list(os.walk('.'))}")


# Sys module: Provides access to some variables used or maintained
# by the interpreter and functions to interact with the Python runtime.
import sys

print("\nSys module:")
print(f"Python version: {sys.version}")
print(f"Command-line arguments: {sys.argv}")
print(f"Path where Python is installed: {sys.executable}")
print(f"Maximum recursion depth: {sys.getrecursionlimit()}")


# Re module: Provides regular expression tools for pattern matching,
# searching, and manipulating text with regex-based patterns.
import re

pattern = r"\b[a-zA-Z]{3}\b"
text = "cat bat mat sat at hat"
matches = re.findall(pattern, text)
print("\nRe module:")
print(f"Words with exactly 3 letters: {matches}")
print(f"Replace 'cat' with 'dog': {re.sub(r'cat', 'dog', text)}")
print(f"Search for 'mat' in the text: {re.search(r'mat', text).group()}")
print(f"Find all words starting with 'a': {re.findall(r'\ba\w*', text)}")


# Itertools module: Provides building blocks for constructing iterators
# that operate on items of a sequence. It supports infinite iterators,
# combinatoric iterators, and more.
import itertools

print("\nItertools module:")

# count: Generates an infinite sequence of numbers, 
# starting from a number and incrementing by a step.
count_iter = itertools.count(start=5, step=3)
print(f"First 5 values of count(5, 3): {list(itertools.islice(count_iter, 5))}")

# cycle: Repeats the given iterable indefinitely.
cycle_iter = itertools.cycle([1, 2, 3])
print(f"First 6 values of cycle([1, 2, 3]): {list(itertools.islice(cycle_iter, 6))}")

# repeat: Repeats the value for a specified number of times.
repeat_iter = itertools.repeat(7, 4)
print(f"Repeat 7 for 4 times: {list(repeat_iter)}")

# chain: Combines multiple iterables into one continuous iterator.
chain_iter = itertools.chain([1, 2], [3, 4], [5, 6])
print(f"Chain of lists: {list(chain_iter)}")

# combinations: Generates all possible combinations of a 
# specified length from the iterable.
combinations_iter = itertools.combinations([1, 2, 3, 4], 2)
print(f"Combinations of length 2: {list(combinations_iter)}")

# permutations: Generates all possible permutations of a 
# specified length from the iterable.
permutations_iter = itertools.permutations([1, 2, 3], 2)
print(f"Permutations of length 2: {list(permutations_iter)}")

# product: Generates the Cartesian product of input iterables, 
# equivalent to nested for-loops.
product_iter = itertools.product([1, 2], ['a', 'b'])
print(f"Cartesian product of [1, 2] and ['a', 'b']: {list(product_iter)}")

# compress: Filters elements from an iterable based on a selector iterable.
data = ['a', 'b', 'c', 'd']
selector = [1, 0, 1, 0]
compressed_iter = itertools.compress(data, selector)
print(f"Compressed data: {list(compressed_iter)}")


# Functools module: Provides higher-order functions 
# that work on functions or return functions.
import functools

print("\nFunctools module:")

# reduce: Applies a binary function (passed as argument) cumulatively
#  to the items of an iterable.
nums = [1, 2, 3, 4]
reduce_result = functools.reduce(lambda x, y: x + y, nums)
print(f"Sum of {nums} using reduce: {reduce_result}")

# lru_cache: Caches the results of expensive or frequently called 
# functions to optimize performance.
@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(f"Fibonacci number at index 10: {fib(10)}")
print(f"Fibonacci number at index 20: {fib(20)}")

# partial: Creates a new function with some arguments fixed.
partial_add = functools.partial(lambda x, y: x + y, 5)
print(f"Partial function that adds 5: {partial_add(3)}")  # Output will be 8


# JSON module: Provides functions to work with JSON data, including serialization and deserialization.
import json

print("\nJSON module:")

# json.dumps: Converts a Python object to a JSON string.
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(f"Serialized JSON: {json_string}")

# json.loads: Converts a JSON string back to a Python object.
json_obj = json.loads(json_string)
print(f"Deserialized Python object: {json_obj}")

# json.dump: Writes a Python object as a JSON string to a file.
with open("data.json", "w") as f:
    json.dump(data, f)
print("Python object written to data.json")

# json.load: Reads a JSON string from a file and converts it back to a Python object.
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(f"Loaded data from file: {loaded_data}")

# json.dumps with indentation: Converts Python object to a formatted JSON string.
formatted_json = json.dumps(data, indent=4)
print(f"Formatted JSON with indentation:\n{formatted_json}")