import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu
from queries import show_query5, show_query10








def show_main_dashboard3():
        st.markdown(
            """
            <style>
                /* Container styling for each query */
                .query-container {
                    padding: 1rem;
                    margin: 1rem 0;
                    background-color: #f0f2f6; /* Light background for better contrast */
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Slight shadow for depth */
                }
                .header-text {
                    font-size: 1.2rem;
                    font-weight: bold;
                    color: #AEDBF0;
                    text-align: center;
                    margin-bottom: 1rem;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

       
        ####################################################  Query5 ##############################################
        show_query5()
        ###############################################   end of Query5  ##############################################

        ###############################################    Query10  ##############################################
        show_query10()
        ###############################################   end of Query10  ##############################################
