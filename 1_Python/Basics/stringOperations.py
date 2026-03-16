str="Hello, World!"
print(str[0])  # Output: H accessing individual characters in a string using indexing
print(str[7:12])  # Output: World slicing a string to extract a substring
print(str.upper())  # Output: HELLO, WORLD! converting a string to uppercase
print(str.lower())  # Output: hello, world! converting a string to lowercase
print(str.replace("World", "Python"))  # Output: Hello, Python! replacing a substring with another substring
print(str.split(", "))  # Output: ['Hello', 'World!'] splitting a string into a list of substrings based on a delimiter
print(str.strip("!"))  # Output: Hello, World removing leading and trailing characters from a string
print(str.find("World"))  # Output: 7 finding the index of the first occurrence of a substring in a string
print(str.count("o"))  # Output: 2 counting the number of occurrences of a substring in a string
print(str.startswith("Hello"))  # Output: True checking if a string starts with a specific substring
print(str.endswith("!"))  # Output: True checking if a string ends with a specific substring
print(str.isalpha())  # Output: False checking if all characters in a string are alphabetic
print(str.isdigit())  # Output: False checking if all characters in a string are digits
print(str.isalnum())  # Output: False checking if all characters in a string are alphanumeric
print(str.islower())  # Output: False checking if all characters in a string are lowercase
print(str.isupper())  # Output: False checking if all characters in a string are uppercase  
print(str.isspace())  # Output: False checking if all characters in a string are whitespace
print(str.center(20, "*"))  # Output: ***Hello, World!*** centering a string within a specified width and filling the remaining space with a specified character
print(str.ljust(20, "*"))  # Output: Hello, World!**** left-justifying a string within a specified width and filling the remaining space with a specified character
print(str.rjust(20, "*"))  # Output: ****Hello, World! right-justifying a string within a specified width and filling the remaining space with a specified character
print(str.zfill(20))  # Output: 000000Hello, World! padding a string with zeros on the left to fill a specified width
print(str.format("Python"))  # Output: Hello, World! formatting a string using the format() method
print(f"{str} Welcome to Python programming!")  # Output: Hello, World! Welcome to Python programming! formatting a string using an f-string (formatted string literal) 
print(str + " Welcome to Python programming!")  # Output: Hello, World! Welcome to Python programming! concatenating strings using the + operator
print(str * 2)  # Output: Hello, World!Hello, World! repeating a string using the * operator
print(len(str))  # Output: 13 getting the length of a string using the len() function
print(str[0:5])  # Output: Hello slicing a string to extract a substring using indexing
print(str[-6:])  # Output: World! slicing a string to extract a substring using negative indexing
print(str[::2])  # Output: Hlo ol! slicing a string to extract every second character
print(str[::-1])  # Output: !dlroW ,olleH slicing a string to reverse it
print(str.split())  # Output: ['Hello,', 'World!'] splitting a string into a list of substrings based on whitespace
print(str.split(", "))  # Output: ['Hello', 'World!'] splitting a string into a list of substrings based on a specific delimiter
print(str.replace("Hello", "Hi"))  # Output: Hi, World! replacing a substring with another substring using the replace() method
