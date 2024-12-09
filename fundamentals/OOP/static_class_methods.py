"""
Static Method:
Use static methods when you want to define a function
that logically belongs to the class but does not need
to interact with any instance or class data. 
Examples include utility functions, helper methods, 
or methods that just process inputs and outputs.

Class Method:
Use class methods when you need to access or modify
class-level data or when you need a method that works 
with the class itself, like alternative constructors or 
methods that track or manipulate class-level state.
"""

class Dog:

    # Class variable
    total_dogs = 0 # Non unique to each object

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1  # Increment the class variable every time a new dog is created

    @staticmethod
    def is_dog_friendly(breed):
        """Static method: Checks if the breed is known for being friendly"""
        friendly_breeds = ['Labrador', 'vodafone', 'Beagle']
        return breed in friendly_breeds
    
    @classmethod
    def get_total_dogs(cls):
        """Class method: Returns the total number of dogs created"""
        return cls.total_dogs
    
# Creating dog objects
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Bulldog")

# Calling static method
print(Dog.is_dog_friendly("Labrador"))  # True
print(Dog.is_dog_friendly("Bulldog"))   # False

# Calling class method
print(f"Total number of dogs: {Dog.get_total_dogs()}")  # 2