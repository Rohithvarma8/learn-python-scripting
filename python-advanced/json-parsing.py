import json

with open("data.json", "r") as f:
    data = json.load(f)

# for key, value in data.items():
#     print(f"{key} is mapped to ---> {value}")

for key, value in data.items():
    if isinstance(value, dict):
        for key_1, val_1 in value.items():
            print(f"{key}-----> {key_1} --> {val_1}")
    
    elif isinstance(value,list):
        for vals in value:
            print(f"{key} --> {vals}")

    else:
        print(f"{key} --> {value}")
