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

def show_imdb_details_table():
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

def show_directors_table():
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

def show_cast_table():
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

def show_genre_table():
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

def show_production_table():
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

def show_finances_table():
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

def show_release_details_table():

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

def show_god_mode():
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