import pandas as pd
import plotly.express as px
from conn import run_query
import streamlit as st
from logout import clear_session
from streamlit_option_menu import option_menu





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
        coln1, coln2 = st.columns([1, 1])

       
        ####################################################  Query6 ##############################################

        with coln1:
                

                # Query to get genre and correlation between popularity and revenue
                def corr():
                    query1 = """
                        SELECT mg.genre, CORR(imd.popularity, f.revenue) AS popularity_revenue_corr
                        FROM movie_genre mg
                        JOIN movie m ON mg.id = m.id
                        JOIN imdb_details imd ON m.id = imd.id
                        JOIN finances f ON m.id = f.id
                        GROUP BY mg.genre
                        ORDER BY popularity_revenue_corr DESC;
                    """
                    data = run_query(query1)
                    return pd.DataFrame(data, columns=["Genre", "Popularity_revenue_corr"])
                
                # Revenue Trend Line Chart
                revenue_df = corr()
                st.markdown('<div class="header-text"> Popularity vs. Revenue by Genre</div>', unsafe_allow_html=True)
                fig1 = px.line(
                    revenue_df, x="Genre", y="Popularity_revenue_corr",
                   labels={"Year": "Year", "Revenue": "Total Revenue ($)"}
                )
                fig1.update_layout(
                   
                    plot_bgcolor="#2b2b2b",
                    paper_bgcolor="#2b2b2b",
                    font_color="#cfd8dc",
                    xaxis=dict(showgrid=False, color="#cfd8dc"),
                    yaxis=dict(color="#cfd8dc"),
                    
                )
                fig1.update_traces(line=dict(color="cyan", width=2))
                fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)")
                st.plotly_chart(fig1, use_container_width=True)


                        
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
        coln3, coln4 = st.columns([1, 1])

       
        ####################################################  Query7 ##############################################

        with coln3:
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
                    
                )

                # Display the plot
                st.plotly_chart(fig, use_container_width=True)

                # Pagination controls
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    if st.button("Previous Actors1") and st.session_state['rating_diff_offset'] >= records_per_page:
                        st.session_state['rating_diff_offset'] -= records_per_page

                with col3:
                    if st.button("Next Actors1"):
                        st.session_state['rating_diff_offset'] += records_per_page

                        
        ###############################################   end of Query7  ##############################################

        ###############################################    Query8   ##############################################
        with coln4:
                st.markdown('<div class="header-text">Top Production Companies by Total Revenue in each Genre</div>', unsafe_allow_html=True)
                gen_list = run_query("SELECT DISTINCT genre FROM movie_genre ORDER BY genre")
                genres = [genre[0] for genre in gen_list]

                #genres = gen_list['genre'].tolist()
                selected_genre = st.selectbox("Select Genre:", genres)

                # Fetch and display data on submit
                if st.button("Show Top 5 Production Companies"):
                    
                    result_df =run_query("SELECT * FROM get_top_production_companies_by_genre(%s);", (selected_genre,))
                    df_top5 = pd.DataFrame(result_df, columns=["Production company", "Total Revenue"])
                    if not df_top5.empty:
                        st.write(f"Top 5 Production Companies in {selected_genre} genre:")
                        st.table(df_top5)
                    else:
                        st.write("No data found for the selected genre.")


              

        ###############################################   end of Query8  ##############################################



