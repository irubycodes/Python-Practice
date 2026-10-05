# Functions Practice

# Basic function
def greet(name):
    print("Hello", name, "welcome to Python!")

greet("Reuben")
greet("John")
greet("Amaka")

# Return values
def add(a, b):
    return a + b

result = add(10, 5)
print(result)

# Print vs Return
def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

result1 = add_with_print(10, 5)
result2 = add_with_return(10, 5)

print("Result 1:", result1)
print("Result 2:", result2)