import pandas as pd
import json
import re

def hover_data(data):
    path = ""
    data_option = data['data_option'].lower()
    quater = data["quater"]
    quater = re.findall(r'\d+', quater)
    quater =quater[:4][0]
    if data["state"]== "All-India":
        path = f"pulse/data/map/{data_option}/hover/country/india/{data['year']}/{quater}.json"
    else:
        state = data["state"].lower()
        path = f"pulse/data/map/{data_option}/hover/country/india/state/{state}/{data['year']}/{quater}.json"
    if data_option == "transaction":
        return tranction_data(path)
    elif data_option == "user":
        return user_data(path)
    else:
        return incurance_data(path)
    
def tranction_data(path):
    hover_data = open(path)
    hover_data = json.load(hover_data)
    hover_data = hover_data['data']["hoverDataList"]
    rows = []
    for entry in hover_data:
        name = entry["name"]
        if "state" in path:
            name = str(name).replace("district", "")\
                            .replace(" ","")
        name = str(name).replace(" ", "-")
        name =name.title()
        count = entry["metric"][0]["count"]
        amount = entry["metric"][0]["amount"]
        amount = int(amount)  
        avg = amount/int(count)
        count = '{:,.2f}'.format(count)
        amount = '{:,.2f}'.format(amount)
        amount = '₹'+ str(amount)
        avg = '{:,.2f}'.format(avg)
        avg = '₹'+ str(avg)
        rows.append({"ST_NM": name, "Count": count, "Amount": amount, "Avg":avg})
    agg_data = pd.DataFrame(rows)
    return agg_data


def user_data(path):
    hover_data = open(path)
    hover_data = json.load(hover_data)
    hover_data = hover_data['data']["hoverData"]
    rows = []
    for entry in list(hover_data.keys()):
        name = entry
        if "state" in path:
            name = str(name).replace("district", "")\
                            .replace(" ","")
        name = str(name).replace(" ", "-")
        name =name.title()
        reg_user = hover_data[entry]["registeredUsers"]
        reg_user = '{:,.2f}'.format(reg_user)
        app_open = hover_data[entry]["appOpens"]
        app_open = '{:,.2f}'.format(app_open)
        rows.append({"ST_NM": name, "registeredUsers" : reg_user, "appOpens":app_open})
    hover_data = pd.DataFrame(rows)
    return hover_data

def incurance_data(path ):
    hover_data = open(path)
    hover_data = json.load(hover_data)
    hover_data = hover_data['data']["hoverDataList"]
    rows = []
    for entry in hover_data:
        name = entry["name"]
        if "state" in path:
            name = str(name).replace("district", "")\
                            .replace(" ","")
        name = str(name).replace(" ", "-")
        name =name.title()
        count = entry["metric"][0]["count"]
        amount = entry["metric"][0]["amount"]
        amount = int(amount)  
        avg = amount/int(count)
        count = '{:,.2f}'.format(count)
        amount = '{:,.2f}'.format(amount)
        amount = '₹'+ str(amount)
        avg = '{:,.2f}'.format(avg)
        avg = '₹'+ str(avg)
        rows.append({"ST_NM": name, "Count": count, "Amount": amount, "Avg":avg})
    agg_data = pd.DataFrame(rows)
    return agg_data
