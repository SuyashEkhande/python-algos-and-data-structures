
# Basic Lambda Function
square = lambda x: x * x
print(f'Square of 5: {square(5)}')

# Lambda Function with Multiple Arguments
add = lambda x, y: x + y
print(f'Addition of 2 and 3: {add(2, 3)}')

# Lambda Function For Sorting
students = [("Alice", 25),("Bob", 22),("Charlie", 27)]
students_sorted = sorted(students, key = lambda student: student[1]) # sorted(list, key=function)
print(f'Sorted Students: {students_sorted}')

# Lambda Function with Map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers)) # map(function, list)
print(f'Squared Numbers: {squared_numbers}')

# Lambda Function with Filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filter(function, list)
print(f'Even Numbers: {even_numbers}')


# Lambda Function with Sorted (by Length)
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words = sorted(words, key = lambda word: len(word))
print(f'Sorted Words: {sorted_words}')

