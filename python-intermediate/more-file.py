with open("person.txt", "r") as f:
    for line in f:
        print(line.strip()) # prints line by line

# with open("person.txt", "r") as f:
#     lines = f.readlines()
#     print(lines) # prints the text file as a list

lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("data.txt", "a") as f:
    f.writelines(lines)

# if you want to read and write at once you can use r+

"""
# Use full path
with open("/home/user/logs/log.txt", "r") as f:
    ...

# Or use relative paths
with open("logs/today.txt", "r") as f:
    ...
"""
with open("./../python-basics/date.txt", "x") as f:
    pass

