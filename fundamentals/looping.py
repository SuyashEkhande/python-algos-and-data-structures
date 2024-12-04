# List For Loop

players = ["Ronaldo", "Messi", "Vinicius"]
print("For loop with a list: ")
for player in players:
    print(f'I like {player}')
print()

# Reverse For Loop

print("For loop in reverse: ")
for i in range(5, 0, -1):
    print(f'{i}')
print()

# For Loop Range

print("For loop with a range: ")
for j in range(1,6):
    print(f'Number: {j}')
print()

# For Loop Enumerate

print("For loop with enumerate: ")
for index, player in enumerate(players):
    print(f'Player {index+1}: {player}')
print()

# For Loop Dictionary

players = {
    "Ronaldo": 7,
    "Messi": 10,
    "Vinicius": 10
}
print("For loop with a dictionary: ")
for key, value in players.items():
    print(f'{key} [Jersey Number]: {value}')
print()

# Nested For Loops

print("Nested for loop: ")
for k in range(1,6):
    for l in range(1,6):
        print(f'k: {k}, l: {l}')
print()

# Enumerated Nested For Loops

destination = ["Hawaii", "Finland", "Thailand"]
transport = ["Boat", "Plane", "Train"]

print("Enumerated Nested for loop: ")
for dest_index, dest in enumerate(destination):
    for trans_index, trans in enumerate(transport):
        print(f'Visiting [{dest_index}]{dest} via [{trans_index}]{trans}')
print()


# While loop with counter

count = 3
print("While loop with counter: ")
while count > 0:
    print(f'Count: {count}')
    count -= 1
print()

# While loop with Else

print("While loop with else: ")
count = 3
while count > 0:
    print(f'Countdown: {count}')
    count -= 1
else:
    print("Blastoff!")
print()

# Break Statement

print("Break statement: ")
for c in range(1,6):
    if c == 3:
        break # Breaks out from loop
    print(f'Number: {c}')
print()

# Continue Statement

print("Continue statement: ")
for x in range(1,6):
    if x == 3:
        print("Skipping 3")
        continue # Skips current iteration
    print(f'Number: {x}')
print()

# Pass Statement

print("Pass statement: ")
for y in range(1,6):
    if y == 3:
        pass # Does Nothing
    print(f'Number: {y}')
print()



