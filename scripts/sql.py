import pandas as pd
from tools.mysql import Mysql

class Sql(Mysql):
    def __init__(self, host="mysqldb", user="user", password="password", database="phonepe") -> None:
        super().__init__(host, user, password, database)

    def read_transaction(self, Year, Quarter):
        querry = f"""select state, sum(count) as Total_Transactions, 
                     sum(amount) as Total_amount from map_transaction where year = {Year} and quarter = {Quarter} group by state order by state"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
        return df
    
    def type_transaction(self, Year, Quarter):
        querry = f"""select Transaction_type, sum(Transaction_count) as Total_Transactions, 
                     sum(Transaction_amount) as Total_amount from aggregated_transaction where year= {Year} and quarter = {Quarter} 
                     group by transaction_type order by Transaction_type"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Transaction_type', 'Total_Transactions','Total_amount'])
        return df
    
    def state_transaction(self, Year , Quarter, selected_state):
        querry = f"""select State, District,year,quarter, sum(count) as Total_Transactions, 
                     sum(amount) as Total_amount from map_transaction where year = {Year} and quarter = {Quarter} 
                     and State = '{selected_state}' group by State, District,year,quarter order by state,district"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State','District','Year','Quarter','Total_Transactions','Total_amount'])
        return df
    
    def read_insurance(self, Year, Quarter):
        querry = f"""select state, sum(count) as Total_Policies, 
                     sum(amount) as Total_amount from map_insurance where year = {Year} and quarter = {Quarter} group by state order by state"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns= ['State', 'Total_Policies', 'Total_amount'])
        return df
    
    def state_insurance(self, Year , Quarter, selected_state):
        querry = f"""select State, District,year,quarter, sum(count) as Total_Policies, 
                     sum(amount) as Total_amount from map_insurance where year = {Year} and quarter = {Quarter} 
                     and State = '{selected_state}' group by State, District,year,quarter order by state,district"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State','District','Year','Quarter','Total_Policies','Total_amount'])
        return df
    
    def read_user(self, Year, Quarter):
        querry = f"""select state, sum(Registered_user) as Total_Users, sum(App_opens) 
                     as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} group by state order by state"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns= ['State', 'Total_Users','Total_Appopens'])
        return df
    
    def state_user(self, Year , Quarter, selected_state):
        querry = f"""select State,year,quarter,District,sum(Registered_user) as Total_Users, 
                     sum(App_opens) as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} 
                     and state = '{selected_state}' group by State, District,year,quarter order by state,district"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
        return df
    
    def search_tranaction_state(self, Year, Quarter):
        querry = f"""select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) 
                     as Total from  aggregated_transaction where year = {Year} and quarter = {Quarter} group 
                     by state order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_tranaction_district(self, Year, Quarter):
        querry = f"""select district , sum(Count) as Total_Count, sum(Amount) as Total 
                     from map_transaction where year = {Year} and quarter = {Quarter} group 
                     by district order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['District', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_tranaction_pincode(self, Year, Quarter):
        querry = f"""select pincode, sum(Transaction_count) as Total_Transactions_Count, 
                     sum(Transaction_amount) as Total from top_transaction where year = {Year} 
                     and quarter = {Quarter} group by pincode order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Pincode', 'Transactions_Count','Total_Amount'])
        return df

    def search_tranaction_state1(self, Year, Quarter):
        querry = f"""select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) 
                     as Total from  aggregated_transaction where year = {Year} and quarter = {Quarter} group 
                     by state order by Total_Transactions_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_tranaction_district1(self, Year, Quarter):
        querry = f"""select district , sum(Count) as Total_Count, sum(Amount) as Total 
                     from map_transaction where year = {Year} and quarter = {Quarter} group 
                     by district order by Total_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['District', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_tranaction_pincode1(self, Year, Quarter):
        querry = f"""select pincode, sum(Transaction_count) as Total_Transactions_Count, 
                     sum(Transaction_amount) as Total from top_transaction where year = {Year} 
                     and quarter = {Quarter} group by pincode order by Total_Transactions_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Pincode', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_insurance_state(self, Year, Quarter):
        querry = f"""select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) 
                     as Total from  aggregated_insurance where year = {Year} and quarter = {Quarter} group 
                     by state order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_insurance_district(self, Year, Quarter):
        querry = f"""select district , sum(Count) as Total_Count, sum(Amount) as Total 
                     from map_insurance where year = {Year} and quarter = {Quarter} group 
                     by district order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['District', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_insurance_pincode(self, Year, Quarter):
        querry = f"""select pincode, sum(Transaction_count) as Total_Transactions_Count, 
                     sum(Transaction_amount) as Total from top_insurance where year = {Year} 
                     and quarter = {Quarter} group by pincode order by Total desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Pincode', 'Transactions_Count','Total_Amount'])
        return df

    def search_insurance_state1(self, Year, Quarter):
        querry = f"""select state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) 
                     as Total from  aggregated_insurance where year = {Year} and quarter = {Quarter} group 
                     by state order by Total_Transactions_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_insurance_district1(self, Year, Quarter):
        querry = f"""select district , sum(Count) as Total_Count, sum(Amount) as Total 
                     from map_insurance where year = {Year} and quarter = {Quarter} group 
                     by district order by Total_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['District', 'Transactions_Count','Total_Amount'])
        return df
    
    def search_insurance_pincode1(self, Year, Quarter):
        querry = f"""select pincode, sum(Transaction_count) as Total_Transactions_Count, 
                     sum(Transaction_amount) as Total from top_insurance where year = {Year} 
                     and quarter = {Quarter} group by pincode order by Total_Transactions_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Pincode', 'Transactions_Count','Total_Amount'])
        return df
    
    def user_brand(self, Year, Quarter):
        querry = f"""select brands, sum(count) as Total_Count, avg(percentage)*100 as 
                     Avg_Percentage from aggregated_user where year = {Year} and quarter = {Quarter} 
                     group by brands order by Total_Count desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Brand', 'Total_Users','Avg_Percentage'])
        return df
    def user_district(self, Year, Quarter):
        querry = f"""select district, sum(Registered_User) as Total_Users, sum(app_opens) 
                     as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} 
                     group by district order by Total_Users desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['District', 'Total_Users','Total_Appopens'])
        return df
    
    def user_pincode(self, Year, Quarter):
        querry = f"""select Pincode, sum(Registered_users) as Total_Users from 
                     top_user where year = {Year} and quarter = {Quarter} group 
                     by Pincode order by Total_Users desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['Pincode', 'Total_Users'])
        return df
    
    def user_state(self, Year, Quarter):
        querry = f"""select state, sum(Registered_user) as Total_Users, sum(App_opens) 
                     as Total_Appopens from map_user where year = {Year} and quarter = {Quarter} 
                     group by state order by Total_Users desc limit 10"""
        self.cursor.execute(querry)
        df = pd.DataFrame(self.cursor.fetchall(),columns=['State', 'Total_Users','Total_Appopens'])
        return df
