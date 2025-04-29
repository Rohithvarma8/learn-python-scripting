import json
'''
    Parse the JSON file.

    Focus only on incidents where:
        resolved = false
        AND severity is "high" or "critical".

    For all such incidents:
        Aggregate the total downtime per service.
        Calculate the average error rate per service.

    Output a list of services with:
        service (service name)
        total_downtime
        average_error_rate (rounded to 2 decimal places)

    Sort the output by:
    First: Descending total_downtime
    Second: Descending average_error_rate (if downtimes tie)

'''
def load_json(file_path):
    with open(file_path, "r") as f:
        logs = json.load(f)
    return logs

def filter_req_logs(logs):
    logs = list(filter(lambda x : (x["severity"] == "high" or x["severity"] == "critical") and x["resolved"] == False, logs))
    return logs

def calc_downtime_error_rate(logs):
    filtered_map = {}
    filtered_map_err = {}
    for log in logs:
        for ls in log["services"]:
            name = ls["name"]
            filtered_map[name] = filtered_map.get(name,0) + ls["downtime_minutes"]
            if filtered_map_err.get(name) == None:
                filtered_map_err[name] = [ls.get("error_rate", 0.0), 1]
            else:
                list_err = filtered_map_err.get(name)
                list_err[0] += ls.get("error_rate", 0.0)
                list_err[1] += 1
                filtered_map_err[name] = list_err
    
    for key, value in filtered_map_err.items():
        filtered_map_err[key] = round(value[0]/value[1], 2)

    return [filtered_map, filtered_map_err]


def generate_list_dicts(dicts):
    ls = []
    for key, value in dicts[0].items():
        res_dict = {
            "name" : key,
            "total_downtime": value,
            "average_error_rate" : dicts[1].get(key, 0)
        }
        ls.append(res_dict)
    return ls

def write_file(file_path, list_dict):
    with open(file_path, "w") as f:
        json.dump(list_dict, f, indent=2)


if __name__ == "__main__":
    logs = load_json("huge_incident_logs.json")
    filter_logs = filter_req_logs(logs)
    dict_1 = calc_downtime_error_rate(filter_logs)
    res_list_dict = generate_list_dicts(dict_1)
    res_list_dict = sorted(
        res_list_dict,
        key=lambda x: (x["total_downtime"], x["average_error_rate"]),
        reverse=True
    )
    write_file("res_huge_logs.json", res_list_dict)


