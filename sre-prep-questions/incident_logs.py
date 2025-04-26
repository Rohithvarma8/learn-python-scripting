import json

'''
Parse the JSON file.
    1.  For only high and critical severity incidents:
    2.  Collect the total downtime (sum of downtime_minutes) per service.
    3.  Create a list of services showing:
        i. Service Name
        ii. Total Downtime Across Incidents
    4.  Sort the output by downtime descending.
'''

def load_json(path_file):
    with open(path_file, "r") as f:
        list_dict = json.load(f)
    return list_dict

def filter_log_incident(logs):
    logs = list(filter(lambda x : x["severity"] == "high" or x["severity"] == "critical", logs))
    return logs

def write_load_json(file_name, list_dict):
    with open(file_name, "w") as f:
        json.dump(list_dict, f, indent=2)

def add_all_downtimes(logs):
    downtime_map = {}
    for log in logs:
        for service in log["services_impacted"]:
            name = service["name"]
            downtime_map[name] = downtime_map.get(name, 0) + service["downtime_minutes"]

    # Now create list of dicts
    list_dict = [{"service": name, "total_downtime": downtime} for name, downtime in downtime_map.items()]
    return list_dict

if __name__ == "__main__":
    incident_logs = load_json("incident_logs.json")
    filter_logs = filter_log_incident(incident_logs)
    filter_logs = add_all_downtimes(filter_logs)
    filter_logs = sorted(filter_logs, key= lambda x : x["total_downtime"], reverse=True)
    write_load_json("filter_logs.json",filter_logs)

    
