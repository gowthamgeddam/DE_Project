import streamlit as st
import pandas as pd
from conn import run_query

def show_query5():
    # Number of records per page
    records_per_page = 5
    # Query with pagination
    def fetch_collaborations():
        query = f"""
            select * from collaboration
            """
        return run_query(query)
    
    # Fetch data
    data = fetch_collaborations()
    df = pd.DataFrame(data, columns=["Director", "Actor", "No. of Collaborations", "Highest Grossing Movie"])

    st.markdown("### For each director, actor with most collaborations and their highest grossing movie")
    st.dataframe(df, use_container_width=True)

def show_query10():
    # Query 10-- Which genres have the most profitable sequels and prequels?
    def fetch_query10():
        query = """
        SELECT movie_genre.genre, 
            SUM(finances.revenue - finances.budget) AS total_profit 
        FROM movie
        JOIN movie_genre ON movie.id = movie_genre.id
        JOIN finances ON movie.id = finances.id
        JOIN metadata ON movie.id = metadata.id
        WHERE ( 'sequel' = ANY(metadata.keywords) OR 'prequel' = ANY(metadata.keywords) )
        AND finances.budget > 0 AND finances.revenue > 0
        GROUP BY movie_genre.genre
        ORDER BY total_profit DESC;"""
        return run_query(query)
    
    # Fetch data
    data = fetch_query10()
    df = pd.DataFrame(data, columns=["Genre", "Total Profit"])

    st.markdown("### Genres vs. Total Profit (for sequels and prequels)")
    st.dataframe(df)