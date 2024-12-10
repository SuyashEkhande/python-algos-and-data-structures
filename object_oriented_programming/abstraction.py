"""
Abstraction allows the programmer to focus on the 
high-level functionality of a system while abstracting 
away the complexity that lies underneath.

Key Concepts of Abstraction:
--
[Abstract Classes]: Classes that cannot be instantiated on their 
own but serve as a blueprint for other classes.

[Abstract Methods]: Methods that are declared in an abstract class
but do not have an implementation. Subclasses must provide
an implementation for these methods.

[Concrete Classes]: Classes that implement all abstract methods
and can be instantiated.
"""

# In Python, abstraction is implemented using the abc module, 
# which stands for Abstract Base Classes.
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC): # Initializing with abstract class 'ABC' from abc module
    # Concrete method -- provides implementation
    def speak(self):
        print("The animal makes a sound.")

    # Abstract method
    @abstractmethod
    def move(self):
        pass


# Concrete class 1
class Dog(Animal):
    def move(self):
        print("The dog is walking.")

# Concrete class 2
class Bird(Animal):
    def move(self):
        print("The bird is flying.")

# Concrete class 3
class Fish(Animal):
    def move(self):
        print("The fish is swimming.")


# Testing the abstraction
def test_animal_movement(animal: Animal):
    print(f"Testing movement of {animal.__class__.__name__}")
    animal.move()

# Creating instances of concrete classes
dog = Dog()
bird = Bird()
fish = Fish()

# Testing the move functionality for each animal
test_animal_movement(dog)    # Output: The dog runs.
test_animal_movement(bird)   # Output: The bird flies.
test_animal_movement(fish)   # Output: The fish swims.

# Trying to create an instance of the abstract class 
# directly will raise an error
# animal = Animal()  # This will raise TypeError: 
# Can't instantiate abstract class Animal with abstract method move