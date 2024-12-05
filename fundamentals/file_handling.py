import os

# Set the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Write Mode: Create or Overwrite a file
print(f"Writing to a file ('w' mode)")
with open("file_handling.txt","w") as file:
    file.write("Hello World\n")
    file.write("This is a test\n")
print(f"File created and written. \n")

# Append Mode: Add more content to the file
print(f"Appending to a file ('a' mode)")
with open("file_handling.txt","a") as file:
    file.write("This is a test for append\n")
    file.write("This is a test for append\n")
print(f"File created and written. \n")

# Read Mode: Read a file
print(f"Reading a file ('r' mode)")
with open("file_handling.txt","r") as file:
    content = file.read()
    print(content)
print(f"File created and read. \n")

# Create Mode: Create a new file ('x' mode)
try:
    print(f"Creating a new file ('x' mode)")
    with open("new_file.txt","x") as file:
        file.write("Hello World\n")
        file.write("This is a test\n")
    print(f"File created. \n")
except FileExistsError:
    print(f"File already exists. \n")

# Handling Binary Files
print(f"Writing to a binary file ('wb' mode)")
binary_data = b"Python is great for binary data!\n" #byte level data
with open("file_handling.txt","wb") as file:
    file.write(binary_data)
print(f"File created and written. \n")

# Reading a binary file
print(f"Reading a binary file ('rb' mode)")
with open("file_handling.txt","rb") as file:
    binary_data = file.read()
    print(f"Binary data: {binary_data}")
print(f"Binary File Written \n")

# Error Handling
print(f"Handling errors during file operations")
try:
    with open("non_existent_file.txt","r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(f"Error: {e}")

# If not using file handling using the "with" syntax
# you have to close the file manually
print(f"Closing a file manually")
try:
    file = open("file_handling.txt","r")
    content = file.read()
    print(content)
finally:
    file.close() # Must close the file manually if not using 'with'
    print(f"File closed manually \n")