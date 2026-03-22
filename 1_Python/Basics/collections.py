#List - List is a collection of items which is ordered and changeable. It allows duplicate members.
#List is defined by using square brackets [] and items are separated by commas.
listexample = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(listexample)  # Output: [1, 2, 3, 4, 5, 4, 3, 2, 1]
for element in listexample:
    print(element)

listexample[0] = 10  # Change the first element to 10
listexample.insert(2, 10)  # Insert 10 at index 2
listexample.append(20)  # Append 20 to the end of the list

# Remove elements from the list
listexample.remove(4)  # Remove the first occurrence of 4
listexample.pop(3)  # Remove the element at index 3
del listexample[4]  # Remove the element at index 4

listexample2 = [6, 7, 8, 9, 10]
# Extend the list with another list. not only adds the elements of the second list but also modifies the original list.
listexample.extend(listexample2) 

tupleexample = (1, 2, 3, 4, 5, 4, 3, 2, 1)
# Extend the list with a tuple. not only adds the elements of the tuple but also modifies the original list.  
#tuples,sets and dictionaries can be extended to a list using the extend() method, which adds the elements of the tuple, set or dictionary to the end of the list.  
listexample.extend(tupleexample)  


print(listexample)  # Output: [10, 2, 10, 3, 5, 4, 3, 2, 1, 20, 6, 7, 8, 9, 10]

listexample.clear()  # Clear all elements from the list
print(listexample)  # Output: []


#Tuple - Tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
#Tuple is defined by using parentheses () and items are separated by commas.
#Dictionary - Dictionary is a collection of key-value pairs which is unordered, changeable and indexed. It does not allow duplicate members.
#Dictionary is defined by using curly braces {} and key-value pairs are separated by commas. The
#key and value are separated by a colon :.
#Set - Set is a collection of items which is unordered and unindexed. It does not allow duplicate members.
#Set is defined by using curly braces {} and items are separated by commas. It can also be defined by using the set() constructor.
