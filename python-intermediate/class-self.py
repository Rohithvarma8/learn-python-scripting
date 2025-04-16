"""
def __init__(self,..) is kind of similar to constructor in java

self --> this keyword
"""

class Person:
    def __init__(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print("Person Details")
        print("- name:", self.name)
        print("- age:", self.age)
        print("- gender:", self.gender)


p = Person("Rohith", 22, "M")

p.print_details() 
