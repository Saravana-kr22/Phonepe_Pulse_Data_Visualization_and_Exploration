import json
import re
import pandas as pd


def aggregated_data(data):

    path = ""
    data_option = data['data_option'].lower()
    quater = data["quater"]
    quater = re.findall(r'\d+', quater)
    quater =quater[:4][0]
    if data["state"]== "All-India":
        path = f"pulse/data/aggregated/{data_option}/country/india/{data['year']}/{quater}.json"
    else:
        state = data["state"].lower()
        path = f"pulse/data/aggregated/{data_option}/country/india/state/{state}/{data['year']}/{quater}.json"
    
    if data_option == "transaction":
        return tranction_data(path)
    elif data_option == "user":
        return user_data(path)
    else:
        return incurance_data(path)


def tranction_data(path):
    agg_data = open(path)
    agg_data = json.load(agg_data)
    agg_data = agg_data['data']["transactionData"]
    rows = []
    for transaction in agg_data:
        name = transaction["name"]
        count = transaction["paymentInstruments"][0]["count"]
        amount = transaction["paymentInstruments"][0]["amount"]
        amount = int(amount)  # Format amount to have commas and 2 decimal places
        rows.append({"name": name, "Count": count, "Amount": amount})
    agg_data = pd.DataFrame(rows)
    return agg_data


def user_data(path):
    agg_data = open(path)
    agg_data = json.load(agg_data)
    agg_data1 = agg_data['data']["aggregated"]
    rows = []
    agg_data = agg_data['data']['usersByDevice']
    if agg_data == None:
        return agg_data1
    reg_user = agg_data1["registeredUsers"]
    app_open = agg_data1["appOpens"]
    rows.append({"registeredUsers": reg_user, "appOpens": app_open, "brand": "Nil", "count": "Nil","percentage":"Nil"})
    for transaction in agg_data:
        brand = transaction["brand"]
        count = transaction["count"]
        percentage = transaction["percentage"]
        rows.append({"registeredUsers": reg_user, "appOpens": app_open, "brand": brand, "count": count,"percentage":percentage})
    agg_data = pd.DataFrame(rows)
    return agg_data

def incurance_data(path):
    agg_data = open(path)
    agg_data = json.load(agg_data)
    agg_data = agg_data['data']["transactionData"][0]
    return agg_data