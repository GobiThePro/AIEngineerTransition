#boolean examples
print(5 > 3)  # Output: True comparing two numbers using the greater than operator
print(2 < 1)  # Output: False comparing two numbers using the less than operator
print(bool("python"))  # Output: True converting a non-empty string to a boolean value
print(bool(""))  # Output: False converting an empty string to a boolean value
print(bool(0))  # Output: False converting the number 0 to a boolean value
print(bool(1))  # Output: True converting the number 1 to a boolean value
print(bool([]))  # Output: False converting an empty list to a boolean value
print(bool([1, 2, 3]))  # Output: True converting a non-empty list to a boolean value
print(bool(None))  # Output: False converting the None value to a boolean value

class Person:
    def __len__(self):
        return 0;  # Output: None defining a class with an __init__ method that does not return anything
person = Person()

print(bool(person))  # Output: True converting an instance of a class to a boolean value (non-empty object is considered True)

print(isinstance(30,int))  # Output: True checking if a value is an instance of a specific type (integer in this case)
print(isinstance("Hello", str))  # Output: True checking if a value is an instance of a specific type (string in this case)