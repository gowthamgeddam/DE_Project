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
                                options=["home", "movies", "metadata", "imdb details", "directors", "cast", "genre", "production", "finances", "release details", "GOD MODE"],
                               default_index=0,
                               icons=("house-lock-fill", "film", "film", "database-fill-lock", "film", "film", "film", "film", "film", "film", "shield-lock"),
                               menu_icon='person-fill-lock'
                               )
    
    # Selected Page to Show
    if selected == "home":
        admin_main_dashboard()
    elif selected == "movies":
        show_movies_table()
    elif selected == "metadata":
        show_metadata_table()
    elif selected == "imdb details":
        show_imdb_details_table()
    elif selected == "directors":
        show_directors_table()
    elif selected == "cast":
        show_cast_table()
    elif selected == "genre":
        show_genre_table()
    elif selected == "production":
        show_production_table()
    elif selected == "finances":
        show_finances_table()
    elif selected == "release details":
        show_release_details_table()
    elif selected == "GOD MODE":
        show_god_mode()
    else:
        admin_main_dashboard()