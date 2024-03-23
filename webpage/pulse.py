import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import geopandas as gpd
from scripts.data.aggerated_data import *


def detail_col_1():
    space1,trans_col,year_col,q_col,space2 = st.columns([1,10,7,10,1])

    with trans_col:
        data_option = st.selectbox(label = "" ,options= ["Transaction", "User", "Insurance"], index=0)
    with year_col:
        year_option = [2018,2019,2020,2021,2022,2023]
        if data_option == "Insurance":
            year_option = [2020,2021,2022,2023]
        
        year = st.selectbox(label = "" ,options= year_option, index=year_option.index(2023))
    with q_col:
        quater_options = ["Q1(Jan - Mar)","Q2(Apr - Jun)", "Q3(Jul - Sep)", "Q4(Oct - Dec)"]
        if (data_option == "Insurance") & (year == 2020):
            quater_options = ["Q2(Apr - Jun)", "Q3(Jul - Sep)", "Q4(Oct - Dec)"]
        quater = st.selectbox(label="", options =quater_options,index=quater_options.index("Q4(Oct - Dec)"))

    return data_option, year, quater


def detail_col_2():
    state_map = gpd.read_file("src/geojson/indian_states.geojson")
    space1 ,recenter_col, india_bcol, allindia_col, space3 = st.columns([1,7,5,15,1])
    states = state_map["ST_NM"].to_list()
    states.insert(0,"All-India")
    with recenter_col:
        with stylable_container(key="Recenterbutton",
                                css_styles="""button {background-color:#121326}"""):
            st.write("")
            recenter_button = st.button("Recenter Map")
    
    with india_bcol:
        with stylable_container(key="indiabutton",
                                    css_styles="""button {background-color:#121326}"""):
                st.write("")
                india_button = st.button("All-India")

        if india_button:
            st.session_state.load_map = states[0]
    
    with allindia_col:
        load_map = st.selectbox(label= "Select the State", options=states,index=states.index("All-India"), key="load_map")

    return recenter_button, load_map

def detail_col_3(load_map, data_option):
    if load_map == "All-India":
        space1,d_title, state_b, district_b, pincode_b,space2 = st.columns([1,15,5,5,5,1], gap="small")
        with d_title:
            st.markdown(f"<h2 style='color:#b069ff	;'>{data_option}</h2>", unsafe_allow_html=True)
        with state_b:
            with stylable_container(key="statebutton",
                                    css_styles="""button {background-color:#121326; border-radius: 18px;}"""):
                state_button = st.button("State")
        with district_b:
            with stylable_container(key="districtbutton",
                                    css_styles="""button {background-color:#121326; border-radius: 18px;}"""):
                district_button = st.button("District")
        with pincode_b:
            with stylable_container(key="pincodebutton",
                                    css_styles="""button {background-color:#121326; border-radius: 18px;}"""):
                pincode_button = st.button("Pincode")
    else:
        space1,d_title, district_b, pincode_b,space2 = st.columns([1,15,5,5,1], gap="small")
        with d_title:
            st.markdown(f"<h2 style='color:#b069ff	;'>{data_option}</h2>", unsafe_allow_html=True)
        with district_b:
            with stylable_container(key="districtbutton",
                                    css_styles="""button {background-color:#121326; border-radius: 18px;}"""):
                district_button = st.button("District")
        with pincode_b:
            with stylable_container(key="pincodebutton",
                                    css_styles="""button {background-color:#121326; border-radius: 18px;}"""):
                pincode_button = st.button("Pincode")


    top_data = "District"
    if district_button:
        top_data ="District"
    if pincode_button:
        top_data = "Pincode"
    if load_map == "All-India":
        top_data = "State"
        if district_button:
            top_data ="District"
        if pincode_button:
            top_data = "Pincode"
        if state_button:
            top_data = "State"
    return top_data

def detail_info_col(info_dict):
    data = aggregated_data(info_dict)
    data_option = info_dict["data_option"]
    if data_option == "Transaction":
        #st.write("All PhonePe transactions (UPI + Cards + Wallets)")
        total_count = data["Count"].sum()
        total_payement = data["Amount"].sum()
        avg_amount = total_payement/total_count
        total_count = '{:,.2f}'.format(total_count)
        total_payement = '{:,.2f}'.format(total_payement)
        total_payement = '₹'+str(total_payement)
        avg_amount = '{:,.2f}'.format(avg_amount)
        avg_amount = '₹'+str(avg_amount)
        st.markdown(f"""<p style='margin: 0;'>All PhonePe transactions (UPI + Cards + Wallets)</p>
                    <h2 style='color:#b069ff; margin: 0;'>{total_count}</h2>
                    <p style='margin: 0;'>Total payment value</p>
                    <h3 style='color:#b069ff; margin: 0;'>{total_payement}</h3>
                    <p style='margin: 0;'>Avg. transaction value</p>
                    <h2 style='color:#b069ff; margin: 0;'>{avg_amount}</h2>
                    """, unsafe_allow_html=True)
        
    elif data_option == "User":
        if isinstance(data, dict):
            reg_user = data["registeredUsers"]
            app_opens = data["appOpens"]
        else:
            reg_user =  data["registeredUsers"]
            app_opens = data["appOpens"]
            reg_user = reg_user.drop_duplicates()[0]
            app_opens = app_opens.drop_duplicates()[0]
        
        reg_user = '{:,.2f}'.format(reg_user)
        app_opens = '{:,.2f}'.format(app_opens)
        #st.write(type(app_opens))
        if app_opens == "0.00":
            app_opens = "Unavailable"
        quater = info_dict["quater"]
        year = info_dict["year"]
        st.markdown(f"""<p style='margin: 0;'>Registered PhonePe users till {quater} {year}</p>
                    <h2 style='color:#b069ff; margin: 0;'>{reg_user}</h2>
                    <p style='margin: 0;'>PhonePe app opens in {quater} {year}</p>
                    <h3 style='color:#b069ff; margin: 0;'>{app_opens}</h3>
                    """, unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    
    else:
        ins_purchased = data["paymentInstruments"][0]["count"]
        ins_amount = data["paymentInstruments"][0]["amount"]
        avg_amount = ins_amount/ins_purchased
        ins_purchased = '{:,.2f}'.format(ins_purchased)
        ins_amount = '{:,.2f}'.format(ins_amount)
        ins_amount = '₹'+str(ins_amount)
        avg_amount = '{:,.2f}'.format(avg_amount)
        avg_amount = '₹'+str(avg_amount)
        load_map = info_dict["data_option"]
        st.markdown(f"""<p style='margin: 0;'>{load_map} Insurance Policies Purchased (Nos.)</p>
                    <h2 style='color:#b069ff; margin: 0;'>{ins_purchased}</h2>
                    <p style='margin: 0;'>Total premium value</p>
                    <h3 style='color:#b069ff; margin: 0;'>{ins_amount}</h3>
                    <p style='margin: 0;'>Average premium value</p>
                    <h2 style='color:#b069ff; margin: 0;'>{avg_amount}</h2>
                    """, unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    return None