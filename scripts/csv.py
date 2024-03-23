import pandas as pd

class Csv:
    def __init__(self) -> None:
        pass

    def read_transaction(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"State" : state,"Total_Transactions":tt,"Total_amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="State")
        return df3
    
    def type_transaction(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        types = df["Transaction_type"].drop_duplicates().to_list()
        row = []
        for type in types:
            df2 = df[df.Transaction_type == type]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"Transaction_type" : type,"Total_Transactions":tt,"Total_amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transaction_type")
        return df3
    
    def state_transaction(self, Year , Quarter, selected_state):
        df = pd.read_csv('src/csv_data/map_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        df = df[df.State == selected_state.lower()].reset_index(drop = True)
        districts = df["District"].drop_duplicates().to_list()
        row = []
        for district in districts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"State" : selected_state,'District':district,'Year': Year,'Quarter':Quarter,"Total_Transactions":tt,"Total_amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="District")
        return df3
    
    def read_insurance(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"State" : state,"Total_Policies":tt,"Total_amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="State")
        return df3
    
    
    def state_insurance(self, Year , Quarter, selected_state):
        df = pd.read_csv('src/csv_data/map_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        df = df[df.State == selected_state.lower()].reset_index(drop = True)
        districts = df["District"].drop_duplicates().to_list()
        row = []
        for district in districts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"State" : selected_state,'District':district,'Year': Year,'Quarter':Quarter,"Total_Policies":tt,"Total_amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="District")
        return df3
    
    def read_user(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            print(df2)
            tt = df2["RegisteredUser"].sum()
            ta = df2["AppOpens"].sum()
            row.append({"State" : state,"Total_Users":tt,"Total_Appopens":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="State")
        return df3
    
    def state_user(self, Year , Quarter, selected_state):
        df = pd.read_csv('src/csv_data/map_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        df = df[df.State == selected_state.lower()].reset_index(drop = True)
        districts = df["District"].drop_duplicates().to_list()
        row = []
        for district in districts:
            df2 = df[df.District == district]
            tt = df2["RegisteredUser"].sum()
            ta = df2["AppOpens"].sum()
            row.append({"State" : selected_state,'Year': Year,'Quarter':Quarter, 'District':district, "Total_Users":tt, "Total_Appopens":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="District")
        return df3
    
    def search_transaction_state(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"State" : state,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_transaction_district(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        disctricts = df["District"].drop_duplicates().to_list()
        row = []
        for district in disctricts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"District" : district,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_transaction_pincode(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/top_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        pincodes = df["Pincode"].drop_duplicates().to_list()
        row = []
        for pincode in pincodes:
            df2 = df[df.Pincode == pincode]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"Pincode" : pincode,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_transaction_state1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"State" : state,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def search_transaction_district1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        disctricts = df["District"].drop_duplicates().to_list()
        row = []
        for district in disctricts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"District" : district,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def search_transaction_pincode1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/top_transaction.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        pincodes = df["Pincode"].drop_duplicates().to_list()
        row = []
        for pincode in pincodes:
            df2 = df[df.Pincode == pincode]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"Pincode" : pincode,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def search_insurance_state(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"State" : state,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_insurance_district(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        disctricts = df["District"].drop_duplicates().to_list()
        row = []
        for district in disctricts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"District" : district,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_insurance_pincode(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/top_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        pincodes = df["Pincode"].drop_duplicates().to_list()
        row = []
        for pincode in pincodes:
            df2 = df[df.Pincode == pincode]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"Pincode" : pincode,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Amount", ascending= False)
        return df3.head(10)
    
    def search_insurance_state1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"State" : state,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def search_insurance_district1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        disctricts = df["District"].drop_duplicates().to_list()
        row = []
        for district in disctricts:
            df2 = df[df.District == district]
            tt = df2["Count"].sum()
            ta = df2["Amount"].sum()
            row.append({"District" : district,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def search_insurance_pincode1(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/top_insurance.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        pincodes = df["Pincode"].drop_duplicates().to_list()
        row = []
        for pincode in pincodes:
            df2 = df[df.Pincode == pincode]
            tt = df2["Transaction_count"].sum()
            ta = df2["Transaction_amount"].sum()
            row.append({"Pincode" : pincode,"Transactions_Count":tt,"Total_Amount":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Transactions_Count", ascending= False)
        return df3.head(10)
    
    def user_brand(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/aggregated_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        brands = df["Brands"].drop_duplicates().to_list()
        row = []
        for brand in brands:
            df2 = df[df.Brands == brand]
            tt = df2["Count"].sum()
            ta = df2["Percentage"].mean() * 100
            row.append({"Brand" : brand,"Total_Users":tt,"Avg_Percentage":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Users", ascending= False)
        return df3.head(10)
    
    def user_district(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        disctricts = df["District"].drop_duplicates().to_list()
        row = []
        for district in disctricts:
            df2 = df[df.District == district]
            tt = df2["RegisteredUser"].sum()
            ta = df2["AppOpens"].sum()
            row.append({"District" : district,"Total_Users":tt,"Total_Appopens":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Users", ascending= False)
        return df3.head(10)
    
    def user_pincode(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/top_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        pincodes = df["Pincode"].drop_duplicates().to_list()
        row = []
        for pincode in pincodes:
            df2 = df[df.Pincode == pincode]
            tt = df2["RegisteredUsers"].sum()
            row.append({"Pincode" : pincode,"Total_Users":tt})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Users", ascending= False)
        return df3.head(10)
    
    def user_state(self, Year, Quarter):
        df = pd.read_csv('src/csv_data/map_user.csv')
        df = df[df.Year == Year].reset_index(drop = True)
        df = df[df.Quarter == Quarter].reset_index(drop = True)
        states = df["State"].drop_duplicates().to_list()
        row = []
        for state in states:
            df2 = df[df.State == state]
            tt = df2["RegisteredUser"].sum()
            ta = df2["AppOpens"].sum()
            row.append({"State" : state,"Total_Users":tt,"Total_Appopens":ta})
        df3 = pd.DataFrame(row)
        df3 = df3.sort_values(by="Total_Users", ascending= False)
        return df3.head(10)

