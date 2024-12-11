import weakref

# Weak references allow referencing objects without increased their reference count
class MyObject:
    def __init__(self, name):
        self.name = name

# Create an object
obj = MyObject("WeakRef Object")
# Create a weak reference to the object
weak_obj = weakref.ref(obj)

print(f"Original Object: {obj}")
print(f"Weak Reference: {weak_obj().name}") # Access the object via the weak ref

# Delete the original object
del obj

# Weak referenec becomes 'None' after the object is garbage collected
print(f"Weak reference after deletion: {weak_obj()}")