"""
How memory works in pyhton:

In Python, the input() function always returns a string — no matter what the user types.
    Even if the user types 42, user_input will be '42' (a string), not the integer 42.

In Python, variables are names (or labels) that point to objects stored in memory — kind of like a tag attached to a box.
    x = 5
        1. Python creates an integer object with the value 5 in memory.
        2. The name x is created and made to point to that object.
    x = "hello"
        3. Think of x as a sticky note labeled "x" that you put on a box. The box holds the number 5. If you later write: "hello"
        4. Now it just points at a different box
Behind the scenes
        1. Python stores objects in heap memory.
        2. Variable names are stored in a namespace (like a dictionary).
        3. Python keeps track of how many variables (or things) point to an object — this is called reference counting.
    a = 10
    b = a
        4. Both a and b now point to the same object: the integer 10.
        5. No new memory is used for b unless you change 
"""

#functions in python (base level)

# function with no parameters
def say_hello():
    print("Hello There!!")

say_hello()

# function with parameters
def print_name(name):
    print("My name is", name)

print_name("rohith")

"""
    You can also give default values in a method with parameter so when no parameters are given it takes default values
"""
#function with parameter and has a default value
def print_default_name(name="Nikhil"):
    print("[default demo] My name is", name)

print_default_name("Rohith")
print_default_name()

#function with return value
def sum_two_numbers(c,d):
    return c + d
a = 5
b = 6
result = sum_two_numbers(a,b)
print("a + b =", result)

# nested functions
def outer():
    def inner():
        print("I'm in inner")
    inner()
    print("I'm in Outer")

outer()

# FUnction as First class citizens
def sum_two(a,b):
    return a + b
def diff_two(a,b):
    return a - b
def operate_two_nums(func, a, b):
    return func(a,b)
result = operate_two_nums(sum_two, 5, 4)
print("result is:", result)
result = operate_two_nums(diff_two,5,4)
print("result is:", result)

"""
More About Nested Function in python
    Sterting from What is a Nested Function - As the name suggests it is a function in a function
    Why use them?
        1. Encapsulation: Inner function is hidden and only used inside the outer one.
        2. Logical grouping: When a helper is only needed inside another function.
        3. Closures: (More advanced) Inner function can remember variables from outer function.
"""

def say_hello(name):
    def send_greet():
        return f"Hi {name}!"
    return send_greet()

print(say_hello("Harshini")) # The f in an f-string stands for "formatted" — it tells Python to evaluate the expressions inside curly braces {} and insert their values into the string.

"""
More about first class citizens in python
    What does that mean?
        In Python, functions are first-class citizens, meaning:
            1. You can assign them to variables.
            2. You can pass them as arguments.
            3. You can return them from other functions.
"""
def greet(func, name):
    return func(name)

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

big  = greet(shout, "i have a dream")
print(big)
small = greet(whisper, "and Also I Have a secret")
print(small)

"""
Closures in python
    A closure is a function that remembers and uses variables from an enclosing scope even after the outer function has finished executing.

        Nested + first class = closures

    Think of it like this:
        You're packing a function in a box, and it carries the surrounding context with it — even after the original scope is gone.
"""

# using closures effectively in real-life scenario if want to create funtion that can be reused multiple times with different functionality

def power_num(x):
    def base_num(n):
        return n ** x
    return base_num

square = power_num(2)
cube = power_num(3)

print(square(5))
print(cube(5))


