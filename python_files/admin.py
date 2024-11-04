import pandas as pd
import plotly.express as px
from conn import create_connection,run_query
import streamlit as st
from logout import clear_session

def admin_dashboard():
    
    if st.sidebar.button("Logout"):
            clear_session()
            #st.experimental_set_query_params(dummy_param=1) 
    st.markdown('<div class="header1"><h1>Admin Dashboard</h1></div>', unsafe_allow_html=True)
    
    # Query to get basic movie data
    query = "SELECT * FROM movie;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "original_title"])

    #if st.sidebar.button("Logout",key="admin_logout"):
        #st.sidebar.button("Logout", key="admin_logout",on_click=clear_session)
    

    
    
    st.write("Movie Data:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

    
    
   