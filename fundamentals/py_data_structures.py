# Lists - Ordered, Mutable, Allows mixed datatypes
print("=== Lists ===")

# Create a list
my_list = [1, 2, 3, 4, 5]
print(f"Initial list: {my_list}")

# Adding elements
my_list.append(6)
print(f"After Append: {my_list}")
my_list.insert(2,'a')
print(f"After insert: {my_list}")

# Removing elements
my_list.remove(6)
print(f"After Remove: {my_list}")
my_list.pop(2)
print(f"After Pop: {my_list}")

# List Slicing
my_list = [1, 2, 3, 4, 5]
print(f"Initial list: {my_list}")
print(f"List Slicing(2:4): {my_list[2:4]}") # from index 2 to 3, exclusive of last mentioned slice index

# List Comprehension -- Refer comprehension.py for more detailed approaches
squared_list = [x**2 for x in range(1,11)]
print(f"Squared List: {squared_list}")

# Tuple - Ordered, Immutable, Allows mixed datatypes
print("=== Tuples ===")

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"Initial tuple: {my_tuple}")

# Accessing Elements
print(f"Element at index 2: {my_tuple[2]}")

# Tuples are Immutable so you cant change their values directly
# But you can create a new tuple
my_new_tuple = my_tuple + (6,7)
print(f"New Tuple: {my_new_tuple}")

# Sets - Unordered, Mutable, No duplicates
print("=== Sets ===")

# Create a set
my_set = {1, 2, 3, 4, 5}
print(f"Initial set: {my_set}")

# Adding elements
my_set.add(6)
print(f"After Add: {my_set}")
my_set.update([7,8])
print(f"After Update: {my_set}")

# Removing elements
my_set.remove(6) # throws error if not found
print(f"After Remove: {my_set}")
my_set.discard(7) # does nothing if not found
print(f"After Discard: {my_set}")
my_set.pop() # Removes and returns the value
print(f"After Pop: {my_set}, Popped Value: {my_set.pop()}")
my_set.clear() # Clears the set
print(f"After Clear: {my_set}")

# Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Set Difference: {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")

# Dictionary - Unordered, Mutable, Key-Value pairs
print("=== Dictionaries ===")

# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Initial dictionary: {my_dict}")

# Accessing Elements
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict.get('age')}")

# Adding & Updating elements
my_dict["occupation"] = "Engineer"
my_dict["age"] = 31
print(f"After Adding: {my_dict}")

# Removing elements
del my_dict["city"]
print(f"After Removing: {my_dict}")
removed_item = my_dict.pop("age")
print(f"After Pop: {my_dict}, Popped Value: {removed_item}")
my_dict.clear()
print(f"After Clear: {my_dict}")

# Dictionary Methods
my_dict = {'name': 'Alice', 'age': 25, 'location': 'Wonderland'}
keys = my_dict.keys()  # Get all keys
values = my_dict.values()  # Get all values
items = my_dict.items()  # Get all key-value pairs
print(f"Keys: {keys}, Values: {values}, Items: {items}")

# Dictionary Comprehension -- Refer comprehension.py for more detailed approaches
squared_dict = {x: x**2 for x in range(5)}
print(f"Squared Dictionary: {squared_dict}")
