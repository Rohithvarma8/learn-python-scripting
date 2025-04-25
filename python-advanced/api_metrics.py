import json

'''
Load the JSON file.
    1. For each API endpoint, calculate the average response time.
    2. Print the top 2 endpoints with the highest average response time, in descending order.
'''
def load_json(api_data_path):
    with open(api_data_path, "r") as f:
        api_data = json.load(f)
    return api_data

def highest_api_endpoint(api_metrics):
    list_1 = [-1, -1]
    endpoint_list = []
    for api in api_metrics:
        api_avg_res_time = calc_avg_res_time(api["response_times"])
        if api_avg_res_time > list_1[0]:
            temp = list_1[0]
            endpoint_list.insert(0,api["endpoint"])
            list_1[0] = api_avg_res_time
            if temp == list_1[1] and temp != -1:
                list_1.append(temp)
                endpoint_list.append(api["endpoint"])
            else:
                list_1 = list_1[0:1]
                endpoint_list = endpoint_list[0:1]
                endpoint_list.append(api["endpoint"])
                list_1.append(temp)
        elif api_avg_res_time > list_1[1]:
            list_1 = list_1[0:1]
            endpoint_list = endpoint_list[0:1]
            endpoint_list.append(api["endpoint"])
            list_1.append(api_avg_res_time)
        elif api_avg_res_time == list_1[1]:
            endpoint_list.append(api["endpoint"])
            list_1.append(api_avg_res_time)
        else:
            pass
    return endpoint_list



def calc_avg_res_time(res_times):
    l_size = len(res_times)
    count = 0
    for t in res_times:
        count += t
    return count/l_size

if __name__ == "__main__":
    api_metrics = load_json("api_metrics.json")
    res_time = highest_api_endpoint(api_metrics)
    print(res_time)


