import streamlit as st
import pandas as pd
import plotly.express as px
import json
from scripts.sql import *
from scripts.csv import *

def trancaction(data, mysql, db_arg = None):
    with open("src/geojson/indian_states.geojson","r")as f:
        geodata = json.load(f)
    Year = data["year"]
    Quarter = data["quater"]
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("## :violet[Overall State Data - Transactions Amount]")
        if mysql:
            if db_arg:
                df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).read_transaction(Year,Quarter)
            else:
                df1 = Sql().read_transaction(Year,Quarter)
        else:
            df1 = Csv().read_transaction(Year,Quarter)
        
        df2 = pd.read_csv('src/pincode_coordinates.csv')
        df2 = df2["state"].drop_duplicates().reset_index(drop=True)
        df1.State = df2
    

        fig = px.choropleth(df1, geojson=geodata,
                featureidkey='properties.ST_NM',
                locations='State',
                color='Total_amount',
                color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        
        st.markdown("## :violet[Overall State Data - Transactions Count]")
        df1.Total_Transactions = df1.Total_Transactions.astype(int)
        df1.State = df2

        fig = px.choropleth(df1,geojson=geodata,
                featureidkey='properties.ST_NM',
                locations='State',
                color='Total_Transactions',
                color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)
        
    st.markdown("## :violet[Top Payment Type]")
    if mysql:
        if db_arg:
            df = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).type_transaction(Year,Quarter)
        else:
            df = Sql().type_transaction(Year,Quarter)   
    else:
        df = Csv().type_transaction(Year,Quarter)  

    fig = px.bar(df,
                title='Transaction Types vs Total_Transactions',
                x="Transaction_type",
                y="Total_Transactions",
                orientation='v',
                color='Total_amount',
                color_continuous_scale=px.colors.sequential.Agsunset)
    fig_pie = px.pie(df,
                 names="Transaction_type",
                 values="Total_Transactions",
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 title='Transaction Types Distribution')
    chart_col, pie_col = st.columns(2, gap="large")
    with chart_col:
        st.plotly_chart(fig,use_container_width=True)
    with pie_col:
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.markdown("# ")
    st.markdown("## :violet[Select any State to explore more]")
    selected_state = st.selectbox("", options=df2.to_list()
                        ,index=21)
    if mysql:
        if db_arg:
            df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).state_transaction(Year,Quarter, selected_state)
        else:
            df1 = Sql().state_transaction(Year,Quarter, selected_state) 
    else:
        df1 = Csv().state_transaction(Year,Quarter, selected_state)
    
    fig = px.bar(df1,
                title=selected_state,
                x="District",
                y="Total_Transactions",
                orientation='v',
                color='Total_amount',
                color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)

    return None

def incurance(data, mysql, db_arg =None):
    with open("src/geojson/indian_states.geojson","r")as f:
        geodata = json.load(f)
    Year = data["year"]
    Quarter = data["quater"]
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("## :violet[Overall State Data - Insurance Amount]")
        if mysql:
            if db_arg:
                df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                    database=db_arg["database"]).read_insurance(Year,Quarter)
            else:
                df1 = Sql().read_insurance(Year,Quarter)
        else:
            df1 = Csv().read_insurance(Year,Quarter)
        
        df2 = pd.read_csv('src/pincode_coordinates.csv')
        df2 = df2["state"].drop_duplicates().reset_index(drop=True)
        df1.State = df2
    

        fig = px.choropleth(df1, geojson=geodata,
                featureidkey='properties.ST_NM',
                locations='State',
                color='Total_amount',
                color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        
        st.markdown("## :violet[Overall State Data - Policies Count]")
        df1.Total_Policies = df1.Total_Policies.astype(int)
        df1.State = df2

        fig = px.choropleth(df1,geojson=geodata,
                featureidkey='properties.ST_NM',
                locations='State',
                color='Total_Policies',
                color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)
    
    st.markdown("## :violet[Select any State to explore more]")
    selected_state = st.selectbox("", options=df2.to_list()
                        ,index=21)
    if mysql:
        if db_arg:
            df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).state_insurance(Year,Quarter, selected_state)
        else:
            df1 = Sql().state_insurance(Year,Quarter, selected_state) 
    else:
        df1 = Csv().state_insurance(Year,Quarter, selected_state)
    
    fig = px.bar(df1,
                title=selected_state,
                x="District",
                y="Total_Policies",
                orientation='v',
                color='Total_amount',
                color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)

    return None

def users(data, mysql, db_arg =None):
    st.markdown("## :violet[Overall State Data - Total User ]")
    with open("src/geojson/indian_states.geojson","r")as f:
        geodata = json.load(f)
    Year = data["year"]
    Quarter = data["quater"]
    
    if mysql:
        if db_arg:
            df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).read_user(Year,Quarter)
        else:
            df1 = Sql().read_user(Year,Quarter)
    else:
        df1 = Csv().read_user(Year,Quarter)
    
    df2 = pd.read_csv('src/pincode_coordinates.csv')
    df2 = df2["state"].drop_duplicates().reset_index(drop=True)
    df1.State = df2
    df1.Total_Users = df1.Total_Users.astype(int)

    fig = px.choropleth(df1, geojson=geodata,
            featureidkey='properties.ST_NM',
            locations='State',
            color='Total_Users',
            color_continuous_scale='sunset')

    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
    
    # BAR CHART TOTAL UERS - DISTRICT WISE DATA 
    st.markdown("## :violet[Select any State to explore more]")
    selected_state = st.selectbox("", options=df2.to_list()
                        ,index=21)
    if mysql:
        if db_arg:
            df1 = Sql(host=db_arg["host"], user= db_arg["user"], password=db_arg["password"], 
                database=db_arg["database"]).state_user(Year,Quarter, selected_state)
        else:
            df1 = Sql().state_user(Year,Quarter, selected_state) 
    else:
        df1 = Csv().state_user(Year,Quarter, selected_state)
  
    df1.Total_Users = df1.Total_Users.astype(int)
    
    fig = px.bar(df1,
                title=selected_state,
                x="District",
                y="Total_Users",
                orientation='v',
                color='Total_Users',
                color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig,use_container_width=True)