import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu
import time

def user_dashboard():
    # Custom CSS for background and header
    def add_custom_css():
        st.markdown(
            """
            <style>
            /* Background color for the page */
            body {
                background-color: #01172B;
            }
            .header1 {
                padding: 1rem;
                color: white;
                background-color: #4B6587;
                text-align: left;
                width: 100%;
                border-radius: 8px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logout-button {
                padding: 8px 16px;
                background-color: #333;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .dashboard_header{
             margin-bottom : 2rem;
             }
            </style>
            """,
            unsafe_allow_html=True
        )

    add_custom_css()

   
    if st.sidebar.button("Logout"):
        clear_session()

    with st.sidebar:
        selected = option_menu (menu_title = "User Dashboard",
                                options=["home","page1","page2","page3","page4","page5"],
                               default_index=0,
                               icons=("house","house","house","house","house","house"),
                               )
    
   

    st.markdown('<div class="dashboard_header"><div class="header1"><h1>User Dashboard</h1></div></div>', unsafe_allow_html=True)

    

    # Initialize session state variables for dashboard page and director offset
    
    if 'director_offset' not in st.session_state: #Query 1
        st.session_state['director_offset'] = 0
    if 'dir_offset' not in st.session_state: #Query 5
        st.session_state['dir_offset'] = 0
    if 'corr_offset' not in st.session_state: #Query 6
        st.session_state['corr_offset'] = 0
    

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
            DIRECTORS_PER_PAGE = 5

            def fetch_directors(offset, limit):
                query = f"""
                    SELECT d.director_name, COUNT(m.id) AS movie_count
                    FROM directed d
                    JOIN movie m ON d.id = m.id
                    GROUP BY d.director_name
                    ORDER BY movie_count DESC
                    LIMIT {limit} OFFSET {offset};
                """
                return run_query(query)

            # Fetch the current page of directors
            directors = fetch_directors(st.session_state['director_offset'], DIRECTORS_PER_PAGE)
            df_directors = pd.DataFrame(directors, columns=["Director Name", "Movies Directed"])

            # Display the top directors
            st.markdown('<div class="header-text">Top Directors by Number of Movies</div>', unsafe_allow_html=True)
            st.table(df_directors)

            # Pagination controls
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("Previous Directors") and st.session_state['director_offset'] >= DIRECTORS_PER_PAGE:
                    st.session_state['director_offset'] -= DIRECTORS_PER_PAGE

            with col2:
                if st.button("Next Directors"):
                    st.session_state['director_offset'] += DIRECTORS_PER_PAGE

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




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def show_main_dashboard2():
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

        ###############################################    Query3   ##############################################
        with coln1:
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
        with coln2:
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



        ####################################################  Query5 ##############################################

       

        ###############################################   end of Query5  ##############################################







































    def show_main_dashboard3():
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

       
        ####################################################  Query6 ##############################################

        with coln1:
                corr_per_page = 5
                if 'corr_offset' not in st.session_state:
                    st.session_state['corr_offset'] = 0

                # Query to get genre and correlation between popularity and revenue
                def corr(offset, limit):
                    query1 = f"""
                        SELECT mg.genre, CORR(imd.popularity, f.revenue) AS popularity_revenue_corr
                        FROM movie_genre mg
                        JOIN movie m ON mg.id = m.id
                        JOIN imdb_details imd ON m.id = imd.id
                        JOIN finances f ON m.id = f.id
                        GROUP BY mg.genre
                        ORDER BY popularity_revenue_corr DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query1)

                # Fetch the current page of correlation data
                corr_data = corr(st.session_state['corr_offset'], corr_per_page)
                df_corr = pd.DataFrame(corr_data, columns=["Genre", "Popularity_Revenue_Correlation"])

                # Display section header
                
                st.markdown('<div class="header-text">Correlation Heatmap: Popularity vs. Revenue by Genre</div>', unsafe_allow_html=True)
                # Generate a heatmap using Plotly
                fig = px.imshow(
                    df_corr.set_index("Genre").T,  # Transpose for a vertical heatmap
                    color_continuous_scale="RdBu",
                    aspect="auto",
                    title="Popularity and Revenue Correlation by Genre",
                    labels={"color": "Correlation Coefficient"},
                )
                fig.update_layout(
                    coloraxis_colorbar=dict(title="Correlation", tickvals=[-1, 0, 1], ticktext=["-1", "0", "1"]),
                    
                    plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16)
                )
                st.plotly_chart(fig)

                # Pagination controls for genres
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Previous Genres") and st.session_state['corr_offset'] >= corr_per_page:
                        st.session_state['corr_offset'] -= corr_per_page

                with col2:
                    if st.button("Next Genres"):
                        st.session_state['corr_offset'] += corr_per_page

                        
        ###############################################   end of Query6  ##############################################

        ###############################################    Query9   ##############################################
        with coln2:
                if 'actor_offset' not in st.session_state:
                    st.session_state['actor_offset'] = 0

                # Actors per page
                actors_per_page = 5

                # SQL query with LIMIT and OFFSET
                def fetch_high_rated_actors(offset, limit):
                    query = f"""
                        SELECT c.actor_name, COUNT(m.id) AS high_rated_movies_count
                        FROM movie_cast c
                        JOIN movie m ON c.id = m.id
                        JOIN imdb_details imd ON m.id = imd.id
                        JOIN movie_genre mg ON m.id = mg.id
                        WHERE imd.vote_average > 8.0
                        GROUP BY c.actor_name
                        ORDER BY high_rated_movies_count DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query)

                # Fetch data for the current page
                actors_data = fetch_high_rated_actors(st.session_state['actor_offset'], actors_per_page)
                df = pd.DataFrame(actors_data, columns=["Actor", "High Rated Movies Count"])
                st.markdown('<div class="header-text">Actors with the Most High-Rated Movies (Vote Average > 8.0)</div>', unsafe_allow_html=True)
                # Animated bar chart
                fig = px.bar(
                    df, x="High Rated Movies Count", y="Actor", orientation='h',
                    
                    labels={"High Rated Movies Count": "Number of High-Rated Movies"}
                )

                # Set initial bar lengths to zero for animation
                fig.update_traces(marker_color="lightblue", base=0)
                fig.update_layout(
                    plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16)
                )

                # Display the animated chart
                st.plotly_chart(fig, use_container_width=True)
               

                # Pagination controls
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    if st.button("Previous Actors") and st.session_state['actor_offset'] >= actors_per_page:
                        st.session_state['actor_offset'] -= actors_per_page

                with col3:
                    if st.button("Next Actors"):
                        st.session_state['actor_offset'] += actors_per_page

        ###############################################   end of Query9  ##############################################


   
   
   
   
   
   












    def show_main_dashboard4():
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

       
        ####################################################  Query7 ##############################################

        with coln1:
                # Initialize session state for pagination
                if 'rating_diff_offset' not in st.session_state:
                    st.session_state['rating_diff_offset'] = 0

                # Number of records per page
                records_per_page = 5

                # Query with pagination
                def fetch_rating_diff(offset, limit):
                    query = f"""
                        WITH AvgRatings AS (
                            SELECT c.actor_name, mg.genre, AVG(imd.vote_average) AS avg_vote
                            FROM movie_cast c
                            JOIN movie m ON c.id = m.id
                            JOIN movie_genre mg ON m.id = mg.id
                            JOIN imdb_details imd ON m.id = imd.id
                            WHERE mg.genre IN ('Drama', 'Comedy')
                            GROUP BY c.actor_name, mg.genre
                        )
                        SELECT a1.actor_name, a1.avg_vote - a2.avg_vote AS rating_diff
                        FROM AvgRatings a1
                        JOIN AvgRatings a2 ON a1.actor_name = a2.actor_name
                        WHERE a1.genre = 'Drama' AND a2.genre = 'Comedy'
                        ORDER BY rating_diff DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query)

                # Fetch data for the current page
                rating_diff_data = fetch_rating_diff(st.session_state['rating_diff_offset'], records_per_page)
                df = pd.DataFrame(rating_diff_data, columns=["Actor", "Rating Difference (Drama - Comedy)"])
                st.markdown('<div class="header-text">Top Actors by Rating Difference between Drama and Comedy Genres</div>', unsafe_allow_html=True)
                # Create a bar chart
                fig = px.bar(
                    df, x="Rating Difference (Drama - Comedy)", y="Actor", orientation='h',
                    
                    labels={"Rating Difference (Drama - Comedy)": "Rating Difference"}
                )

                # Customize plot appearance
                fig.update_layout(
                    plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16)
                )

                # Display the plot
                st.plotly_chart(fig, use_container_width=True)

                # Pagination controls
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    if st.button("Previous Actors") and st.session_state['rating_diff_offset'] >= records_per_page:
                        st.session_state['rating_diff_offset'] -= records_per_page

                with col3:
                    if st.button("Next Actors"):
                        st.session_state['rating_diff_offset'] += records_per_page

                        
        ###############################################   end of Query7  ##############################################

        ###############################################    Query8   ##############################################
        with coln2:
                 # Initialize session state for pagination
                if 'prod_offset' not in st.session_state:
                    st.session_state['prod_offset'] = 0

                # Number of records per page
                records_per_page = 5

                # Query with pagination
                def fetch_top_production_companies(offset, limit):
                    query = f"""
                        SELECT p.production_company, SUM(f.revenue) AS total_revenue
                        FROM production p
                        JOIN movie m ON p.id = m.id
                        JOIN finances f ON m.id = f.id
                        JOIN movie_genre mg ON m.id = mg.id
                        GROUP BY p.production_company
                        ORDER BY total_revenue DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query)

                # Fetch data for the current page
                data = fetch_top_production_companies(st.session_state['prod_offset'], records_per_page)
                df = pd.DataFrame(data, columns=["Production Company", "Total Revenue"])
                st.markdown('<div class="header-text">Top Production Companies by Total Revenue</div>', unsafe_allow_html=True)
                # Create a bar chart using Plotly
                fig = px.bar(
                    df, x="Total Revenue", y="Production Company", orientation='h',
                    
                    labels={"Total Revenue": "Total Revenue", "Production Company": "Production Company"}
                )
                fig.update_layout(
                    plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    title_font=dict(size=16)
                )


                # Display the chart
                st.plotly_chart(fig, use_container_width=True)

                # Pagination controls
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    if st.button("Previous Companies") and st.session_state['prod_offset'] >= records_per_page:
                        st.session_state['prod_offset'] -= records_per_page

                with col3:
                    if st.button("Next Companies"):
                        st.session_state['prod_offset'] += records_per_page

        ###############################################   end of Query8  ##############################################










   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    def show_main_dashboard5():
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

       
        ####################################################  Query5 ##############################################

        with coln1:
                # Initialize session state for pagination
                 if 'collab_offset' not in st.session_state:
                    st.session_state['collab_offset'] = 0

                # Number of records per page
                 records_per_page = 5

                # Query with pagination
                 def fetch_collaborations(offset, limit):
                    query = f"""
                        WITH DirectorActorCollab AS (
                            SELECT d.director_name, c.actor_name, COUNT(m.id) AS collab_count, MAX(f.revenue) AS highest_gross
                            FROM directed d
                            JOIN movie m ON d.id = m.id
                            JOIN movie_cast c ON m.id = c.id
                            JOIN finances f ON m.id = f.id
                            GROUP BY d.director_name, c.actor_name
                        )
                        SELECT director_name, actor_name, collab_count, highest_gross
                        FROM DirectorActorCollab
                        ORDER BY collab_count DESC
                        LIMIT {limit} OFFSET {offset};
                    """
                    return run_query(query)

                # Fetch data for the current page
                 data = fetch_collaborations(st.session_state['collab_offset'], records_per_page)
                 df = pd.DataFrame(data, columns=["Director", "Actor", "Collaboration Count", "Highest Gross"])
                 st.markdown('<div class="header-text">Collaboration Count and Highest Grossing Revenue for Top Director-Actor Pairs</div>', unsafe_allow_html=True)
                # Reshape the data for grouped bar chart
                 df_melted = df.melt(id_vars=["Director", "Actor"], 
                                    value_vars=["Collaboration Count", "Highest Gross"], 
                                    var_name="Metric", 
                                    value_name="Value")

                # Plot: Grouped Bar Chart
                 fig = px.bar(
                    df_melted, x="Actor", y="Value", color="Metric", barmode="group",
                    
                    labels={"Value": "Count / Revenue", "Actor": "Actor"}
                )
                 fig.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)", 
                    xaxis=dict(showgrid=False),
                    yaxis_title="Value",
                    xaxis_title="Actor",
                )

                # Display the grouped bar chart
                 st.plotly_chart(fig, use_container_width=True)

                # Pagination controls
                 col1, col2, col3 = st.columns([1, 2, 1])
                 with col1:
                    if st.button("Previous Collaborations") and st.session_state['collab_offset'] >= records_per_page:
                        st.session_state['collab_offset'] -= records_per_page

                 with col3:
                    if st.button("Next Collaborations"):
                        st.session_state['collab_offset'] += records_per_page
                        
        ###############################################   end of Query5  ##############################################

        ###############################################    Query10  ##############################################
        

        ###############################################   end of Query10  ##############################################   












    def main_dashboard():
            
            def fetch_metrics():
                metrics = {
                    "Total Movies": "SELECT COUNT(id) FROM movie;",
                    "Total Revenue": "SELECT SUM(revenue) FROM finances;",
                    "Average Rating": "SELECT AVG(vote_average) FROM imdb_details;",
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

            # Sidebar
            with st.sidebar:
                  # Update path to your logo
                st.title("Movie Metrics Dashboard")
                st.markdown("**Navigate**")
                st.button("Home")
                st.button("Movies")
                st.button("Directors")
                st.button("Actors")
                st.button("Genres")

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
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.subheader("Total Movies")
                animate_metric(metrics["Total Movies"])
            with col2:
                st.subheader("Total Revenue")
                animate_metric(metrics["Total Revenue"])
            with col3:
                st.subheader("Average Rating")
                animate_metric(round(metrics["Average Rating"], 2))
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
                fig2.update_traces(textinfo="percent+label")
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
   
   
   
   
   
   
   
   
   
   
    if selected == "home":
        main_dashboard()
    elif selected == "page1":
        show_main_dashboard1()
    elif selected == "page2":
        show_main_dashboard2()
    elif selected == "page3":
        show_main_dashboard3()
    elif selected == "page4":
        show_main_dashboard4()
    else:
        show_main_dashboard5()



     






