import pandas as pd
from conn import run_query
import streamlit as st
import time

def admin_main_dashboard():
        
        def fetch_metrics():
            metrics = {
                "Total Movies": "SELECT COUNT(id) FROM movie;",
                "Total Directors": "SELECT COUNT(DISTINCT director_name) FROM directed;",
                "Total Actors": "SELECT COUNT(DISTINCT actor_name) FROM movie_cast;"
            }
            return {key: run_query(query)[0][0] for key, query in metrics.items()}

        def animate_metric(end_value):
            value = 0
            step = end_value // 100  
            placeholder = st.empty()
            for _ in range(100):
                value += step
                placeholder.metric(label="", value=f"{value:,}")
                time.sleep(0.01)
            placeholder.metric(label="", value=f"{end_value:,}")

        # Main Page - Top Metrics
        st.markdown("---")
        metrics = fetch_metrics()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Total Movies")
            animate_metric(metrics["Total Movies"])
        with col2:
            st.subheader("Total Directors")
            animate_metric(metrics["Total Directors"])
        with col3:
            st.subheader("Total Actors")
            animate_metric(metrics["Total Actors"])

        st.markdown("---")

def show_movies_table():
    
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get basic movie data
        query = "SELECT * FROM movie;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "original_title"])

        st.markdown("### Movie Data:")
        st.dataframe(df)
    
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")
    
    # Option to add new movie
    st.markdown("### Add New Movie:")
    movie_id = st.number_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = f"INSERT INTO movie (id, original_title) VALUES ({movie_id}, '{org_title}')"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Movie added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting movie, contact admin")

