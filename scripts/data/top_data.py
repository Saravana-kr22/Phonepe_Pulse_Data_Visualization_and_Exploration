import json
import re
import pandas as pd

def top10_data(data):
    path = ""
    data_option = data['data_option'].lower()
    quater = data["quater"]
    quater = re.findall(r'\d+', quater)
    quater =quater[:4][0]
    if data["state"]== "All-India":
        path = f"pulse/data/top/{data_option}/country/india/{data['year']}/{quater}.json"
    else:
        state = data["state"].lower()
        path = f"pulse/data/top/{data_option}/country/india/state/{state}/{data['year']}/{quater}.json"
    if data_option == "transaction":
        return tranction_data(path, data["top_data"])
    elif data_option == "user":
        return user_data(path, data["top_data"])
    else:
        return incurance_data(path, data["top_data"])
    
def tranction_data(path, option):
    top_data = open(path)
    top_data = json.load(top_data)
    option = option.lower()+"s"
    top_data = top_data['data'][option]
    rows = []
    for entry in top_data:
        name = entry["entityName"]
        count = entry["metric"]["count"]
        amount = entry["metric"]["amount"]
        amount = int(amount)  # Format amount to have commas and 2 decimal places
        rows.append({"name": name, "Count": count, "Amount": amount})
    top_data = pd.DataFrame(rows)
    top_data = top_data[["name","Count"]].reset_index(drop=True)
    return top_data


def user_data(path, option):
    top_data = open(path)
    top_data = json.load(top_data)
    option = option.lower()+"s"
    top_data = top_data['data'][option]
    rows = []
    for entry in top_data:
        name = entry["name"]
        reg_user = entry["registeredUsers"]
        rows.append({"name": name, "registeredUsers" : reg_user})
    top_data = pd.DataFrame(rows)
    return top_data

def incurance_data(path ,option):
    top_data = open(path)
    top_data = json.load(top_data)
    option = option.lower()+"s"
    top_data = top_data['data'][option]
    rows = []
    for entry in top_data:
        name = entry["entityName"]
        count = entry["metric"]["count"]
        amount = entry["metric"]["amount"]
        amount = int(amount)  # Format amount to have commas and 2 decimal places
        rows.append({"name": name, "Count": count, "Amount": amount})
    top_data = pd.DataFrame(rows)
    top_data = top_data[["name","Count"]].reset_index(drop=True)
    return top_data
