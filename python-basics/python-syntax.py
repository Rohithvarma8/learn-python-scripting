# hey if you want learn python then this can help you through your journey 
# you will use HASHTAG to write comment in python file
# Multi-line comment is demonstrated below


"""
    This is a multi-line comment
    More About Python:-
        Python is an interpreted language, which means you write code in text files (usually with a .py extension), and the Python interpreter runs your code line by line.
        A Python script is simply a file containing a series of Python statements. When the script is running, the interpreter processes the code sequentially from top to bottom.
"""

# Printing a String in Python
print("Hello World")

# Data types
# Python is a Dynamically typed language so you do not need to declare the data type of the variable
number = 5
pi = 3.14
name = "Rohith"
age = 7
# In python prefer using snake case
is_male = True # T should be capital

# printing variable in python 
print(number)
print(pi)
# string and variables in a print statement
print("My name is", name,"and my age is", age)

# Basic I/O UNCOMMENT THESE
# user_input = input("Enter a Number: ")
# # Type Conversion 
# person_age = int(user_input) # input is taken as a string
# print(person_age)

"""
Indentation in python:- 
    Indentation is Mandatory: In Python, blocks of code are defined by indentation instead of the braces {} you might see in other languages.
    Standard Practice: Typically, you use 4 spaces per indentation level. Consistency is key: mixing tabs and spaces can lead to errors.
"""

# Control Flow Statments

# Indentation Demo
if True:
    print("I'm in the if statement")
print("I'm out of if statement")
# conditional if-else
if number > 0:
    print("I'm greater than 0")
elif number == 0:
    print("I'm equal to 0")
else:
    print("I'm less than 0")

# Loops
for i in range(5):
    print("iteration:", i)

count = 0
while count < 5:
    print("Count incremented by 1 and the current count is :", count)
    count += 1

# Operators in python 
a = 5 
b = 9
# a = "r"
# b = "ohith" concatenates two strings gives rohith as output
c = a + b
print("Sum is", c)

# Basic Functions in python 
"""
This is a multi-line string.
It is often used as a docstring(Document String) in functions, classes, or modules.
"""
def learn_functions():
    return "You just called a function"

print(learn_functions())