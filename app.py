import streamlit as st
import pydeck as pdk
import argparse
from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu
from webpage.pulse import *
from webpage.about import *
from webpage.basic_insight import *
from webpage.search import *
from scripts.pulse.layers import *
from scripts.pulse.viewstate import *
from scripts.data.top_data import *
from tools.mysql import *

 
def parse_mysql_arg (db_arg):
    arg = {}
    pairs = db_arg.split()
    for pair in pairs:
        key, value = pair.split(':')
        arg[key.strip()] = value.strip()
    k= list(arg.keys())
    db_par = ["host", "user", "password", "database"]
    if not db_par in k:
        raise Exception
    return arg

parser = argparse.ArgumentParser(description='Phonepe Pulse Data Visualization')
parser.add_argument('--use_mysql', type= bool, default=False , help="If --use_mysql is true the script will use mysql else it will use the csv files")
parser.add_argument('--mysql_arg', type= parse_mysql_arg, default=False , help="this arguments are used to connected to the database If it is not provide defaults from docker will be used")
args = parser.parse_args()

class Website():
    def __init__(self, mysql) :
        self.mysql = mysql
        self.arg = args.mysql_arg
        if mysql:
            if self.arg:
                Mysql(host=self.arg["host"], user= self.arg["user"], password=self.arg["password"], database=self.arg["database"]).store_data_in_mysql()
            Mysql().store_data_in_mysql()
        self.website()

    def home(self):
        space1, head_col, space2 = st.columns([3,7,3])
        with head_col:
            st.markdown("# :violet[PhonePe Data Visualization and Exploration]")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        img_col,data_col = st.columns([2,3],gap="medium")
        
        with img_col:
            st.image("src/images/phonepe_home.png", width=600)
        with data_col:
            st.write("")
            st.write("")
            st.write("")
            st.markdown("### :violet[Domain :] Fintech")
            st.markdown("### :violet[Technologies used :] Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.")
            st.markdown("### :violet[Overview :] This is a streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, insurances , top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get basic insights.")        
        return None
    
    def pulse(self):
        map_column, details_colmun = st.columns([7,4])

        with details_colmun:
            with stylable_container(key ="info_container", css_styles="""
                                {background-color: #3A3C5E;}"""):
               
                data_option, year, quater = detail_col_1()
                recenter_button, load_map = detail_col_2()
                
                st.markdown("----", unsafe_allow_html=True)
                
                top_data = detail_col_3(load_map, data_option)
               
                info_dict =  {"data_option":data_option,"year":year, "quater":quater, "state": load_map, "top_data": top_data}
                
                space1, detial_info, top_10 = st.columns([1,20,20])

                with detial_info:
                    detail_info_col(info_dict)

                with top_10:
                    st.markdown(f"<h3>Top 10 {top_data}</h3>", unsafe_allow_html=True)
                    top_10_result = top10_data(info_dict)
                    top_10_result["name"] = top_10_result["name"].str.title()
                    top_10_result = top_10_result.style.apply(lambda x: ['color: #b069ff' if isinstance(v, int) else '' for v in x], axis=1)
                    st.markdown(top_10_result.hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)
                    st.write("")
                    st.write("")
                    st.write("")
                    
            initial_view_state = viewstate(load_map)

            layer = list(create_layers(info_dict))
            if data_option == "Transaction":
                r = pdk.Deck(
                initial_view_state=initial_view_state,
                layers=layer, map_provider=None, tooltip={"html": """<p style= 'margin: 0; line-height: 1;'>{state}</p> 
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{ST_NM}</b>
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>All Transactions</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Count}</b> 
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Total Payment Value</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Amount}</b> 
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Avg. Transactions Value</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Avg}</b>""", 
                                                            "style": {"color": "white", "backgroundColor": "#121326"}})
                
            elif data_option =="User":
                r = pdk.Deck(
                initial_view_state=initial_view_state,
                layers=layer, map_provider=None, tooltip={"html": """<p style= 'margin: 0; line-height: 1;'>{state}</p> 
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{ST_NM}</b>
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Registered Users</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{registeredUsers}</b> 
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>App Opens</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{appOpens}</b> """, 
                                                            "style": {"color": "white", "backgroundColor": "#121326"}})
            else:
                r = pdk.Deck(
                initial_view_state=initial_view_state,
                layers=layer, map_provider=None, tooltip={"html": """<p style= 'margin: 0; line-height: 1;'>{state}</p> 
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{ST_NM}</b>
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Insurance Policies(Nos.)</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Count}</b> 
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Total Premium Value</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Amount}</b> 
                                                        <p style= 'margin: 0; line-height: 1; color:white;'>Avg. Premium Value</p>
                                                        <b style='color:#b069ff; margin: 0;line-height: 3;'>{Avg}</b>""", 
                                                            "style": {"color": "white", "backgroundColor": "#121326"}})

            with map_column:
                if recenter_button:
                    r.initial_view_state = initial_view_state
                with st.spinner("Loading the Map"):
                    c = st.pydeck_chart(r)
            return None
        
    def basic_insights(self):
        space1,tpye_col, year_col, quater_col, space2 = st.columns([2,4,4,4,2], gap="large")
        with tpye_col:
            Type = st.selectbox("**Type**", ("Transactions", "Users", "Insurance"))
            if Type == "Insurance":
                year_min = 2020
            else:
                year_min = 2018
        with year_col:
            Year = st.slider("**Year**", min_value=year_min, max_value=2023)
            if (Type == "Insurance") & (Year == 2020):
                quater_min = 2
            else:
                quater_min = 1
        with quater_col:
            Quarter = st.slider("**Quarter**", min_value=quater_min, max_value=4)

        data = {"type":Type, "year":Year, "quater":Quarter}

        if Type == "Transactions":
            if self.arg:
                trancaction(data,self.mysql, self.arg)
            else:
                trancaction(data,self.mysql)

        if Type == "Insurance":
            if self.arg:
                incurance(data,self.mysql, self.arg)
            else:
                incurance(data,self.mysql)
        if Type == "Users":
            if self.arg:
                users(data,self.mysql, self.arg)
            else:
                users(data,self.mysql)
        return None

    def search(self):
        colum1,colum2= st.columns([1.25,1],gap="large")
        with colum2:

            st.write("")
            Type = st.selectbox("**Type**", ("Transactions", "Users", "Insurance"))
            if Type == "Insurance":
                year_min = 2020
            else:
                year_min = 2018
        
            Year = st.slider("**Year**", min_value=year_min, max_value= 2023)
            if (Type == "Insurance") & (Year == 2020):
                quater_min = 2
            else:
                quater_min = 1
            
            Quarter = st.slider("**Quarter**", min_value=quater_min, max_value=4)
        
        data = {"type":Type, "year":Year, "quater":Quarter}

        with colum1:
            st.markdown("## :violet[Top Charts]")
            st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
            
        if Type == "Transactions":
            if self.arg:
                top_transaction(data,self.mysql, self.arg)
            else:
                top_transaction(data,self.mysql)
        if Type == "Insurance":
            if self.arg:
                top_insurance(data,self.mysql, self.arg)
            else:
                top_insurance(data,self.mysql)
        if Type == "Users":
            if self.arg:
                top_insurance(data,self.mysql, self.arg)
            else:
                top_users(data,self.mysql)
        return None
    
    def about(self):
        return about_page()
            
    def website(self):
            with stylable_container(key ="navigation_bar", css_styles="""
                                    {background-color: #121326;}"""):
                title_column,navigation_column = st.columns([12,18])
                with title_column:
                    s,logo, title = st.columns([1,6,40])

                    with logo:
                        st.write("")
                        img = "src/images/phonepe.png"
                        st.image(img, width=95)
                        st.write("")
                    with title:
                        st.markdown(
                        """
                        <h1 style='text-align: center;'> Phonepe Data Visuvalization</h1>
                        """,
                        unsafe_allow_html=True
                        )
                
                with navigation_column:
                    options = option_menu(menu_title = "Navigation Bar",
                        options = ["Home","Pulse","Basic insights","Search","About"],
                        icons =["house","graph-up-arrow","toggles","search","bar-chart"],
                        default_index=0,
                        orientation="horizontal",
                        styles={
                            "icon": {"color": "#70717c", "font-size": "20px"},
                            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
                            "nav-link-selected": {"background-color": "black"}
                        })
            
            if options == "Home":
                self.home()
            elif options == "Pulse":    
                self.pulse()
            elif options == "Basic insights":
                self.basic_insights()
            elif options == "Search":
                self.search()
            elif options == "About":
                self.about()  

if __name__ == "__main__":
     # To increase the wide of the webpage
    st.set_page_config(layout="wide", page_title="Phonepe Data Visuvalization", page_icon="src/images/phonepe.svg")
    Website(args.use_mysql)