import pandas as pd
import numpy as np
import random
from scripts.data.top_data import top10_data

def add_hexa_value(hexagondata, info_dict):
    info_dict["top_data"] = "Pincode"
    top10_pincode = read_top_data(info_dict, hexagondata)
    info_dict["top_data"] = "District"
    top10_state = read_top_data(info_dict, hexagondata)
    min_values = [900,3208, 2454, 9110, 4180]
    if info_dict["data_option"] == "User":
        max_value = top10_pincode["registeredUsers"].max()
        top10_state = top10_state.set_index('name')['registeredUsers'].to_dict()
        top10_pincode = top10_pincode.set_index('name')['registeredUsers'].to_dict()
    else:
        max_value = top10_pincode["Count"].max()
        top10_state = top10_state.set_index('name')['Count'].to_dict()
        top10_pincode = top10_pincode.set_index('name')['Count'].to_dict()
    min_value = random.choice(min_values)
    hexagondata['val'] = np.random.randint(min_value, max_value + 1, len(hexagondata["postal code"]))
    for district in list(top10_state.keys()):
        min_value = random.choice(min_values)
        hexagondata_d =  hexagondata[hexagondata.province_or_county == district]
        total = top10_state[district]
        np.random.seed(0)  # For reproducibility
        random_values = np.random.randint(1, 10, len(hexagondata_d))
        total_random = sum(random_values)
        random_values = [value * total // total_random for value in random_values]

        sum_adjusted_values = sum(random_values)
        sum_adjustments = total_random - sum_adjusted_values

        # Adjust the values to meet the minimum value constraint
        while sum_adjustments != 0:
            for idx, value in enumerate(random_values):
                if value == min(random_values):
                    random_values[idx] += 1
                    sum_adjustments -= 1
                    if sum_adjustments == 0:
                        break

        
        hexagondata_d['val'] = random_values
        hexagondata.update(hexagondata_d)
    
    for index, row in hexagondata.iterrows():
        if row["postal code"] in list(top10_pincode.keys()):
            hexagondata.at[index, 'val'] = top10_pincode[row["postal code"]]
    
    return hexagondata


def read_top_data(info_dict, hexagondata):
    if info_dict["state"] == "All-India":
        top_10 = top10_data(info_dict)
        states = hexagondata["state"].dropna().drop_duplicates().to_list()
        for state in states:
            info_dict["state"] = state
            s_top_10 = top10_data(info_dict)
            top_10 = pd.concat([top_10, s_top_10], ignore_index=True)
    else:
        top_10 = top10_data(info_dict)
    
    return top_10