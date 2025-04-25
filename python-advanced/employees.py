'''
Write a Python script to:
    1. Load this JSON file.
    2. Print the names of all employees in the Engineering department.
'''
import json

def read_and_load_json(path_of_json_file):
    with open(path_of_json_file, "r") as f:
        ret_val = json.load(f)
    return ret_val

def find_filter(emp_data, target):
    for employee in emp_data:
        if employee["department"].strip().lower() == target.strip().lower():
            print(employee["name"])
    



if __name__ == "__main__":
    var1 = read_and_load_json("employees.json")
    find_filter(var1, "engineering")
