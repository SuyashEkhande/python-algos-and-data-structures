"""
Factory Design Pattern Implementation

The Factory pattern provides an interface for creating objects without
specifying the exact class of object that will be created.
"""

from abc import ABC, abstractmethod
from enum import Enum


# Abstract Product
class Animal(ABC):
    """Abstract base class for all animals."""
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def get_type(self):
        pass


# Concrete Products
class Dog(Animal):
    """Concrete Dog class."""
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def get_type(self):
        return "Dog"


class Cat(Animal):
    """Concrete Cat class."""
    
    def make_sound(self):
        return "Meow! Meow!"
    
    def get_type(self):
        return "Cat"


class Bird(Animal):
    """Concrete Bird class."""
    
    def make_sound(self):
        return "Tweet! Tweet!"
    
    def get_type(self):
        return "Bird"


# Simple Factory
class AnimalFactory:
    """
    Simple Factory for creating animals.
    """
    
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat,
            'bird': Bird
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Factory Method Pattern
class AnimalCreator(ABC):
    """
    Abstract creator class for Factory Method pattern.
    """
    
    @abstractmethod
    def create_animal(self):
        """Factory method to be implemented by subclasses."""
        pass
    
    def interact_with_animal(self):
        """Template method using the factory method."""
        animal = self.create_animal()
        return f"{animal.get_type()} says: {animal.make_sound()}"


class DogCreator(AnimalCreator):
    """Concrete creator for dogs."""
    
    def create_animal(self):
        return Dog()


class CatCreator(AnimalCreator):
    """Concrete creator for cats."""
    
    def create_animal(self):
        return Cat()


class BirdCreator(AnimalCreator):
    """Concrete creator for birds."""
    
    def create_animal(self):
        return Bird()


# Abstract Factory Pattern
class VehicleFactory(ABC):
    """Abstract factory for creating vehicles."""
    
    @abstractmethod
    def create_car(self):
        pass
    
    @abstractmethod
    def create_motorcycle(self):
        pass


class Vehicle(ABC):
    """Abstract vehicle class."""
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def get_info(self):
        pass


# European Vehicles
class EuropeanCar(Vehicle):
    def start(self):
        return "European car started with manual transmission"
    
    def get_info(self):
        return "European Car - Compact, fuel-efficient"


class EuropeanMotorcycle(Vehicle):
    def start(self):
        return "European motorcycle started - smooth ride"
    
    def get_info(self):
        return "European Motorcycle - Lightweight, agile"


# American Vehicles
class AmericanCar(Vehicle):
    def start(self):
        return "American car started with automatic transmission"
    
    def get_info(self):
        return "American Car - Large, powerful engine"


class AmericanMotorcycle(Vehicle):
    def start(self):
        return "American motorcycle started - powerful rumble"
    
    def get_info(self):
        return "American Motorcycle - Heavy, long-distance touring"


# Concrete Factories
class EuropeanVehicleFactory(VehicleFactory):
    """Factory for European vehicles."""
    
    def create_car(self):
        return EuropeanCar()
    
    def create_motorcycle(self):
        return EuropeanMotorcycle()


class AmericanVehicleFactory(VehicleFactory):
    """Factory for American vehicles."""
    
    def create_car(self):
        return AmericanCar()
    
    def create_motorcycle(self):
        return AmericanMotorcycle()


# Factory with Registration
class PluginFactory:
    """
    Factory that allows runtime registration of new types.
    """
    
    def __init__(self):
        self._creators = {}
    
    def register(self, type_name, creator_class):
        """Register a new creator class."""
        self._creators[type_name] = creator_class
    
    def create(self, type_name, **kwargs):
        """Create an object of the specified type."""
        creator_class = self._creators.get(type_name)
        if not creator_class:
            raise ValueError(f"Unknown type: {type_name}")
        return creator_class(**kwargs)
    
    def get_available_types(self):
        """Return list of available types."""
        return list(self._creators.keys())


# Database Connection Factory Example
class DatabaseConnection(ABC):
    """Abstract database connection."""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLConnection(DatabaseConnection):
    def __init__(self, host="localhost", port=3306):
        self.host = host
        self.port = port
    
    def connect(self):
        return f"Connected to MySQL at {self.host}:{self.port}"
    
    def execute_query(self, query):
        return f"MySQL executing: {query}"


