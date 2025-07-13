"""
Singleton Design Pattern Implementation

The Singleton pattern ensures that a class has only one instance
and provides a global point of access to that instance.
"""

import threading
from functools import wraps


class SingletonMeta(type):
    """
    Thread-safe Singleton implementation using metaclass.
    """
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                # Double-checked locking pattern
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """
    Example: Database connection singleton.
    """
    
    def __init__(self):
        self.connection = None
        self.host = "localhost"
        self.port = 5432
        self.connected = False
        print("Database instance created")
    
    def connect(self):
        if not self.connected:
            print(f"Connecting to database at {self.host}:{self.port}")
            self.connected = True
            return True
        print("Already connected to database")
        return True
    
    def disconnect(self):
        if self.connected:
            print("Disconnecting from database")
            self.connected = False
        else:
            print("Not connected to database")
    
    def query(self, sql):
        if self.connected:
            print(f"Executing query: {sql}")
            return f"Result of: {sql}"
        else:
            raise ConnectionError("Not connected to database")


class SingletonDecorator:
    """
    Singleton implementation using decorator.
    """
    def __init__(self, cls):
        self._cls = cls
        self._instance = None
        self._lock = threading.Lock()
    
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            with self._lock:
                if self._instance is None:
                    self._instance = self._cls(*args, **kwargs)
        return self._instance


@SingletonDecorator
class Logger:
    """
    Example: Logger singleton using decorator.
    """
    
    def __init__(self):
        self.log_level = "INFO"
        self.log_file = "app.log"
        print("Logger instance created")
    
    def log(self, message, level="INFO"):
        print(f"[{level}] {message}")
    
    def set_level(self, level):
        self.log_level = level
        print(f"Log level set to {level}")


class ConfigManager:
    """
    Configuration manager singleton using __new__ method.
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.config = {
                "app_name": "MyApp",
                "version": "1.0.0",
                "debug": False
            }
            self._initialized = True
            print("ConfigManager instance created")
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        print(f"Config updated: {key} = {value}")
    
    def get_all(self):
        return self.config.copy()


def singleton_function(cls):
    """
    Simple singleton decorator function.
    """
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton_function
class CacheManager:
    """
    Cache manager singleton using function decorator.
    """
    
    def __init__(self):
        self.cache = {}
        self.max_size = 100
        print("CacheManager instance created")
    
    def get(self, key):
        return self.cache.get(key)
    
    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            # Simple LRU: remove first item
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        
        self.cache[key] = value
        print(f"Cache updated: {key} = {value}")
    
    def clear(self):
        self.cache.clear()
        print("Cache cleared")
    
    def size(self):
        return len(self.cache)


class RegistryManager:
    """
    Registry-based singleton implementation.
    """
    _registry = {}
    
    @classmethod
    def register(cls, name, instance):
        cls._registry[name] = instance
    
    @classmethod
    def get_instance(cls, name):
        return cls._registry.get(name)
    
    @classmethod
    def remove(cls, name):
        if name in cls._registry:
            del cls._registry[name]


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== Singleton Design Pattern Examples ===")
    
    # Metaclass Singleton
    print("\n1. Metaclass Singleton (Database):")
    db1 = Database()
    db2 = Database()
    print(f"db1 is db2: {db1 is db2}")
    print(f"db1 id: {id(db1)}, db2 id: {id(db2)}")
    
    db1.connect()
    result = db1.query("SELECT * FROM users")
    print(f"Query result: {result}")
    
    # Decorator Singleton
    print("\n2. Decorator Singleton (Logger):")
    logger1 = Logger()
    logger2 = Logger()
    print(f"logger1 is logger2: {logger1 is logger2}")
    
    logger1.log("Application started")
    logger2.log("Database connected")
    logger1.set_level("DEBUG")
    
    # __new__ method Singleton
    print("\n3. __new__ method Singleton (ConfigManager):")
    config1 = ConfigManager()
    config2 = ConfigManager()
    print(f"config1 is config2: {config1 is config2}")
    
    config1.set("debug", True)
    print(f"config2.get('debug'): {config2.get('debug')}")
    print(f"All config: {config2.get_all()}")
    
    # Function decorator Singleton
    print("\n4. Function Decorator Singleton (CacheManager):")
    cache1 = CacheManager()
    cache2 = CacheManager()
    print(f"cache1 is cache2: {cache1 is cache2}")
    
    cache1.set("user:123", {"name": "Alice", "age": 30})
    cached_user = cache2.get("user:123")
    print(f"Cached user: {cached_user}")
    print(f"Cache size: {cache2.size()}")
    
    # Registry-based approach
    print("\n5. Registry-based Singleton:")
    # Create and register instances
    db_instance = Database()
    logger_instance = Logger()
    
    RegistryManager.register("database", db_instance)
    RegistryManager.register("logger", logger_instance)
    
    # Retrieve instances
    retrieved_db = RegistryManager.get_instance("database")
    retrieved_logger = RegistryManager.get_instance("logger")
    
    print(f"Retrieved DB is same: {retrieved_db is db_instance}")
    print(f"Retrieved Logger is same: {retrieved_logger is logger_instance}")
    
    print("\n=== Thread Safety Test ===")
    import concurrent.futures
    
    def create_database():
        return Database()
    
    # Test thread safety
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(create_database) for _ in range(5)]
        instances = [future.result() for future in futures]
    
    # Check if all instances are the same
    all_same = all(instance is instances[0] for instance in instances)
    print(f"All instances are the same (thread-safe): {all_same}")
    
    print("\nNote: Singleton pattern ensures single instance but consider:")
    print("- Thread safety in multi-threaded environments")
    print("- Global state management challenges")
    print("- Testing difficulties (shared state)")
    print("- Alternative: Dependency Injection for better testability")
