## List

# Basic List Comprehension: Squares of numbers from 0 to 4
squares_list = [x**2 for x in range(1,11)]
print(f'Squares List: {squares_list}')

# Filtered List Comprehension: Only squares of even numbers
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]
print(f'Even Squares: {even_squares}')

# The list comprehension [item for sublist in matrix for item in sublist] 
# flattens a 2D list matrix by iterating over each sublist and then over each 
# item within those sublists, collecting all the items into a single 1D list.
matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
flattened_list = [item for sublist in matrix for item in sublist]
print(f'Flattened List: {flattened_list}')

# List Comprehension with `else`: Squaring even numbers and cubing odd numbers
squares_and_cubes = [ x**2 if x % 2 == 0 else x**3 for x in range(1,11)]
print(f'Squares and Cubes: {squares_and_cubes}')

## Set

# Basic Set Comprehension: Squares of numbers from 0 to 4
squares_set = {x**2 for x in range(5)}
print(f"Squares Set: {squares_set}")

# Filtered Set Comprehension: Only squares of even numbers
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even Squares Set: {even_squares_set}")

# Set Comprehension with Condition: Only numbers divisible by 3
div_by_3_set = {x for x in range(10) if x % 3 == 0}
print(f"Divisible by 3 Set: {div_by_3_set}")

# Set Comprehension with `else`: Squaring even and cubing odd numbers
squares_and_cubes_set = {x**2 if x % 2 == 0 else x**3 for x in range(5)}
print(f"Squares and Cubes Set: {squares_and_cubes_set}")

## Dictionary

# Basic Dictionary Comprehension: Numbers and their squares
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares Dictionary: {squares_dict}")

# Filtered Dictionary Comprehension: Only squares of even numbers
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even Squares Dictionary: {even_squares_dict}")

# Nested dictionary comprehension: 

players = ['Messi', 'Ronaldo', 'Zidane']
data = ['Jersey', 'Team']
nested_dict = {player: {info: f"{info}_{player}" for info in data} for player in players}
print(nested_dict)


# Dictionary Comprehension with Condition: Only numbers divisible by 3
div_by_3_dict = {x: x**2 for x in range(10) if x % 3 == 0}
print(f"Divisible by 3 Dictionary: {div_by_3_dict}")

# Dictionary with `else`: Squaring even and cubing odd numbers
squares_and_cubes_dict = {x: (x**2 if x % 2 == 0 else x**3) for x in range(5)}
print(f"Squares and Cubes Dictionary: {squares_and_cubes_dict}")

## Generator / Tuple

# Basic Generator Expression: Generating squares of numbers from 0 to 4
squares_gen = (x**2 for x in range(5))
print(f"Squares Generator: {list(squares_gen)}")

# Filtered Generator Expression: Only squares of even numbers
even_squares_gen = (x**2 for x in range(10) if x % 2 == 0)
print(f"Even Squares Generator: {list(even_squares_gen)}")

# Generator Expression with Condition: Only numbers divisible by 3
div_by_3_gen = (x for x in range(10) if x % 3 == 0)
print(f"Divisible by 3 Generator: {list(div_by_3_gen)}")

# Generator with `else`: Squaring even and cubing odd numbers
squares_and_cubes_gen = (x**2 if x % 2 == 0 else x**3 for x in range(5))
print(f"Squares and Cubes Generator: {list(squares_and_cubes_gen)}")






