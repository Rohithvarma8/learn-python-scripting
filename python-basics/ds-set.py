"""
Set - In Python is an unordered, mutable collection of unique elements, meaning it automatically removes duplicates and doesn't keep order
    1. Ordered	- No (elements are unordered)
    2. Mutable	- Yes (can add/remove elements)
    3. Indexed	- No (no indexing/slicing)
    4. Duplicates - Not allowed
    5. Heterogeneous - Yes (mix of types allowed)
Intializing a set
    1. {}
    2. can also initialize a set using set() function
"""
# Empty set (must use set(), not {}) {} --> is a dict not a set
empty_set = set()

number_set = {1, 2, 3}
print(number_set)
s = set([1, 2, 3])
print(s)
s1 = set("Rohith")
print(s1) # will not be in order
# Frozen Set 
fs_number = frozenset([1, 2, 3]) # acts like a tuple and set now add and remove functionality
"""
Method	            Description	                                Example
add(x)	            Adds x to the set	                        s.add(10)
update(iterable)	Adds multiple items	                        s.update([11, 12])
remove(x)	        Removes x (error if not found)	            s.remove(2)
discard(x)	        Removes x (no error if not found)	        s.discard(99)
pop()	            Removes and returns an arbitrary element	s.pop()
clear()	            Empties the set	                            s.clear()
"""
number_set.add(25)
number_set.add(25)
print(number_set)
number_set.discard(25)
pop_element = number_set.pop() 
print(pop_element) # removes the first element in number_set
print(number_set)
number_set.add(25)
number_set.add(35)
"""
Using Set you can do math related Set operations
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
        Operation	                Result
        a.union(b)	                {1, 2, 3, 4, 5, 6}
        a.intersection(b)	        {3, 4}
        a.difference(b)	            {1, 2} (a - b)
        a.symmetric_difference(b)	{1, 2, 5, 6}
"""
# looping through a set
for item in number_set:
    print(item)
# Conditional Statements with sets
if 25 in number_set:
    print("Yes")