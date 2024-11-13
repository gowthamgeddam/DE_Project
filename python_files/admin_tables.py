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
    # Query to get basic movie data
    query = "SELECT * FROM movie;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "original_title"])

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

def show_metadata_table():
    # Query to get basic movie data
    query = "SELECT * FROM metadata;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "keywords", "tagline", "runtime (mins)", "homepage", "overview"])

    st.write("Movie MetaData:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

def show_imdb_details_table():
    # Query to get basic movie data
    query = "SELECT * FROM imdb_details;"
    movies = run_query(query)

    df = pd.DataFrame(movies, columns=["id", "imdb_id", "popularity", "vote_count", "vote_average"])

    st.write("Movie IMDb Details:")
    st.dataframe(df)

    # Option to add new movie
    st.write("Add New Movie:")
    movie_id = st.text_input("Movie ID")
    org_title = st.text_input("original title")

    if st.button("Add Movie"):
        query = "INSERT INTO movie (original_title, release_date) VALUES (%s, %s)"
        run_query(query, (movie_id, org_title))
        st.success("Movie added successfully!")

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