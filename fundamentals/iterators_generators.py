
"""
Key Differences:
Iterator: Requires defining the class with __iter__() and __next__(). 
You can iterate over it using a loop.

Generator: Defined using a function with yield, 
which produces values one at a time without storing the entire list in memory.
"""

# Iterator is an object which implements 
# __iter__() & __next__()
# Iterator Example
class Counter:
    def __init__(self, start, end):
        self.count = start
        self.end = end
    
    def __iter__(self):
        return self # The object itself is the iterator
    
    def __next__(self):
        if self.count >= self.end:
            raise StopIteration # for stopping iteration
        else:
            self.count += 1
            return self.count - 1
        
# Generator is a function that returns values lazily using yield
# Generator Example
def square_numbers(start, end):
    for num in range(start, end+1):
        yield num * num


# Using Iterator
print("Iterator Output: ")
counter = Counter(1, 5) # create a generator object
for num in counter:
    print(num)

# Using Generator
print("Generator Output: ")
for num in square_numbers(1, 5):
    print(num)