def show_metadata_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get movie metadata
        query = "SELECT * FROM metadata;"
        movies = run_query(query)
        df = pd.DataFrame(movies, columns=["id", "keywords", "tagline", "runtime (mins)", "homepage", "overview"])
        st.write("Movie MetaData:")
        st.dataframe(df)
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new movie
    st.markdown("### Add New Movie:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    keywords = st.text_input("List of keywords", placeholder="{word1,word2,..}")
    tagline = st.text_input("Tagline")
    runtime = st.number_input("runtime (mins)")
    homepage = st.text_input("Homepage URL", placeholder="https://iitpkd.ac.in/")
    overview = st.text_input("overview")

    if st.button("Add metadata for movie"):
        query = f"INSERT INTO metadata (id, keywords, tagline, runtime, homepage, overview) VALUES ({movie_id}, '{keywords}', '{tagline}', {runtime}, '{homepage}', '{overview}' )"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Movie metadata added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting movie metadata, check your inputs or contact admin")

def show_imdb_details_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get IMDb Details
        query = "SELECT * FROM imdb_details;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "imdb_id", "popularity", "vote_count", "vote_average"])

        st.write("Movie IMDb Details:")
        st.dataframe(df)
    
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new movie
    st.markdown("### Add IMDb Details:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    imdb_id = st.text_input("IMDb ID", placeholder="tt970456")
    popularity = st.number_input("Popularity")
    vote_count = st.number_input("Vote Count")
    vote_average = st.number_input("Vote Average")

    if st.button("Add IMDb details for movie"):
        query = f"INSERT INTO imdb_details (id, imdb_id, popularity, vote_count, vote_average) VALUES ({movie_id}, '{imdb_id}', {popularity}, {vote_count}, {vote_average})"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"IMDb details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting IMDb details, check your inputs or contact admin")

def show_directors_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get Directors table
        query = "SELECT * FROM directed;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "director_name"])

        st.markdown("### Movie Directors:")
        st.dataframe(df)
    
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new movie
    st.markdown("### Add director details:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    director_name = st.text_input("Director", placeholder="Nicholas Tesla")

    if st.button("Add director"):
        query = f"INSERT INTO directed (id, director_name) VALUES ({movie_id}, '{director_name}')"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Director details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting director details, check your inputs or contact admin")

def show_cast_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get basic movie cast data
        query = "SELECT * FROM movie_cast;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "actor name"])

        st.markdown("### Movie Cast details:")
        st.dataframe(df)
        
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new actor
    st.markdown("### Add actor:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    actor_name = st.text_input("Director", placeholder="Nicholas Tesla")

    if st.button("Add actor"):
        query = f"INSERT INTO movie_cast (id, actor_name) VALUES ({movie_id}, '{actor_name}')"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Actor details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting actor details, check your inputs or contact admin")

def show_genre_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get basic movie data
        query = "SELECT * FROM movie_genre;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "genre"])

        st.markdown("### Movie Genre:")
        st.dataframe(df)
        
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new actor
    st.markdown("### Add movie genre:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    genre = st.text_input("Genre", placeholder="Adventure")

    if st.button("Add genre"):
        query = f"INSERT INTO movie_genre (id, genre) VALUES ({movie_id}, '{genre}')"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Genre details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting genre details, check your inputs or contact admin")

def show_production_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get production company details
        query = "SELECT * FROM production;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "production_company"])

        st.markdown("### Movie Producers Details:")
        st.dataframe(df)
        
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new actor
    st.markdown("### Add movie production company:")
    movie_id = st.number_input("Movie ID", placeholder="135397")
    production_company = st.text_input("Production Company", placeholder="BioScope Films Ltd.")

    if st.button("Add production company"):
        query = f"INSERT INTO production (id, production_company) VALUES ({movie_id}, '{production_company}')"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Production Company details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting Production Company details, check your inputs or contact admin")
    

def show_finances_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get finance details
        query = "SELECT * FROM finances;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "budget", "revenue", "budget_adj", "revenue_adj"])

        st.write("Movie Finances Data:")
        st.dataframe(df)
        
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new actor
    st.markdown("### Add movie finances data:")
    movie_id = st.number_input("Movie ID")
    budget = st.number_input("Budget")
    revenue = st.number_input("Revenue")
    budget_adj = st.number_input("Budget_Adj")
    revenue_adj = st.number_input("Revenue_Adj")

    if st.button("Add finances"):
        query = f"INSERT INTO finances (id, budget, revenue, budget_adj, revenue_adj) VALUES ({movie_id}, {budget}, {revenue}, {budget_adj}, {revenue_adj})"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Finance details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting finance details, check your inputs or contact admin")    

def show_release_details_table():
    if 'show_df' not in st.session_state:
        st.session_state.show_df = True
    def refresh_df():
            st.session_state.show_df = not st.session_state.show_df
            time.sleep(0.001)
            st.session_state.show_df = not st.session_state.show_df
    
    if st.session_state.show_df:
        # Query to get movie release details
        query = "SELECT * FROM release_details;"
        movies = run_query(query)

        df = pd.DataFrame(movies, columns=["id", "release_date", "release_year"])

        st.write("Movie Release Details:")
        st.dataframe(df)
        
    st.button(label=" ", on_click=refresh_df, icon=":material/refresh:")

    # Option to add new actor
    st.markdown("### Add movie release details:")
    movie_id = st.number_input("Movie ID")
    release_date = st.date_input("Release Date", format='YYYY-MM-DD')
    release_year = st.number_input("Release Year")

    if st.button("Add release details"):
        query = f"INSERT INTO release_details (id, release_date, release_year) VALUES ({movie_id}, '{release_date}', {release_year})"
        try:
            query_return = run_query(query)
            if query_return=="Done":
                # refresh_df()
                st.success(f"Movie Release details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting release details, check your inputs or contact admin") 

def show_god_mode():
    # Page to add all movie details at once
    st.markdown("### Add all details of a movie:")
    movie_id = st.number_input("Movie ID")
    org_title = st.text_input("original title")
    keywords = st.text_input("List of keywords (in braces'\{\}')", placeholder="{word1,word2,..}")
    tagline = st.text_input("Tagline")
    runtime = st.number_input("runtime (mins)")
    homepage = st.text_input("Homepage URL", placeholder="https://iitpkd.ac.in/")
    overview = st.text_input("overview")
    imdb_id = st.text_input("IMDb ID", placeholder="tt970456")
    popularity = st.number_input("Popularity")
    vote_count = st.number_input("Vote Count")
    vote_average = st.number_input("Vote Average")
    directors_list = st.text_input("List of directors", placeholder="Chris Nolan, John Nolan, ...")
    actors_list = st.text_input("List of actors", placeholder="John Riley, Harold Finch, ...")
    genres_list = st.text_input("List of genre", placeholder="Adventure, Thriller, ...")
    producers_list = st.text_input("List of production companies", placeholder="BioScope Films Ltd., BadRobot, ...")
    budget = st.number_input("Budget")
    revenue = st.number_input("Revenue")
    budget_adj = st.number_input("Budget_Adj")
    revenue_adj = st.number_input("Revenue_Adj")
    release_date = st.date_input("Release Date", format='YYYY-MM-DD')
    release_year = st.number_input("Release Year")

    if st.button("Add all details"):
        query_list = []
        # Insert into movie table
        query_list.append(f"INSERT INTO movie (id, original_title) VALUES ({movie_id}, '{org_title}')")
        # Add metadata 
        query_list.append(f"INSERT INTO metadata (id, keywords, tagline, runtime, homepage, overview) VALUES ({movie_id}, '{keywords}', '{tagline}', {runtime}, '{homepage}', '{overview}' )")
        # Add imdb details
        query_list.append(f"INSERT INTO imdb_details (id, imdb_id, popularity, vote_count, vote_average) VALUES ({movie_id}, '{imdb_id}', {popularity}, {vote_count}, {vote_average})")
        # Add each director
        director_names = directors_list.split(',')
        for name in director_names:
            query_list.append(f"INSERT INTO directed (id, director_name) VALUES ({movie_id}, '{name}')")
        # Add each actor
        actor_names = actors_list.split(',')
        for name in actor_names:
            query_list.append(f"INSERT INTO movie_cast (id, actor_name) VALUES ({movie_id}, '{name}')")
        # Add each genre
        genres = genres_list.split(',')
        for genre in genres:
            query_list.append(f"INSERT INTO movie_genre (id, genre) VALUES ({movie_id}, '{genre}')")
        # Add each producer
        producers = producers_list.split(',')
        for producer in producers:
            query_list.append(f"INSERT INTO production (id, production_company) VALUES ({movie_id}, '{producer}')")
        # Add finances
        query_list.append(f"INSERT INTO finances (id, budget, revenue, budget_adj, revenue_adj) VALUES ({movie_id}, {budget}, {revenue}, {budget_adj}, {revenue_adj})")
        # Add release details
        query_list.append(f"INSERT INTO release_details (id, release_date, release_year) VALUES ({movie_id}, '{release_date}', {release_year})")

        try:
            for each_query in query_list:
                query_return = run_query(each_query)
                if query_return!="Done":
                    raise Exception    
            st.success(f"All details added successfully! {query_return}")
        except:
            st.warning("Oops! Error inserting movie details, check your inputs or contact admin")