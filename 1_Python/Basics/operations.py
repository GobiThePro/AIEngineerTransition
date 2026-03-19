# Basic arithmetic operations in Python
from itertools import count


print(5 + 3)  # Output: 8 adding two numbers
print(10 - 4)  # Output: 6 subtracting one number from another
print(6 * 7)  # Output: 42 multiplying two numbers
print(20 / 5)  # Output: 4.0 dividing one number by another (result is a float)
print(10 // 3)  # Output: 3 floor division (result is an integer)
print(2 ** 3)  # Output: 8 exponentiation (raising a number to the power of another number)
print(10 % 3)  # Output: 1 modulus (remainder of the division of one number by another)

#assignment operators
x = 15
x += 3  # Output: 18 equivalent to x = x + 3
x -= 2  # Output: 16 equivalent to x = x - 2
x *= 4  # Output: 64 equivalent to x = x * 4
x /= 6  # Output: 10.666666666666666 equivalent to x = x / 6
x //= 2  # Output: 5.0 equivalent to x = x // 2
x **= 3  # Output: 8.0 equivalent to x = x ** 3
x %= 5  # Output: 3.0 equivalent to x = x % 5   
#x &= 2  # Output: 2 equivalent to x = x & 2 (bitwise AND assignment)
#x |= 1  # Output: 3 equivalent to x = x | 1 (bitwise OR assignment)
#x ^= 1  # Output: 2 equivalent to x = x ^ 1 (bitwise XOR assignment)
#x <<= 1  # Output: 4 equivalent to x = x << 1 (bitwise left shift assignment)
#x >>= 1  # Output: 2 equivalent to x = x >> 1 (bitwise right shift assignment)  

y=[1, 2, 3]
 # Output: False using the walrus operator (:=) to assign a value to a variable as part of an expression
if(count:=len(y))<4:
    print(count)

y=23
# comparison operators
print(y == 23)  # Output: True checking if two values are equal
print(y != 10)  # Output: True checking if two values are not equal 
print(y > 20)  # Output: True checking if one value is greater than another
print(y < 30)  # Output: True checking if one value is less than another
print(y >= 23)  # Output: True checking if one value is greater than or
print(y <= 25)  # Output: True checking if one value is less than or equal to another

#logical operators
print(y > 20 and y < 30)  # Output: True checking if both conditions are true using the logical AND operator
print(y < 20 or y > 30)  # Output: False checking if at least one condition is true using the logical OR operator
print(not(y > 20))  # Output: False checking if a condition is not true using the logical NOT operator

#identity operators
print(y is 23)  # Output: True checking if two variables refer to the same object in memory using the identity operator 'is'
print(y is not 10)  # Output: True checking if two variables do not refer to the same object in memory using the identity operator 'is not'

xy=["a", "b", "c"]
yz = ["a", "b", "c"]
print(xy == yz)  # Output: True checking if the values of xy and yz are equal using the equality operator '=='
print(xy is yz)  # Output: False checking if xy and yz refer to the same object in memory using the identity operator 'is' (lists are not cached by Python, so xy and yz refer to different objects)
print(xy is not yz)  # Output: True checking if xy and yz do not refer to the same object in memory using the identity operator 'is not'

#Difference between '==' and 'is'
# The '==' operator checks for value equality, meaning it checks if the values of the objects being compared are equal.
# In contrast, the 'is' operator checks for identity, meaning it checks if the two operands refer to the same object in memory. Therefore, two different objects with the same value will be considered equal by '==', but they will not be considered identical by 'is'.


#membership operators
print("a" in xy)  # Output: True checking if the value "a" is present in the list xy using the membership operator 'in'
print("d" not in xy)  # Output: True checking if the value "d" is not present in the list xy using the membership operator 'not in'
