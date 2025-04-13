"""
data structures is nothing but structuring the data and storing it in structured manner with set of its own functionalities
In this we are going to look at following data structures
    1. List
    2. Tuple
    3. Set
    4. Dict

Before gettint to know more about data structures we will know the terminolgy of their properties
    1. ordered - The elements in that particular data structure maintain the order in which they were added.
    2. mutable - You can change the data structure after it's created (add, remove and change exsisting value in the data structure)
    3. duplicates - Having same value multiple times in the data structure
    4. indexing - You can access a value with its positon in the data structure
"""
# Lists and its Types
"""
List - A list is a built-in Python data structure that allows you to store a collection of items. Python lists can store mixed data types, grow dynamically, and offer rich built-in functionality.
    1. ordered - Yes (items have a fixed position)
    2. mutable - Yes (you can change, add, remove items)
    3. duplicates - Allowed
    4. indexed - Yes (access using position)

Initializing a list:
    1. [] --> is used t
    2. can also use list() method
"""
greet = list("hello")
number_list = [10, 20, 20, 30, 40, 40]
mixed_list = [10, 20, "Rohith", True]
nested_list = [[1,2,3], [1,2]]
print(greet)
print(number_list)
print(mixed_list)
print(nested_list)
# slicing [start:stop:step]
print(number_list[0])
print(number_list[1:3]) # 20 20
print(number_list[:3]) # 10 20 20
print(number_list[::2]) # 10 20 40
"""
Types of Lists
    1. Homogeneous list: same data type
    2. Heterogeneous list: mixed data types
    3. Nested list: list within a list
"""
# built-in method for list
fruit_list = ["banana", "apple", "mango"]
fruit_list.append("orange") # append objects to the end of the list -- o(1)
print(fruit_list.count("banana")) # returns no of occurences -- o(n)
fruit_list.insert(0, "guava") # (postition , value) -- o(n)
print(fruit_list)
last = fruit_list.pop() # removes last value and returns it -- o(1)
print(last)
fruit_list.sort() # o(nlogn)
print(fruit_list)
fruit_list.reverse() # o(n)
print(fruit_list)

