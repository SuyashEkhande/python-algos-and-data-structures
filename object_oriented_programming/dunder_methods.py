"""
Dunder (double underscore) methods, provide special behavior to objects. 

Magic methods act as entry points for predefined Python functionalities,
like +, len(), or str(obj).

They define how objects behave when interacting with built-in functions
or operators in Python.

You can override these methods to add custom functionality while
preserving familiar syntax and behavior.

This makes objects flexible, Pythonic, and intuitive to work with.
"""

class DunderDemo:
    """Class demonstrating the usage of dunder methods in python"""

    def __init__(self, name, value):
        """Initialize the object"""
        self.name = name
        self.value = value
    
    def __str__(self):
        """User-friendly string representation"""
        return f"DunderDemo(name={self.name}, value={self.value})"
    
    def __repr__(self):
        """Technical string representation"""
        return f"DunderDemo({repr(self.name)}, {repr(self.value)})"
    
    def __add__(self, other):
        """Custom addition for objects"""
        if isinstance(other, DunderDemo):
            return DunderDemo(self.name + other.name, self.value + other.value)
        raise TypeError("Addition is support only between DunderDemo objects")
    
    def __eq__(self, other):
        """Check equality based on value"""
        if isinstance(other, DunderDemo):
            return self.value == other.value
        return False
    
    def __getitem__(self, index):
        """Retrieve a character from the name"""
        return self.name[index]

    def __setitem__(self, index, char):
        """Set a character in the name"""
        # Slices the string up to the specified index, 
        # adds the new character, and appends the remaining 
        # part of the string after the index to replace the 
        # character while maintaining Python's string immutability.
        self.name = self.name[:index] + char + self.name[index + 1:] 

    def __delitem__(self, index):
        """Delete a character from the name"""
        # Slices the string upto the index
        # continues the slicing after the index i.e + 1
        self.name = self.name[:index] + self.name[index + 1:]

    def __len__(self):
        """Return the length of the name"""
        return len(self.name)
    
    def __call__(self, multiplier):
        """Make the object callable to multiple value"""
        return self.value * multiplier
    
    def __del__(self):
        """Destroy the object"""
        print(f"Deleting DunderDemo({self.name}, {self.value})")


# creating instances
obj1 = DunderDemo("Dunder", 10)
obj2 = DunderDemo("Demo", 20)

# Using __str__ and __repr__
print(obj1)  # Output: DunderDemo(name=Dunder, value=10)
print(repr(obj2))  # Output: DunderDemo('Dunder', 10)

# Using arithmetic operation (__add__)
obj3 = obj1 + obj2
print(obj3)  # Output: DunderDemo(name=DunderDemo, value=30)

# Using comparison operation (__eq__)
print(obj1 == obj2)  # Output: False
print(obj1 == DunderDemo("Dunder", 10))  # Output: True

# Using container-like behavior (__getitem__, __setitem__, __delitem__, __len__)
print(obj1[0])  # Output: D
obj1[0] = "A" # Modifies name to "Aunder"
print(obj1)  # Output: DunderDemo(name=Aunder, value=10)

del obj1[0] # Deletes character at index 0
print(obj1)  # Output: DunderDemo(name=under, value=10)

print(len(obj1))  # Output: 6

# Using __call__ (callable object)
print(obj1(3))  # Output: 30

# Destructor (__del__)
del obj3
del obj2
del obj1


