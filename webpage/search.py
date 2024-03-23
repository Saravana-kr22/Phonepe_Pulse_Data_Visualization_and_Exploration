import streamlit as st
import pandas as pd
import plotly.express as px
import json
from scripts.sql import *
from scripts.csv import *

def top_transaction(data, mysql, db_arg = None):
    col1,col2,col3 = st.columns([1,1,1],gap="small")
    Year = data["year"]
    Quarter = data["quater"]
    with col1:
        st.markdown("### :violet[State]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_state(Year,Quarter)
            else:
                df = Sql().search_tranaction_state(Year,Quarter)
        else:
            df = Csv().search_transaction_state(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='State',
                            title='Top 10 Transaction_Ammount',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_state1(Year,Quarter)
            else:
                df = Sql().search_tranaction_state1(Year,Quarter)
        else:
            df = Csv().search_transaction_state1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='State',
                            title='Top 10 Transactions',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        
    with col2:
        st.markdown("### :violet[District]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_district(Year,Quarter)
            else:
                df = Sql().search_tranaction_district(Year,Quarter)
        else:
            df = Csv().search_transaction_district(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='District',
                            title='Top 10 Transaction_Ammount',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_district1(Year,Quarter)
            else:
                df = Sql().search_tranaction_district1(Year,Quarter)
        else:
            df = Csv().search_transaction_district1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='District',
                            title='Top 10 Transactions',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)
        
    with col3:
        st.markdown("### :violet[Pincode]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_pincode(Year,Quarter)
            else:
                df = Sql().search_tranaction_pincode(Year,Quarter)
        else:
            df = Csv().search_transaction_pincode(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='Pincode',
                            title='Top 10 Transaction_Ammount',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_tranaction_pincode1(Year,Quarter)
            else:
                df = Sql().search_tranaction_pincode1(Year,Quarter)
        else:
            df = Csv().search_transaction_pincode1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='Pincode',
                            title='Top 10 Transactions',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    return None
    
def top_insurance(data, mysql, db_arg = None):
    col1,col2,col3 = st.columns([1,1,1],gap="small")
    Year = data["year"]
    Quarter = data["quater"]
    with col1:
        st.markdown("### :violet[State]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_state(Year,Quarter)
            else:
                df = Sql().search_insurance_state(Year,Quarter)
        else:
            df = Csv().search_insurance_state(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='State',
                            title='Top 10 Policy_Ammount',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_state1(Year,Quarter)
            else:
                df = Sql().search_insurance_state1(Year,Quarter)
        else:
            df = Csv().search_insurance_state1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='State',
                            title='Top 10 Policies Count',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        
    with col2:
        st.markdown("### :violet[District]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_district(Year,Quarter)
            else:
                df = Sql().search_insurance_district(Year,Quarter)
        else:
            df = Csv().search_insurance_district(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='District',
                            title='Top 10 Policy_Ammount',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_district1(Year,Quarter)
            else:
                df = Sql().search_insurance_district1(Year,Quarter)
        else:
            df = Csv().search_insurance_district1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='District',
                            title='Top 10 Policies Count',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)
        
    with col3:
        st.markdown("### :violet[Pincode]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_pincode(Year,Quarter)
            else:
                df = Sql().search_insurance_pincode(Year,Quarter)
        else:
            df = Csv().search_insurance_pincode(Year,Quarter)
        
        fig = px.pie(df, values='Total_Amount',
                            names='Pincode',
                            title='Top 10 Policy_Ammount',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).search_insurance_pincode1(Year,Quarter)
            else:
                df = Sql().search_insurance_pincode1(Year,Quarter)
        else:
            df = Csv().search_insurance_pincode1(Year,Quarter)
        
        fig = px.pie(df, values='Transactions_Count',
                            names='Pincode',
                            title='Top 10 Policies Count',
                            color_discrete_sequence=px.colors.sequential.Plotly3,
                            hover_data=['Total_Amount'],
                            labels={'Total_Amount':'Total_Amount'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)

    return None

def top_users(data, mysql, db_arg = None):
    Year = data["year"]
    Quarter = data["quater"]
    col1,col2 = st.columns(2, gap="large")
    col3,col4 = st.columns(2, gap="large")
    with col1:
        st.markdown("### :violet[Brands]")
        if Year in [2022,2023] and Quarter in [1,2,3,4]:
            if not(Year == 2022 and Quarter == 1):
                st.markdown("#### Sorry No Data to Display")
            else:
                user_brand(Year, Quarter, mysql, db_arg)
        else:
            user_brand(Year, Quarter, mysql, db_arg)

    with col2:
        st.markdown("### :violet[District]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).user_district(Year,Quarter)
            else:
                df = Sql().user_district(Year,Quarter)
        else:
            df = Csv().user_district(Year,Quarter)
        
        df.Total_Users = df.Total_Users.astype(float)
        fig = px.bar(df,
                        title='Top 10',
                        x="Total_Users",
                        y="District",
                        orientation='h',
                        color='Total_Users',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)
            
    with col3:
        st.markdown("### :violet[Pincode]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).user_pincode(Year,Quarter)
            else:
                df = Sql().user_pincode(Year,Quarter)
        else:
            df = Csv().user_pincode(Year,Quarter)
        fig = px.pie(df,
                        values='Total_Users',
                        names='Pincode',
                        title='Top 10',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Total_Users'])
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)
        
    with col4:
        st.markdown("### :violet[State]")
        if mysql:
            if db_arg:
                df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).user_state(Year,Quarter)
            else:
                df = Sql().user_state(Year,Quarter)
        else:
            df = Csv().user_state(Year,Quarter)
        
        fig = px.pie(df, values='Total_Users',
                            names='State',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Appopens'],
                            labels={'Total_Appopens':'Total_Appopens'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)
        
    return None

def  user_brand(Year, Quarter, mysql, db_arg):
    if mysql:
        if db_arg:
            df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).user_brand(Year,Quarter)
        else:
            df = Sql().user_brand(Year,Quarter)
    else:
        df = Csv().user_brand(Year,Quarter)
    fig = px.bar(df,
                    title='Top 10',
                    x="Total_Users",
                    y="Brand",
                    orientation='h',
                    color='Avg_Percentage',
                    color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)   
    return None
        