import streamlit as st
import pandas as pd
from conn import run_query






# Function Definitions with SQL Queries
def get_movie_details_query(movie_name):
    return f"""
    CREATE OR REPLACE FUNCTION get_movie_details(movie_name VARCHAR) RETURNS TABLE (
    movie_id BIGINT,
    release_year INT,
    imdb_rating DOUBLE PRECISION ) AS $$
    BEGIN
    RETURN QUERY SELECT
    m.id AS movie_id,
    rd.release_year,
    id.vote_average AS imdb_rating
    FROM
    movie m JOIN
    release_details rd ON m.id = rd.id JOIN
    imdb_details id ON m.id = id.id WHERE
    m.original_title = movie_name
    LIMIT 1; 
    END;
    $$ LANGUAGE plpgsql;
    """

def get_actor_highest_grossing_movie_query(actor_name):
    return f"""
    CREATE OR REPLACE FUNCTION get_actor_highest_grossing_movie(p_actor_name VARCHAR) RETURNS VARCHAR AS $$
    DECLARE highest_grossing_movie VARCHAR; BEGIN
    SELECT m.original_title INTO highest_grossing_movie FROM movie_cast mc
    JOIN movie m ON mc.id = m.id
    JOIN finances f ON m.id = f.id
    WHERE mc.actor_name = p_actor_name ORDER BY f.revenue DESC
    LIMIT 1;
    RETURN highest_grossing_movie; END;
    $$ LANGUAGE plpgsql;
    """

def get_movie_director_query(movie_title):
    return f"""
    CREATE OR REPLACE FUNCTION get_movie_director(movie_title VARCHAR) RETURNS VARCHAR AS $$
    DECLARE
    director_name VARCHAR; BEGIN
    SELECT dr.director_name INTO director_name FROM movie m
    JOIN directed dr ON m.id = dr.id WHERE m.original_title = movie_title LIMIT 1;
    RETURN director_name; END;
    $$ LANGUAGE plpgsql;
    """

def count_movies_by_year_query(year):
    return f"""
    CREATE OR REPLACE FUNCTION count_movies_by_year(p_year INT) RETURNS INT AS $$
    DECLARE
    movie_count INT; BEGIN
    SELECT COUNT(*) INTO movie_count FROM release_details
    WHERE release_year = p_year; RETURN movie_count;
    END;
    $$ LANGUAGE plpgsql;
    """

def get_genre_by_movie_query(movie_title):
    return f"""
    CREATE OR REPLACE FUNCTION get_genre_by_movie(movie_title VARCHAR) RETURNS TABLE(genre_name VARCHAR) AS $$
    BEGIN
    RETURN QUERY SELECT mg.genre FROM movie m
    JOIN movie_genre mg ON m.id = mg.id WHERE m.original_title = movie_title;
    END;
    $$ LANGUAGE plpgsql;
    """

# Streamlit Page
def main_functions():
    st.markdown(
            """
            <style>
                /* Container styling for each query */
                
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

    st.title("Movie Database Functions with Queries")

    # Section 1: Movie Details
    st.header("1. Get Movie Details")
    movie_name = st.text_input("Enter Movie Name for Details")
    if st.button("Run 'Get Movie Details'"):
        result = run_query("SELECT * FROM get_movie_details(%s);", (movie_name,))
        df_movie_details = pd.DataFrame(result, columns=["Movie_id", "release_year","IMDB"])
        if  df_movie_details.empty :
            st.write("No data found for this movie.")
        else :
            st.markdown(f'<div class="header-text">Movie ID : {df_movie_details["Movie_id"][0]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="header-text">Release Year: {df_movie_details["release_year"][0]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="header-text">IMDB rating: {df_movie_details["IMDB"][0]}</div>', unsafe_allow_html=True)
    with st.expander("Show the Function"):
        st.code(get_movie_details_query("movie_name"), language="sql")

    # Section 2: Actor's Highest Grossing Movie
    st.header("2. Get Actor’s Highest Grossing Movie")
    
    actor_name = st.text_input("Enter Actor's Name")
    if st.button("Run 'Get Highest Grossing Movie'"):
        result1 = run_query("SELECT get_actor_highest_grossing_movie(%s);", (actor_name,))
        df_highest_grossing_movie = pd.DataFrame(result1, columns=["highest_grossing_movie "])
        if  df_highest_grossing_movie.empty :
            st.write("No data found for this actor.")
        else :
            st.markdown(f'<div class="header-text">Highest Grossing Movie of {actor_name}: {df_highest_grossing_movie["highest_grossing_movie "][0]}</div>', unsafe_allow_html=True)
    with st.expander("Show the Function"):
        st.code(get_actor_highest_grossing_movie_query("actor_name"), language="sql")



    # Section 3: Movie Director
    st.header("3. Get Director of a Movie")
    
    movie_title = st.text_input("Enter Movie Title for Director")
    if st.button("Run 'Get Movie Director'"):
        result2 = run_query("SELECT get_movie_director(%s);", (movie_title,))
        df_director = pd.DataFrame(result2, columns=["Director_name"])
        if  df_director.empty :
            st.write("No data found for this movie.")
        else :
            st.markdown(f'<div class="header-text">Director Name of {movie_title}: {df_director["Director_name"][0]}</div>', unsafe_allow_html=True)
    with st.expander("Show the Function"):
        st.code(get_movie_director_query("movie_title"), language="sql")       

    # Section 4: Count Movies by Year
    st.header("4. Count Movies by Year")
    
    year = st.number_input("Enter Release Year", min_value=1900, max_value=2024)
    if st.button("Run 'Count Movies by Year'"):
        result3 = run_query("SELECT count_movies_by_year(%s);", (year,))
        df_count = pd.DataFrame(result3, columns=["Movies_count"])
        if  df_count.empty :
            st.write("No data found for this year.")
        else :
            st.markdown(f'<div class="header-text">Movies Count of {year}: {df_count["Movies_count"][0]}</div>', unsafe_allow_html=True)
    with st.expander("Show the Function"):
        st.code(count_movies_by_year_query(2022), language="sql")       


    # Section 5: Genre by Movie Name
    st.header("5. Get Genre by Movie Name")
   
    movie_title_for_genre = st.text_input("Enter Movie Title for Genre")
    if st.button("Run 'Get Movie Genre'"):
        result4= run_query("SELECT * FROM get_genre_by_movie(%s);", (movie_title_for_genre,))
        df_genre = pd.DataFrame(result4, columns=["Genre"])
        if  df_genre.empty :
            st.write("No data found for this movie.")
        else :
            st.dataframe(df_genre)
    with st.expander("Show the Function"):
         st.code(get_genre_by_movie_query("movie_title"), language="sql")


if __name__ == "__main__":
    main_functions()
