import json
'''
Write a Python script to:
    1. Parse the JSON file.
    2. Identify all 500-level errors.
    3. For each error, extract:
    4. The IP address
    5. The URL that caused it
    6. The response time
    7. Return a sorted list of these errors by descending response time.
'''
def load_json(json_file_path):
    with open(json_file_path, "r") as f:
        traffic = json.load(f)
    return traffic

def filter_traffic_status(traffic_list, status_code):
    for logs in traffic_list:
        logs["desired_status"] = list(filter(lambda x : x["status"] == status_code, logs["requests"]))

    return traffic_list

def create_desired_list(logs):
    res_list = []
    for log in logs:
        for status_log in log["desired_status"]:
            res_dict = {
                "ip": log["ip"],
                "url": status_log["url"],
                "response_time": status_log["response_time"]
            }
            res_list.append(res_dict)
    return res_list

def create_json(list_of_dict, file_path):
    with open(file_path, "w") as f:
        json.dump(list_of_dict, f, indent=4)        
        


if __name__ == "__main__":
    traffic = load_json("traffic_logs.json")
    req_status_list = filter_traffic_status(traffic, 500)
    desired_dict = create_desired_list(req_status_list)
    create_json(sorted(desired_dict,key= lambda x : x["response_time"], reverse=True), "result_traffic.json")
