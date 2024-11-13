import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu









def show_main_dashboard1():
        st.markdown(
            """
            <style>
                /* Container styling for each query */
                .query-container {
                    padding: 1rem;
                    margin: 1rem 0;
                    background-color: #f0f2f6; /* Light background for better contrast */
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Slight shadow for depth */
                }
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


        coln1, coln2 = st.columns([1, 1])

        ###############################################    Query1   ##############################################
        with coln1:
            
            

            def fetch_directors():
                query = f"""
                    SELECT d.director_name, COUNT(m.id) AS movie_count
                    FROM directed d
                    JOIN movie m ON d.id = m.id
                    GROUP BY d.director_name
                    ORDER BY movie_count DESC
                    LIMIT 5;
                """
                return run_query(query)

            # Fetch the current page of directors
            directors = fetch_directors()
            df_directors = pd.DataFrame(directors, columns=["Director Name", "Movies Directed"])

            # Display the top directors
            st.markdown('<div class="header-text">Top Directors by Number of Movies</div>', unsafe_allow_html=True)
            fig2 = px.pie(
                        df_directors, values="Movies Directed", names="Director Name",
                        title="Movies Count",
                        hole=0.3
                    )
            fig2.update_layout(plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16))
            fig2.update_traces(textinfo="percent+label")
            st.plotly_chart(fig2, use_container_width=True)


           

        ###############################################   end of Query1   ##############################################

        ###############################################    Query2   ##############################################
        with coln2:
            query1 = """
                SELECT m.original_title, f.revenue / f.budget AS profit_margin 
                FROM movie m  
                JOIN finances f ON m.id = f.id 
                WHERE f.budget > 0 
                ORDER BY profit_margin DESC 
                LIMIT 5;
            """
            movie_data = run_query(query1)
            df = pd.DataFrame(movie_data, columns=["movie_title", "profit_margin"])

            
            st.markdown('<div class="header-text">Revenue-to-Budget Ratio:</div>', unsafe_allow_html=True)
            tab1,tab2= st.tabs(["Bar Chart", "Scatter Plot"])

            
            fig1 = px.bar(df, x="movie_title", y="profit_margin", title="Highest Profit Margin")
            fig1.update_layout(plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16))
            tab1.plotly_chart(fig1)
           
            fig2 = px.scatter(df, x="movie_title", y="profit_margin", title="Highest Profit Margin")
            fig2.update_layout(plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16))
            tab2.plotly_chart(fig2)
            
            

        ###############################################   end of Query2  ##############################################
        

        coln3, coln4 = st.columns([1, 1])

        ###############################################    Query3   ##############################################
        with coln3:
            # Wrapping the first query in a styled container
            
            st.markdown('<div class="header-text">Directors with the Most Movies in the Top 100 Grossing Films</div>', unsafe_allow_html=True)

            query = """
                SELECT d.director_name, COUNT(m.id) AS movie_count
                FROM directed d
                JOIN movie m ON d.id = m.id
                JOIN (
                    SELECT id
                    FROM finances
                    ORDER BY revenue DESC
                    LIMIT 100
                ) AS top_movies ON m.id = top_movies.id
                GROUP BY d.director_name
                ORDER BY movie_count DESC;
            """
            data = run_query(query)
            df = pd.DataFrame(data, columns=["Director", "Movie Count"])

            fig = px.bar(
                df, x="Movie Count", y="Director", orientation='h',
                
                labels={"Movie Count": "Number of Movies"}
            )
            fig.update_layout(plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16))
            st.plotly_chart(fig)

            


        ###############################################   end of Query3   ##############################################

        ###############################################    Query4  ##############################################
        with coln4:
        # Wrapping the second query in a styled container
                st.markdown('<div class="header-text">Actors with the Highest Average Vote in Sci-Fi Movies</div>', unsafe_allow_html=True)

                query = """
                    SELECT c.actor_name, AVG(imd.vote_average) AS avg_vote
                    FROM movie_cast c
                    JOIN movie m ON c.id = m.id
                    JOIN movie_genre mg ON m.id = mg.id
                    JOIN imdb_details imd ON m.id = imd.id
                    WHERE mg.genre = 'Science Fiction'
                    GROUP BY c.actor_name
                    ORDER BY avg_vote DESC
                    LIMIT 5;
                """
                data = run_query(query)
                df = pd.DataFrame(data, columns=["Actor", "Average Vote"])

                fig = px.scatter(
                    df, x="Actor", y="Average Vote",
                    size="Average Vote", color="Average Vote", color_continuous_scale="Viridis",
                    
                )
                fig.update_layout(plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16))
                st.plotly_chart(fig)

                

        ###############################################   end of Query4  ##############################################



    
    
    
    
    
    
    
    