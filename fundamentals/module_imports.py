# Importing built-in modules
import math # importing the module
import datetime as dt #importing with different name/alias
from random import randint, choice #importing specific functions

#Importing a custom module
import custom_module

# Using the math module
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Area of circle with radius {radius} is {area:.2f}")

# Using the datetime module with alias
current_date = dt.date.today()
print(f"Current date is {current_date}")

# Using specific functions from the random module
random_number = randint(1, 100)
random_choice = choice(["apple", "banana", "cherry"])
print(f"Random number: {random_number}")
print(f"Random choice: {random_choice}")

# Using a custom module
numbers = [1, 2, 3, 4, 5]
total = custom_module.calculate_sum(numbers)
print(f"Sum of numbers: {total}")

greeting = custom_module.say_hello("Alice")
print(greeting)

# Importing variables from custom_module
print(f"Variable from custom_module: {custom_module.AUTHOR}")