class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, host="localhost", port=5432):
        self.host = host
        self.port = port
    
    def connect(self):
        return f"Connected to PostgreSQL at {self.host}:{self.port}"
    
    def execute_query(self, query):
        return f"PostgreSQL executing: {query}"


class MongoDBConnection(DatabaseConnection):
    def __init__(self, host="localhost", port=27017):
        self.host = host
        self.port = port
    
    def connect(self):
        return f"Connected to MongoDB at {self.host}:{self.port}"
    
    def execute_query(self, query):
        return f"MongoDB executing: {query}"


class DatabaseFactory:
    """Factory for creating database connections."""
    
    @staticmethod
    def create_connection(db_type, **kwargs):
        connections = {
            'mysql': MySQLConnection,
            'postgresql': PostgreSQLConnection,
            'mongodb': MongoDBConnection
        }
        
        connection_class = connections.get(db_type.lower())
        if connection_class:
            return connection_class(**kwargs)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")


# GUI Factory Example
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


# Windows GUI Components
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button"


class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows-style checkbox"


# Mac GUI Components
class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button"


class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering Mac-style checkbox"


# Abstract GUI Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()


class MacGUIFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()


class GUIApplication:
    """Application that uses GUI factory."""
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
    
    def create_interface(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        
        return {
            'button': button.render(),
            'checkbox': checkbox.render()
        }


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Factory Design Pattern Examples ===")
    
    # Simple Factory
    print("\n1. Simple Factory Pattern:")
    animals = ['dog', 'cat', 'bird']
    for animal_type in animals:
        animal = AnimalFactory.create_animal(animal_type)
        print(f"{animal.get_type()}: {animal.make_sound()}")
    
    # Factory Method Pattern
    print("\n2. Factory Method Pattern:")
    creators = [DogCreator(), CatCreator(), BirdCreator()]
    for creator in creators:
        result = creator.interact_with_animal()
        print(result)
    
    # Abstract Factory Pattern
    print("\n3. Abstract Factory Pattern (Vehicles):")
    factories = [EuropeanVehicleFactory(), AmericanVehicleFactory()]
    
    for factory in factories:
        car = factory.create_car()
        motorcycle = factory.create_motorcycle()
        
        factory_type = "European" if isinstance(factory, EuropeanVehicleFactory) else "American"
        print(f"\n{factory_type} Factory:")
        print(f"  Car: {car.get_info()}")
        print(f"  Car start: {car.start()}")
        print(f"  Motorcycle: {motorcycle.get_info()}")
        print(f"  Motorcycle start: {motorcycle.start()}")
    
    # Plugin Factory with Registration
    print("\n4. Plugin Factory with Registration:")
    plugin_factory = PluginFactory()
    
    # Register database connection types
    plugin_factory.register('mysql', MySQLConnection)
    plugin_factory.register('postgresql', PostgreSQLConnection)
    plugin_factory.register('mongodb', MongoDBConnection)
    
    print(f"Available types: {plugin_factory.get_available_types()}")
    
    # Create connections
    mysql_conn = plugin_factory.create('mysql', host='db.example.com')
    postgres_conn = plugin_factory.create('postgresql', port=5433)
    
    print(mysql_conn.connect())
    print(postgres_conn.connect())
    print(mysql_conn.execute_query("SELECT * FROM users"))
    
    # Database Factory
    print("\n5. Database Factory:")
    databases = ['mysql', 'postgresql', 'mongodb']
    
    for db_type in databases:
        conn = DatabaseFactory.create_connection(db_type)
        print(f"{db_type.upper()}: {conn.connect()}")
        print(f"  Query result: {conn.execute_query('SELECT * FROM products')}")
    
    # GUI Abstract Factory
    print("\n6. GUI Abstract Factory:")
    
    # Create Windows application
    windows_factory = WindowsGUIFactory()
    windows_app = GUIApplication(windows_factory)
    windows_ui = windows_app.create_interface()
    
    print("Windows Application:")
    for component, render_result in windows_ui.items():
        print(f"  {component}: {render_result}")
    
    # Create Mac application
    mac_factory = MacGUIFactory()
    mac_app = GUIApplication(mac_factory)
    mac_ui = mac_app.create_interface()
    
    print("\nMac Application:")
    for component, render_result in mac_ui.items():
        print(f"  {component}: {render_result}")
    
    print("\nNote: Factory patterns provide:")
    print("- Loose coupling between client and concrete classes")
    print("- Easy addition of new product types")
    print("- Centralized object creation logic")
    print("- Support for product families (Abstract Factory)")
