"""
tuple - It is a data structure to store collection of items
    1. Ordered - Yes
    2. Mutable - No
    3. Indexed - Yes
    4. duolicates - Yes

initailizing a tuple
    1. () 
    2. use tuple() function
"""

my_tuple  = (1, 2, 4, 4)
print(my_tuple)
number_tuple = tuple([1,2,3])
print(number_tuple)
# Without parentheses (comma is what makes it a tuple)
t = 1, 2, 3, 4, 4
# Single-element tuple (needs comma!)
t1 = (5,)     # Valid
t2 = (5)      # Just an integer, not a tuple
print(type(t))
print(type(t1))
print(type(t2))
"""
Types of Tuples
    1. Homogeneous: same data types
        t = (1, 2, 3, 4)

    2. Heterogeneous: mixed types
        t = (1, "log", True, 2.5)

    3. Nested Tuple: tuple inside a tuple
        t = ((1, 2), (3, 4))

    4. Tuple of lists / List of tuples:
        t = ([1, 2], [3, 4])  --> Mutable elements
        l = [(1, 2), (3, 4)]
"""
print(t.count(4)) # Returna no of occurencees of 4
print(t.index(4)) # Returns first index of 4
print(t[-1])      # Returns last value in a tuple always think every data structure is circular

# Packing and Unpacking a tuple 

info = ("Rohith", 18, True) # packing
name, age, is_male = info # Unpacking
print(name, age, is_male)
"""
Why Use Tuples?
    1. Faster than lists due to immutability.
    2. Safe from modification (good for constants/configs).
    3. Used as dictionary keys (lists can't be, because they're mutable).
    4. Common for returning multiple values from functions.
"""