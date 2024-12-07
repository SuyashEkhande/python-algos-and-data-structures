# String Operations

# Declarations and initialization
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is a 
multi line string."""

print(f"Single Quote: {single_quote}")
print(f"Double Quote: {double_quote}")
print(f"Multi Line: {multi_line}")

#Accessing characters and slicing
sample_str = "1234567890"
print(f"\nOriginal String: {sample_str}")
print(f"First Character: {sample_str[0]}")
print(f"Last Character: {sample_str[-1]}")
print(f"Substring (1 to 6): {sample_str[1:6]}")
print(f"Reversed String: {sample_str[::-1]}")

# String Concatenation and repetition
greeting = "Hello" + " " + "World"
repeated = "Ha" * 3
print(f"\nConcatenated String: {greeting}")
print(f"Repeated String: {repeated}")

# String Methods
text = " Python is Awesome! "
print(f"\nOriginal String: {text}")
print(f"Lowercase: {text.lower()}")
print(f"Uppercase: {text.upper()}")
print(f"Strip Whitespaces: {text.strip()}")
print(f"Replace: {text.replace('Python', 'Node')}")
print(f"Split: {text.split(' ')}")
print(f"Join: {'-'.join(['Python', 'is', 'fun'])}")
print(f"Startswith 'Python': {text.strip().startswith('Python')}")
print(f"Endswith '!': {text.strip().endswith('!')}")

# String Formatting
name = "John"
age = 30
formatted = f"Hello, {name}. You are {age} years old."
print(f"\nFormatted String: {formatted}")

# Escape Characters
escape_str = "He said, \"Python is great!\" \nNew line and \tTab Example"
print(f"\nEscaped String: {escape_str}")

# String Immutability
immutable_str = "Hello"
# immutable_str[0] = 'h' # TypeError: 'str' object does not support item assignment
new_str = "h" + immutable_str[1:]
print(f"\nOriginal String: {immutable_str}")
print(f"New String: {new_str}")

# Checking Membership
contains_check = "Py" in sample_str
print(f"\nContains 'Py': {contains_check}")

# String Length
length_check = len(sample_str)
print(f"\nLength: {length_check}")

# Raw Strings
raw_str = r"This is a raw string\nIt ignores escape sequences"
print(f"\nRaw String: {raw_str}")

# Unicode and encoding
unicode_str = "नमस्ते😊"
encoded = unicode_str.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"\nOriginal String: {unicode_str}")
print(f"Encoded String: {encoded}")
print(f"Decoded String: {decoded}")

# Checking string properties
alphanumeric = "abc123"
print(f"\nIs alphanumeric: {alphanumeric.isalnum()}")
print(f"Is alpha: {alphanumeric.isalpha()}")
print(f"Is numeric: {alphanumeric.isnumeric()}")
print(f"Is lowercase: {'python'.islower()}")
print(f"Is uppercase: {'PYTHON'.isupper()}")
print(f"Is Digit: {'1234'.isdigit()}")

# Iterating through a string
print("\nIterating through a string chars:")
for char in "Python":
    print(char, end="")
print()

# Count occurrences
print(f"\nCount of 'o' in 'Hello World': {'Hello World'.count('o')}")