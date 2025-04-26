import json

'''
Parse the JSON file.
    1. Find all services across all servers that are running and have CPU usage > 30%.
    2. For each such service, extract:
    3. Server ID
    4. Service Name
    5. CPU Usage
    6. Output the results sorted by CPU usage descending.
'''
def load_json(file_path):
    with open(file_path, "r") as f:
        server_metrics_list = json.load(f)
    
    return server_metrics_list

def filter_metrics(metrics):
    for metric in metrics:
        metric["services"] = list(filter(lambda x : x["cpu"] > 30.0 and x["status"] == "running", metric["services"]))

    return metrics

def load_list_of_dict(metrics):
    res_list = list()
    for metric in metrics:
        for value in metric["services"]:
            res_dict = {
                "server_id" : metric["server_id"],
                "service" : value["name"],
                "cpu" : value["cpu"]
            }
            res_list.append(res_dict)
    
    return res_list


def write_json(list_of_dicts, file_path):
    with open(file_path,"w") as f:
        json.dump(list_of_dicts, f, indent=2)

if __name__ == "__main__":
    server_metrics = load_json("server_metrics.json")
    res_metrics = filter_metrics(server_metrics)
    res_metrics = load_list_of_dict(res_metrics)
    res_metrics = sorted(res_metrics, key= lambda x : x["cpu"], reverse=True)
    write_json(res_metrics, "res_metrics.json")