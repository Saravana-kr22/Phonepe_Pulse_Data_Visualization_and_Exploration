import mysql.connector as sql
import pandas as pd
import os

class Mysql():
    def __init__(self, host = "mysqldb", user = "user", password = "password",
                 database = "phonepe") -> None:
        self.dbconnnection = sql.connect(host = host, user = user,
                                         password = password, database = database)
        self.cursor = self.dbconnnection.cursor()
        self.path = "src/csv_data"

    def agg_transaction(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int,
                     Transaction_type varchar(100), Transaction_count int, Transaction_amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def agg_user(self, file):
        querry = f"""create table {file}  (State varchar(100), Year int, Quarter int, Brands varchar(100), 
                     Count int, Percentage double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def agg_insurance(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int,
                     Transaction_type varchar(100), Transaction_count int, Transaction_amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None
    
    def map_transcation(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     District varchar(100), Count int, Amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def map_user(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     District varchar(100), Registered_user int, App_opens int)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def map_insurance(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     District varchar(100), Count int, Amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None
    
    def top_transaction(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     Pincode int, Transaction_count int, Transaction_amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def top_user(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     Pincode int, Registered_users int)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def top_insurance(self, file):
        querry = f"""create table {file} (State varchar(100), Year int, Quarter int, 
                     Pincode int, Transaction_count int, Transaction_amount double)"""
        self.cursor.execute(querry)
        df = pd.read_csv(f"{self.path}/{file}.csv").dropna()
        for i, row in df.iterrows():
            insert_querry = f"INSERT INTO {file} VALUES (%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(insert_querry, tuple(row))
        self.dbconnnection.commit()
        return None

    def create_tables(self, files):
        for file in files:
            if "aggregated" in file:
                if "transaction" in file:
                    self.agg_transaction(file)
                if "user" in file:
                    self.agg_user(file)
                if "insurance" in file:
                    self.agg_insurance(file)
            if "map" in file:
                if "transaction" in file:
                    self.map_transcation(file)
                if "user" in file:
                    self.map_user(file)
                if "insurance" in file:
                    self.map_insurance(file)
            if "top" in file:
                if "transaction" in file:
                    self.top_transaction(file)
                if "user" in file:
                    self.top_user(file)
                if "insurance" in file:
                    self.top_insurance(file)
        return None

    def store_data_in_mysql(self):
        files = os.listdir(self.path)
        files = list(map(lambda x: x.strip(".csv"), files))
        self.cursor.execute("show tables")
        tables = self.cursor.fetchall()
        if tables:
            for table in tables:
                if table[0] in files:
                    break
        else:
            self.create_tables(files)
        return None

