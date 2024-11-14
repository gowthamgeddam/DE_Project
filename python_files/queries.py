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
    st.dataframe(df)

def show_query10():
    # Query 10-- Which genres have the most profitable sequels and prequels?
    def fetch_query10():
        query = """
        SELECT movie_genre.genre, 
            AVG(finances.revenue_adj / finances.budget_adj) AS avg_profit_margin 
        FROM movie
        JOIN movie_genre ON movie.id = movie_genre.id
        JOIN finances ON movie.id = finances.id
        JOIN metadata ON movie.id = metadata.id
        WHERE ( 'sequel' = ANY(metadata.keywords) OR 'prequel' = ANY(metadata.keywords) )
        AND finances.budget_adj > 0 AND finances.revenue_adj > 0
        GROUP BY movie_genre.genre
        ORDER BY avg_profit_margin DESC;"""
        return run_query(query)
    
    # Fetch data
    data = fetch_query10()
    df = pd.DataFrame(data, columns=["Genre", "Average Profit Margin"])

    st.markdown("### Genres vs. Average profit margin (for sequels and prequels)")
    st.dataframe(df)