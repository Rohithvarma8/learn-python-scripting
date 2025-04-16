"""
In this file I'm going to demo why we need dunder main refer script - 2 for next steps
"""
def do_something():
    print(f"I am Studying and this is running from {__name__} ")

# do_something()  
"""
if you use this(above command) I am studying will print two times
__name__ attribute will be printed as __main__  if you run script1 
and it will print "script1" if you run script2 
in-order to eliminate these issues we will use the below functionality
"""

if __name__ == "__main__":
    do_something()

"""
only runs the do_something when you run script1
"""    