import streamlit as st
import pandas as pd
from conn import run_query

def show_query5():
    # Number of records per page
    records_per_page = 5
    # Query with pagination
    def fetch_collaborations():
        query = f"""
            WITH collaboration_counts AS (
                SELECT
                    d.director_name,
                    c.actor_name,
                    COUNT(*) AS collaboration_count
                FROM
                    public.directed d
                JOIN
                    public.movie_cast c ON d.id = c.id
                GROUP BY
                    d.director_name, c.actor_name
            )
            SELECT
                director_name,
                actor_name,
                collaboration_count
            FROM (
                SELECT
                    director_name,
                    actor_name,
                    collaboration_count,
                    ROW_NUMBER() OVER (PARTITION BY director_name ORDER BY collaboration_count DESC) AS rank
                FROM
                    collaboration_counts
            ) ranked
            WHERE
                rank = 1
            ORDER BY
                collaboration_count DESC;
            """
        return run_query(query)
    
    # Fetch data
    data = fetch_collaborations()
    df = pd.DataFrame(data, columns=["Director", "Actor", "No. of Collaborations"])

    st.write("For each director, the actor they collaborated the most with::")
    st.dataframe(df)

def show_query10():
    coln1, coln2, coln3 = st.columns([1, 1, 1])
    with coln1:
        st.markdown('---')
    with coln2:
        st.markdown('## Work in Progress')
    with coln3:
        st.markdown('---')