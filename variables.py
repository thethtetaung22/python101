# Variable assignment
x = 10
name = "Alice"

# Printing output
print(x)
print("Hello,", name)

# Basic data types
integer_num = 5
float_num = 3.14
string_text = "Python"
boolean_val = True

# Lists
numbers = [1, 2, 3, 4, 5]

# Dictionaries
person = {"name": "Bob", "age": 25}

# Conditional statements
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Loops
for num in numbers:
    print(num)

# Functions
def greet(user):
    print("Hello,", user)

greet("Thet")

# ...existing code...

# Function with parameters and return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Function with default parameter
def greet(user="Guest"):
    print("Hello,", user)

greet("Thet")
greet()  # Uses default value


# Function with multiple return values
def get_name_and_age():
    return "Alice", 30

name, age = get_name_and_age()
print("Name:", name)
print("Age:", age)