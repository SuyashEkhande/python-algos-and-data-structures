import gc  # Module for garbage collection inspection

# Reference counting:
class MyObject:
    pass

obj = MyObject()  # Reference count for `obj` is 1
obj_ref = obj  # Reference count is now 2
del obj  # Reference count decreases to 1
print("Object still exists.")  # `obj_ref` still holds a reference

# Cyclic Garbage Collection
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Create a circular reference
node1 = Node("Node 1")
node2 = Node("Node 2")
node1.next = node2
node2.next = node1

# Breaking ciruclar references
del node1, node2

# Manual garbage collection to clean circular references
collected = gc.collect()
print(f"Garbage collected {collected} objects.")