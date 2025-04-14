"""
Python uses try-except blocks to catch and handle exceptions gracefully without crashing the program. You can also use else for code that runs if no error occurs, and finally for cleanup code that runs no matter what.
    1. try-except-finally blocks
    2. raise
"""
# 1
try:
    user_input = int(input("Enter a number:"))
    print(user_input)
except ValueError:
    print("Please entry should be a Interger")
finally:
    print("no matter what i always run")

def get_value_by_key(dict_obj, key):
    try:
        return dict_obj[key] # if use get(key) and there is such key it returns none but this throws you a error 
    except KeyError:
        print(f"couldn't find key that matches '{key}' in the dictionary")
        return None

roommates_info = {
    "people_count" : 7,
    "sharing_person" : "Kalyan",
}  
get_value_by_key(roommates_info, "Bathrooms")

def set_age(age):
    if age <= 0:
        raise ValueError(" age is a positive number please enter a positive number!!!")
    return age

try:
    person_age = set_age(user_input)
    print(person_age)
except ValueError as e:
    print(e)

"""
Most used Types of exception errors
    1. ZeroDivisionError - Occurs when dividing by zero.
    2. ValueError - Occurs when a function gets an argument of the right type but an inappropriate value.
    3. TypeError - Happens when an operation is applied to an object of inappropriate type.
    4. IndexError - Occurs when accessing an index that doesn't exist in a list.
    5. KeyError - Happens when trying to access a dictionary with a key that doesn't exist.
"""