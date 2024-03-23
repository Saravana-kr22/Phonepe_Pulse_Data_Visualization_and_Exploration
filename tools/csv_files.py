import pandas as pd
import json
import os

class CreateCSVFiles:
    def __init__(self) -> None:
        self.write_csv()

    def read_tranction(self, spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data['data']['transactionData']:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")), 'Transaction_type': data["name"], 
                                          'Transaction_count': data['paymentInstruments'][0]['count'], 'Transaction_amount': data['paymentInstruments'][0]['amount']})                      

        return pd.DataFrame(data_list)
    
    def read_user(self, spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    if json_data['data']['usersByDevice'] == None:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")), 'Brands': 0, 
                                          'Count': 0, 'Percentage': 0})
                    else:
                        for data in json_data['data']['usersByDevice']:
                            data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")), 'Brands': data["brand"], 
                                          'Count': data["count"], 'Percentage': data["percentage"]})                      

        return pd.DataFrame(data_list)

    def read_insurance(self, spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data['data']['transactionData']:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")), 'Transaction_type': data["name"], 
                                          'Transaction_count': data['paymentInstruments'][0]['count'], 'Transaction_amount': data['paymentInstruments'][0]['amount']})                      

        return pd.DataFrame(data_list)
    
    def map_tranction(self, spath):
        data_list = []
        spath = spath.replace("/country/india/", "/hover/country/india/")
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data["data"]["hoverDataList"]:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'District': data["name"], 
                                          'Count': data["metric"][0]["count"], 'Amount': data["metric"][0]["amount"]})                      

        return pd.DataFrame(data_list)

    def map_user(self, spath):
        data_list = []
        spath = spath.replace("/country/india/", "/hover/country/india/")
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data["data"]["hoverData"].items():
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'District': data[0], 
                                          'RegisteredUser': data[1]["registeredUsers"], 'AppOpens': data[1]["appOpens"]})                 

        return pd.DataFrame(data_list)

    def map_insurance(self, spath):
        data_list = []
        spath = spath.replace("/country/india/", "/hover/country/india/")
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data["data"]["hoverDataList"]:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'District': data["name"], 
                                          'Count': data["metric"][0]["count"], 'Amount': data["metric"][0]["amount"]})                      

        return pd.DataFrame(data_list)

    def top_transaction(self, spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data['data']['pincodes']:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'Pincode': data["entityName"], 
                                          'Transaction_count': data['metric']['count'], 'Transaction_amount': data['metric']['amount']})                      

        return pd.DataFrame(data_list)

    def top_user(self,spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data['data']['pincodes']:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'Pincode': data["name"], 
                                          'RegisteredUsers': data['registeredUsers']})                      

        return pd.DataFrame(data_list)

    def top_insurance(self,spath):
        data_list = []
        states = os.listdir(spath)
        for state in states:
            cur_state = spath + f"{state}" + "/"
            years = os.listdir(cur_state)
            for year in years:
                cur_year = cur_state + f"{year}" + "/"
                file_list = os.listdir(cur_year) 
                for file in file_list:
                    cur_file = cur_year + file
                    file_data = open(cur_file, 'r')
                    json_data = json.load(file_data)
                    for data in json_data['data']['pincodes']:
                        data_list.append({'State': state, 'Year': year, 'Quarter': int(file.strip(".json")),'Pincode': data["entityName"], 
                                          'Transaction_count': data['metric']['count'], 'Transaction_amount': data['metric']['amount']})                      

        return pd.DataFrame(data_list)

    def write_csv(self):
        path = "pulse/data/" 
        folders = os.listdir(path)
        for folder in folders:
            tpath = path + f"{folder}" +"/"
            types = os.listdir(tpath)
            for type in types:
                spath = tpath +f"{type}"+"/country/india/state/"
                if type == "transaction":
                    if folder == "aggregated":
                        data = self.read_tranction(spath)
                    if folder == "map":
                        data = self.map_tranction(spath)
                    if folder == "top":
                        data = self.top_transaction(spath)
                if type == "user":
                    if folder == "aggregated":
                        data = self.read_user(spath)
                    if folder == "map":
                        data = self.map_user(spath)
                    if folder == "top":
                        data = self.top_user(spath)
                if type == "insurance" :
                    if folder == "aggregated":
                        data = self.read_insurance(spath)
                    if folder == "map":
                        data = self.map_insurance(spath)
                    if folder == "top":
                        data = self.top_insurance(spath)
                data.to_csv(f"src/csv_data/{folder}_{type}.csv", index=False)
                    
        return None
    

if __name__ == "__main__":
    CreateCSVFiles()