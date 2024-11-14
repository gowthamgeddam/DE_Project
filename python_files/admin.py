import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu
from admin_tables import *

def admin_dashboard():
    
    if st.sidebar.button("Logout"):
            clear_session()
            #st.experimental_set_query_params(dummy_param=1) 
    st.markdown('<div class="header1"><h1>Admin Dashboard</h1></div>', unsafe_allow_html=True)
    
    with st.sidebar:
        selected = option_menu (menu_title = "Admin",
                                options=["Home", "Movies", "Metadata", "IMDb Details", "Directors", "Cast", "Genre", "Production", "Finances", "Release Details", "GOD MODE"],
                               default_index=0,
                               icons=("house-lock-fill", "film", "postcard", "database-fill", "camera-reels", "people-fill", "puzzle", "building", "currency-exchange", "ticket-perforated-fill", "shield-lock"),
                               menu_icon='person-fill-lock'
                               )
    
    # Selected Page to Show
    if selected == "Home":
        admin_main_dashboard()
    elif selected == "Movies":
        show_movies_table()
    elif selected == "Metadata":
        show_metadata_table()
    elif selected == "IMDb Details":
        show_imdb_details_table()
    elif selected == "Directors":
        show_directors_table()
    elif selected == "Cast":
        show_cast_table()
    elif selected == "Genre":
        show_genre_table()
    elif selected == "Production":
        show_production_table()
    elif selected == "Finances":
        show_finances_table()
    elif selected == "Release Details":
        show_release_details_table()
    elif selected == "GOD MODE":
        show_god_mode()
    else:
        admin_main_dashboard()