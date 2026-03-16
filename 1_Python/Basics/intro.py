print("Hello, World!")
print('Python syntax can be executed directly via command line or by using a script file with the .py extension. ')

# This is a single-line comment in Python

"""This is a multi-line comment in Python.
It can span multiple lines."""

# Python is a dynamically-typed language, which means you don't need to declare variable types.
# Variables can be assigned values of any type, and the type can change during execution.
# variable names are case-sensitive and can contain letters, digits, and underscores, but cannot start with a digit.    
# Example of variable assignment
x = 10  # x is an integer   
y = "Hello"  # y is a string
z = 3.14  # z is a float
# You can also use type() to check the type of a variable
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
print(type(z))  # Output: <class 'float'>

# Python uses indentation to define blocks of code. Indentation is typically done with 4 spaces.
if x > 5:
    print("x is greater than 5")
# Python supports various data types, including:
# - int: for integers (e.g., 1, 2, 3)
# - float: for floating-point numbers (e.g., 3.14, 2.718)
# - str: for strings (e.g., "Hello", 'World')
# - bool: for boolean values (True or False)
# - list: for ordered collections of items (e.g., [1, 2, 3])
# - tuple: for ordered, immutable collections of items (e.g., (1, 2, 3))
# - dict: for key-value pairs (e.g., {"name": "Alice", "age": 30})  
# - set: for unordered collections of unique items (e.g., {1, 2, 3})

x= [4,5,3,2,1,4,5,6,7,8,9]
print(x)

for element in x:
    print(element)

y=(1,2,3,4,5,4,2,3,4,5,6,7,8,9)
#try to change the value of a tuple element
#y[0] = 10  # This will raise a TypeError because tuples are immutable
print(y)

z={"name": "Alice", "age": 30, "city": "New York"}
print(z)
print(z["name"])  # Output: Alice
print(z["age"])   # Output: 30
print(type(z))    # Output: <class 'dict'>

unique_values = set(x)
print(unique_values)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

stringlist = ["date", "fig", "grape", "apple", "banana", "cherry ", "date", "fig", "grape"]
unique_values = set(stringlist)
print(unique_values)  # Output: {'date', 'fig', 'grape', 'apple', 'banana', 'cherry '}

stringandnumbers =[ 2,5,6,1,"apple", "banana", "cherry ", 2,11, 8,"apple", "banana", "cherry "]
unique_values = set(stringandnumbers)
print(unique_values)  # Output: {1,2, 5, 6, 8, 11, 'apple', 'banana', 'cherry '}

duplicate_dict_values = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1, "a": 3}
print(duplicate_dict_values)  # Output: {'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
unique_values = set(duplicate_dict_values.values())
print(unique_values)  # Output: {1, 2, 3}

print(set("banana"))  # Output: {'b', 'a', 'n'}

