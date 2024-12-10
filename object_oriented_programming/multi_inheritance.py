# Demonstrating the concept of multiple inheritance
# in Python, where a derived class can inherit 
# attributes and methods from more than one base class.
# This example showcases a vehicle and electric classes 
# and their combination in an ElectricCar class.

# Base class 1
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    
    def show_vehicle_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


# Base class 2
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def show_battery_info(self):    
        print(f"Battery Capacity: {self.battery_capacity}")


# Derived class using Multiple Inheritance
class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, wheels, battery_capacity, model):
        # Initialize both parent classes using super() and class names
        Vehicle.__init__(self, brand, wheels)
        Electric.__init__(self, battery_capacity)
        self.model = model
    
    def show_car_info(self):
        self.show_vehicle_info() # From Vehicle class
        self.show_battery_info() # From Electric class
        print(f"Model: {self.model}")

    
# Demonstrating Method Resolution Order (MRO)
print(ElectricCar.mro()) # Displays the order in which methods are resolved

# Create an object of ElectricCar
tesla = ElectricCar(brand = "Tesla", wheels=4, battery_capacity=100, model="Model S")
tesla.show_car_info()
