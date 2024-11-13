import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu

import time
from dash1 import show_main_dashboard1
from dash2 import show_main_dashboard2
from dash3 import show_main_dashboard3
from main_dash import main_dashboard

def user_dashboard():
    # Custom CSS for background and header
    def add_custom_css():
        st.markdown(
            """
            <style>
            /* Background color for the page */
            body {
                background-color: #01172B;
            }
            .header1 {
                padding: 1rem;
                color: white;
                background-color: #4B6587;
                text-align: left;
                width: 100%;
                border-radius: 8px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logout-button {
                padding: 8px 16px;
                background-color: #333;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard_header{
             margin-bottom : 2rem;
             }
            </style>
            """,
            unsafe_allow_html=True
        )

    add_custom_css()

   
    if st.sidebar.button("Logout"):
        clear_session()

    with st.sidebar:
        selected = option_menu (menu_title = "User Dashboard",
                                options=["home","page1","page2","page3"],
                               default_index=0,
                               icons=("house","house","house","house"),
                               )
    
   

    st.markdown('<div class="dashboard_header"><div class="header1"><h1>User Dashboard</h1></div></div>', unsafe_allow_html=True)

    

    # Initialize session state variables for dashboard page and director offset
    
    if 'director_offset' not in st.session_state: #Query 1
        st.session_state['director_offset'] = 0
    if 'dir_offset' not in st.session_state: #Query 5
        st.session_state['dir_offset'] = 0
    if 'corr_offset' not in st.session_state: #Query 6
        st.session_state['corr_offset'] = 0
    

    
    if selected == "home":
        main_dashboard()
    elif selected == "page1":
        show_main_dashboard1()
    elif selected == "page2":
        show_main_dashboard2()
    else:
        show_main_dashboard3()



     






