import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu
import time




def main_dashboard():
            
            def fetch_metrics():
                metrics = {
                    "Total Movies": "SELECT COUNT(id) FROM movie;",
                    "Total Directors": "SELECT COUNT(DISTINCT director_name) FROM directed;",
                    "Total Actors": "SELECT COUNT(DISTINCT actor_name) FROM movie_cast;"
                }
                return {key: run_query(query)[0][0] for key, query in metrics.items()}

            def fetch_genre_distribution():
                query = """
                    SELECT mg.genre, COUNT(m.id) AS movie_count
                    FROM movie_genre mg
                    JOIN movie m ON mg.id = m.id
                    GROUP BY mg.genre
                    ORDER BY movie_count DESC
                """
                data = run_query(query)
                return pd.DataFrame(data, columns=["Genre", "Movie Count"])

            def fetch_revenue_trend():
                query = """
                    SELECT release_year, SUM(revenue) AS total_revenue
                    FROM release_details rd
                    JOIN finances f ON rd.id = f.id
                    GROUP BY release_year
                    ORDER BY release_year
                """
                data = run_query(query)
                return pd.DataFrame(data, columns=["Year", "Revenue"])

            

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
            
            metrics = fetch_metrics()
            col1,col4, col5 = st.columns(3)
            with col1:
                st.subheader("Total Movies")
                animate_metric(metrics["Total Movies"])
            with col4:
                st.subheader("Total Directors")
                animate_metric(metrics["Total Directors"])
            with col5:
                st.subheader("Total Actors")
                animate_metric(metrics["Total Actors"])

            # Main Page - Visualizations
            st.markdown("---")
            
            coln1, coln2 = st.columns([1, 1])

            with coln1:
                # Revenue Trend Line Chart
                revenue_df = fetch_revenue_trend()
                fig1 = px.line(
                    revenue_df, x="Year", y="Revenue",
                    title="Yearly Revenue Trend",
                    labels={"Year": "Year", "Revenue": "Total Revenue ($)"}
                )
                fig1.update_traces(line=dict(color="cyan", width=2))
                fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig1, use_container_width=True)

            with coln2:
                # Genre Distribution Bar Chart
                genre_df = fetch_genre_distribution()
                fig2 = px.pie(
                        genre_df, values="Movie Count", names="Genre",
                        title="Movie Count by Genre",
                        hole=0.3
                    )
                #fig2.update_traces(textinfo="percent+label")
                st.plotly_chart(fig2, use_container_width=True)

            # Additional Detailed View - Row 2
            st.markdown("---")
            coln3, coln4 = st.columns([1, 1])

            with coln3:
                # Top Directors by Number of Movies
                query_directors = """
                    SELECT d.director_name, COUNT(m.id) AS movie_count
                    FROM directed d
                    JOIN movie m ON d.id = m.id
                    GROUP BY d.director_name
                    ORDER BY movie_count DESC
                    LIMIT 5;
                """
                directors_data = run_query(query_directors)
                directors_df = pd.DataFrame(directors_data, columns=["Director", "Movie Count"])
                
                fig3 = px.bar(
                    directors_df, x="Movie Count", y="Director", orientation='h',
                    title="Top 5 Directors by Number of Movies",
                    labels={"Movie Count": "Number of Movies"}
                )
                fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig3, use_container_width=True)

            with coln4:
                # Top Actors by Number of Movies
                query_actors = """
                    SELECT c.actor_name, COUNT(m.id) AS movie_count
                    FROM movie_cast c
                    JOIN movie m ON c.id = m.id
                    GROUP BY c.actor_name
                    ORDER BY movie_count DESC
                    LIMIT 5;
                """
                actors_data = run_query(query_actors)
                actors_df = pd.DataFrame(actors_data, columns=["Actor", "Movie Count"])
                
                fig4 = px.bar(
                    actors_df, x="Movie Count", y="Actor", orientation='h',
                    title="Top 5 Actors by Number of Movies",
                    labels={"Movie Count": "Number of Movies"}
                )
                fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig4, use_container_width=True) 