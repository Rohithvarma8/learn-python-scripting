"""
Dict --> It is more like HashMap in Java stores key-value pair. Dict is a short form for dictionary
A dictionary (dict) in Python is a key-value pairs, where each key is unique and maps to a value.
    1. Ordered - Yes (since Python 3.7+)
    2. Mutable - Yes
    3. Indexed by Keys (not numeric index)
    4. Duplicates - Keys must be unique
    5. Values - Can be of any type

How to Initialize a dict
    1. {} --> empty dict
    2. dict() funtion is used to create a dict
"""
employee_details = {
    "name": "Rohith",
    "role": "SRE Intern", # can leave a leading comma
    "company": "DraftKings",
    "location": "Boston",
}
print(employee_details)
interview_result = dict(hired=True, offer_status="Accepted")
print(interview_result)
# Above dicts are simple dicts below given is a nested dict
personal_resume = {
    "name" : "Rohith",
    "age" : 23,
    "skills" : {
        "lang" : ["Python", "Java", "JavaScript"],
        "Tools" : ["Terraform", "VS code"],
    },
    "matching_jd" : True,
}
print(personal_resume)
"""
Method	        Description	                                Example
get(key)	    Returns value or None (safe access)	        d.get("key")
keys()	        Returns all keys	                        d.keys()
values()	    Returns all values	                        d.values()
items()	        Returns list of (key, value) tuples         d.items()
update()	    Adds or updates multiple items	            d.update({"env": "prod"})
pop(key)	    Removes key and returns value	            d.pop("role")
clear()	        Removes all items                       	d.clear()
in	            Checks if key exists	                    "name" in d
"""
for key, value in personal_resume.items():
    if isinstance(value, dict): # type(value) == dict works but not recommended
        for key, value in value.items():
            print(key,"-->", value)
    else:
        print(key,"-->", value)

for key, value in personal_resume.items():
    print(key,"-->", value)
server = {
    "hostname": "web01",
    "ip": "192.168.1.10",
    "status": "active",
}

# Access
print(server["ip"])           # 192.168.1.10
print(server.get("role"))     # None (safe)

# Add/update
server["os"] = "Linux"
server.update({"role": "backend"})

is_exsist = "os" in server
print(is_exsist)
"""
Operation	    Complexity
Get / Set	    O(1)
Delete	        O(1)
Iterate (all)	O(n)
"""