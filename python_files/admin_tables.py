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
    # Query to get basic movie data
    query = "SELECT * FROM directed;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "director_name"])

    st.write("Movie Directors:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_cast_table():
    # Query to get basic movie data
    query = "SELECT * FROM movie_cast;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "actor name"])

    st.write("Movie Cast details:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_genre_table():
    # Query to get basic movie data
    query = "SELECT * FROM movie_genre;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "genre"])

    st.write("Movie Genre:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_production_table():
    # Query to get basic movie data
    query = "SELECT * FROM production;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "production_company"])

    st.write("Movie Producers Details:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_finances_table():
    # Query to get basic movie data
    query = "SELECT * FROM finances;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "budget", "revenue", "budget_adj", "revenue_adj"])

    st.write("Movie Finances Data:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_release_details_table():

    # Query to get basic movie data
    query = "SELECT * FROM release_details;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "release_date", "release_year"])

    st.write("Movie Release Data:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_god_mode():
    # Page to add all movie details at once
    coln1, coln2, coln3 = st.columns([1, 1, 1])
    with coln1:
        st.markdown('---')
    with coln2:
        st.markdown('## Work in Progress')
    with coln3:
        st.markdown('---')