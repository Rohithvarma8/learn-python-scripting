import json

def load_json(json_file_path):
    with open(json_file_path, "r") as f:
        api_dict_list = json.load(f)
    
    return api_dict_list

def calc_average(res_times):
    no_of_res = len(res_times)
    count = 0
    for response in res_times:
        count += response   
    return count/no_of_res

def top_api_res(api_metrics):
    for api in api_metrics:
        api["average_response_times"] = calc_average(api["response_times"])
    sorted_metrics = sorted(api_metrics, key=lambda x : x["average_response_times"], reverse= True)
    return sorted_metrics

def list_of_top_api(res_list, second_highest):
    count = 0 
    for res in res_list:
        if second_highest == res["average_response_times"]:
            count += 1
        else:
            break
    return count

def print_endpoint(res_list):
    for res in res_list:
        print(res["endpoint"])
    
if __name__ == "__main__":
    api_metrics = load_json("api_metrics.json")
    res_api = top_api_res(api_metrics)
    step_of_list = 2 + list_of_top_api(res_api[2:], res_api[1]["average_response_times"])  
    print_endpoint(res_api[:step_of_list])

    
     
