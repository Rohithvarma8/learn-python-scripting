"""
Lambda Function - A lambda function in Python is a small, anonymous function defined using the lambda keyword instead of def.
    syntax:
        lambda arguements: expression

Use it when:
    1. The function is very simple (1 line).
    2. You're using it only once (e.g., for sorting, filtering).
    3. You don't want to formally define a named function with def.
Avoid when:
    1. The logic is complex (use def for readability).
    2. ou need multiple lines or statements.

Key Characteristics of Lambda
    Feature	        Value
    Name	        Anonymous (no function name)
    Return	        Automatically returns expression
    Body	        Only 1 expression allowed
    Use case	    Short, throwaway functions
    Return type	    Function object
"""
multiply_func = lambda x, y: x * y
print(multiply_func(5,3))
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(3))

"""
MAP, FILTER and SORTED

map - Applies a function to every item in an iterable (like a list) and returns a new map object (which you can convert to a list).
    properties:- 
        1. Map is a lazy iterator.
        2. It holds the instructions for how to generate the values on demand, not the values themselves.
        3. To view or use the actual values, you have to iterate over it (like with list(), for loop, or next()).
    
    initialization:-
        map(function, iterable)
"""
list_1 = [1,2,3,4]
squared_list = list(map(lambda x: x*x, list_1)) # map(lambda x: x*x, list_1) --> points to memory location since it is a lazy iterator
print(squared_list)

"""
filter - Filters out items where the function returns False — keeps only the matching ones.
    1. Same as a map - lazy iterator

    initialization:-
        filter(function, iterable)
"""
filter_list = list(filter(lambda x: x % 2 == 0, list_1 ))
print(filter_list)

"""
sorted - Sorts an iterable using a custom rule defined by a function.
    1. not a lazy iterator

    initialization:-
        sorted(iterable, ?key, ?reverse) # '?' means optional
"""

fruit_list = ["Banana", "apple", "Guava", "pear", "Dragon Fruit"]
sorted_fruits = sorted(fruit_list, key=lambda x: x.lower())
print(sorted_fruits)
sorted_fruits = sorted(fruit_list, key=lambda x: x.upper(), reverse=True)
print(sorted_fruits)
sorted_fruits = sorted(fruit_list)
print(sorted_fruits)