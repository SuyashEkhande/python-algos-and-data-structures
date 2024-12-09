"""
In Python, polymorphism is usually achieved via method overriding. 
This happens when you define a method in the child class with the same-
name as one in the parent class, but with a different behavior.
"""

# Base class (Parent)
class Animal:
    def speak(self):
        pass # This method will be overridden by subclasses

# Subclass 1
class Dog(Animal):
    def speak(self):
        return "Woof!" # Dog speaks "Woof!" - overriding method
    
# Subclass 2
class Cat(Animal):
    def speak(self):
        return "Meow!" # Cat speaks "Meow!" - overriding method
    

# Creating objects of both classes
dog = Dog()
cat = Cat()

# Now let's call the 'speak' method on both objects
print(dog.speak())
print(cat.speak())


"""
Duck typing is a concept in dynamic languages like Python, 
where the type or class of an object is determined by its- 
behavior (methods and properties) rather than its explicit inheritance. 

In Python, this means that an object is considered of a certain type- 
if it has the necessary methods and properties, not because it explicitly- 
inherits from a particular class.
"""

# Example with Duck Typing

class Car:
    def speed_limit(self):
        print("Car speed liimit is 200 km/h")

class Bike:
    def speed_limit(self):
        print("Bike speed limit is 100 km/h")

class Truck:
    def speed_limit(self):
        print("Truck speed limit is 150 km/h")

# Function that expects an object to "speak", 
# i.e. the object has a "speak" method in its class
def speed_checker(vehicle: object):
    """
    Takes an object and calls the speed_limit method on that object
    """
    vehicle.speed_limit()

# Polymorphic behavior with duck typing
speed_checker(Car()) #Passing Car object
speed_checker(Bike()) #Passing Bike object
speed_checker(Truck()) #Passing Truck object